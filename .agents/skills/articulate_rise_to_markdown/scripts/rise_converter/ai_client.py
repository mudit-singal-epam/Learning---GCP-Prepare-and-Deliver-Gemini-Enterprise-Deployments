import os
import time
import threading

try:
    from google import genai
    has_genai = True
except ImportError:
    has_genai = False

class AIClient:
    def __init__(self):
        self.enabled = has_genai and bool(os.environ.get("GEMINI_API_KEY"))
        self.lock = threading.Lock()
        self.api_call_count = 0
        self.api_window_minute = int(time.time() / 60)
        if self.enabled:
            self.client = genai.Client()
        else:
            self.client = None

    def _wait_for_rate_limit(self):
        if not self.enabled:
            return
        with self.lock:
            current_minute = int(time.time() / 60)
            if current_minute > self.api_window_minute:
                self.api_call_count = 0
                self.api_window_minute = current_minute
            
            if self.api_call_count >= 15:
                next_minute_boundary = (self.api_window_minute + 1) * 60
                sleep_duration = next_minute_boundary - time.time() + 1.0
                if sleep_duration > 0:
                    print(f"Rate limit (15 requests/min) reached. Thread sleeping for {sleep_duration:.1f} seconds until next minute window...")
                    time.sleep(sleep_duration)
                
                self.api_window_minute = int(time.time() / 60)
                self.api_call_count = 0
                
            self.api_call_count += 1

    def call_gemini_with_backoff(self, prompt, file_path=None, max_retries=5, base_delay=2):
        """Executes a Gemini API call with exponential backoff for rate limits."""
        if not self.enabled:
            return None
            
        for attempt in range(max_retries):
            try:
                contents = [prompt]
                g_file = None
                
                if file_path:
                    # Upload the file to Gemini File API
                    self._wait_for_rate_limit()
                    g_file = self.client.files.upload(file=str(file_path))
                    
                    # Wait for processing if it's a video
                    while g_file.state.name == "PROCESSING":
                        time.sleep(10)
                        g_file = self.client.files.get(name=g_file.name)
                        
                    if g_file.state.name == "FAILED":
                        raise Exception("Gemini file processing failed.")
                        
                    contents.append(g_file)
                
                self._wait_for_rate_limit()
                response = self.client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=contents
                )
                
                if g_file:
                    self.client.files.delete(name=g_file.name)
                    
                return response.text
                
            except Exception as e:
                error_msg = str(e).lower()
                if "403" in error_msg or "400" in error_msg or "api key not valid" in error_msg:
                    print(f"API Authentication Error: {e}. Skipping retries.")
                    return None
                
                if "429" in str(e) or attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)
                    print(f"[Attempt {attempt+1}/{max_retries}] API Error: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
                else:
                    print(f"Gemini processing failed after {max_retries} attempts: {e}")
                    return None

    def analyze_image_as_mermaid(self, img_path):
        """Prompts Gemini to convert an image to a Mermaid diagram or text description."""
        prompt = (
            "Analyze this image. If it is an architecture diagram or a chart, "
            "convert it into a valid Mermaid.js diagram. Wrap the diagram in ```mermaid ... ``` codeblocks. "
            "If it is a regular picture or icon, output a short 1-sentence description."
        )
        return self.call_gemini_with_backoff(prompt, file_path=img_path)

    def summarize_transcript(self, title, transcript_text):
        """Prompts Gemini to summarize a video transcript."""
        prompt = f"Please provide a detailed, comprehensive summary of the following video transcript for '{title}':\n\n{transcript_text}"
        return self.call_gemini_with_backoff(prompt)

    def summarize_video_file(self, title, video_path):
        """Prompts Gemini to summarize a physical video file."""
        prompt = "Please provide a detailed, comprehensive summary of this educational video, including visual demonstrations on screen."
        return self.call_gemini_with_backoff(prompt, file_path=video_path)
