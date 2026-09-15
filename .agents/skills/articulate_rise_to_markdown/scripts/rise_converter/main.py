import argparse
import concurrent.futures
from pathlib import Path

from .extractor import extract_json_from_js
from .media_handler import validate_url, download_file, fetch_youtube_transcript, download_video_yt_dlp, extract_youtube_id
from .ai_client import AIClient
from .markdown_formatter import format_text, format_list, format_interactive
from .interactive_prompter import ask_deep_video_analysis

def process_image_task(item, output_dir, base_url, ai_client):
    media_item = item.get("items", [{}])[0] if item.get("items") else item
    media = media_item.get('media', {}).get('image', {})
    original_url = media.get('originalUrl')
    if not original_url:
        return ""
    
    img_url = f"{base_url}/assets/{original_url}"
    img_path = output_dir / original_url
    
    if not download_file(img_url, img_path):
        return f"![Image]({original_url})\n\n"
        
    if False: # Disabled: Agent will process images manually using multimodal capabilities
        result = ai_client.analyze_image_as_mermaid(img_path)
        if result:
            return f"\n{result}\n\n"
            
    return f"![Image]({original_url})\n\n"

def process_video_task(item, output_dir, ai_client):
    media_item = item.get("items", [{}])[0] if item.get("items") else item
    media = media_item.get('media', {}).get('embed', {})
    url = media.get('originalUrl')
    title = media.get('title', 'YouTube Video')
    desc = media.get('description', '')
    
    if not url or 'youtube' not in url.lower():
        return ""
        
    fallback_text = f"**Video Link:** [{title}]({url})\n\n>{desc}\n\n"
    
    if not ai_client.enabled:
        return fallback_text

    use_deep = ask_deep_video_analysis(title, url)
    
    if use_deep:
        print("Executing Approach 1: Deep Visual Analysis...")
        video_path = output_dir / "temp_video.mp4"
        try:
            print("Downloading video with yt-dlp...")
            download_video_yt_dlp(url, video_path)
            
            print("Uploading to Gemini and generating summary...")
            result = ai_client.summarize_video_file(title, video_path)
            
            if video_path.exists():
                video_path.unlink()
                
            if result:
                return f"### Deep Video Summary: [{title}]({url})\n\n{result}\n\n"
        except Exception as e:
            print(f"Deep video processing failed: {e}")
            if video_path.exists():
                video_path.unlink()
            print("Falling back to transcript summary...")
            
    # Approach 2 or fallback from Approach 1
    print("Executing Approach 2: Transcript Summary...")
    video_id = extract_youtube_id(url)
    if not video_id:
        return fallback_text
        
    try:
        transcript_text = fetch_youtube_transcript(video_id)
        result = ai_client.summarize_transcript(title, transcript_text)
        if result:
            return f"### Video Summary: [{title}]({url})\n\n{result}\n\n"
    except Exception as e:
        print(f"Failed to fetch transcript: {e}")
        
    return fallback_text

def sanitize_filename(name):
    import re
    return re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')

def main():
    parser = argparse.ArgumentParser(description="Convert Articulate Rise to Markdown")
    parser.add_argument("--input", required=True, help="Path to runtime-data.js")
    parser.add_argument("--output", default="markdown_output", help="Output directory")
    parser.add_argument("--base-url", required=True, help="Base URL to the content folder to download assets")
    parser.add_argument("--parallel", type=int, default=10, help="Number of parallel image processing threads")
    args = parser.parse_args()

    print("Validating Base URL...")
    if not validate_url(args.base_url):
        print("Warning: The provided base URL may be invalid or unreachable. Proceeding anyway...")

    ai_client = AIClient()
    if not ai_client.enabled:
        print("WARNING: Gemini API Key not found. Skipping Multimodal processing.")

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Parsing JSON...")
    course_data = extract_json_from_js(args.input)
    course = course_data.get("course", {})
    lessons = course.get("lessons", [])

    print(f"Course Title: {course.get('title')}")
    
    current_module_dir = output_dir
    module_counter = 1

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel)

    for lesson in lessons:
        lesson_type = lesson.get("type")
        lesson_title = sanitize_filename(lesson.get("title", "Untitled"))
        
        if lesson_type == "section":
            dir_name = f"{module_counter:02d}_{lesson_title}"
            current_module_dir = output_dir / dir_name
            current_module_dir.mkdir(exist_ok=True)
            module_counter += 1
            print(f"\nCreated Section: {dir_name}")
            continue

        if lesson_type == "blocks":
            md_path = current_module_dir / f"{lesson_title}.md"
            print(f"  Generating: {md_path}")
            
            items_to_write = []
            
            for item in lesson.get("items", []):
                item_type = item.get("type")
                
                def extract_text_recursive(data, text_keys={"title", "description", "paragraph", "heading", "caption"}):
                    content = ""
                    if isinstance(data, dict):
                        for k, v in data.items():
                            if k in text_keys and isinstance(v, str):
                                content += format_text(v)
                            else:
                                content += extract_text_recursive(v, text_keys)
                    elif isinstance(data, list):
                        for d in data:
                            content += extract_text_recursive(d, text_keys)
                    return content
                
                if item_type == "list":
                    items_to_write.append(("text", format_list(item.get("items", []))))
                    
                elif item_type == "image":
                    future = executor.submit(process_image_task, item, current_module_dir, args.base_url, ai_client)
                    items_to_write.append(("future", future))
                    extracted = extract_text_recursive(item)
                    if extracted.strip():
                        items_to_write.append(("text", f"{extracted.strip()}\n\n"))
                    
                elif item_type == "multimedia":
                    # Synchronous to allow user input prompt
                    items_to_write.append(("text", process_video_task(item, output_dir, ai_client)))
                    
                elif item_type == "interactive":
                    items_to_write.append(("text", format_interactive(item)))
                    
                elif item_type == "divider":
                    items_to_write.append(("text", "---\n\n"))
                    
                else:
                    # Generic recursive text extraction for "text" or any unhandled block type
                    extracted = extract_text_recursive(item)
                    if extracted.strip():
                        items_to_write.append(("text", f"{extracted.strip()}\n\n"))
                    elif item_type != "text":
                        print(f"Warning: Unhandled block type '{item_type}' with no obvious text content.")

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {lesson.get('title')}\n\n")
                for kind, content in items_to_write:
                    if kind == "future":
                        f.write(content.result())
                    else:
                        f.write(content)

    executor.shutdown(wait=True)
    print("\nConversion Complete.")

if __name__ == "__main__":
    main()
