---
name: articulate_rise_to_markdown
description: A robust skill for converting exported Articulate Rise courses (runtime-data.js) into GitHub-style Markdown repositories, utilizing the Gemini API for image-to-Mermaid conversion and video summarization.
---

# Articulate Rise to Markdown Conversion

This skill provides a methodology and script for converting Articulate Rise 360 web exports into beautifully formatted Markdown files, neatly organized into a module/lesson folder structure.

## Features

- **JSON Parsing**: Extracts the entire course payload from `runtime-data.js` (Base64 decoded).
- **Directory Structuring**: Creates a folder for each "section" (module) and a markdown file for each "block" (lesson).
- **Interactive Elements**: Parses flashcards, accordions, and tabs into nested bullet points and headers.
- **Multimodal AI Processing (Gemini)**:
  - **Images (Hybrid Workflow)**: The automated script intentionally leaves `![Image](path)` placeholders in the markdown to save API quota. As the **Agent**, you must explicitly use your internal `view_file` multimodal vision to manually read these images, generate the Mermaid diagrams, and rewrite the markdown files to insert them. This is an autonomous post-processing step!
  - **Header Nesting (Post-Processing)**: The extraction script faithfully extracts bold text as `**bold**`, even if the course author intended it to be a section header. As the **Agent**, you must read the generated markdown and use your context awareness to intelligently promote standalone bold text into proper Markdown headers (e.g., `##` or `###`), ensuring the nesting levels are logically correct and do not violate Markdown lint rules (like skipping from H1 to H3).
  - **Videos**: Uses `yt-dlp` to download embedded YouTube videos, uploads them to the Gemini API, and extracts a detailed summary using native video processing.

## Usage

When a user wants to create a local markdown copy of an Articulate Rise course, run the provided Python script located in this skill's `scripts/` directory.

### Requirements

- The user must provide their `GEMINI_API_KEY` as an environment variable.
- `pip install google-genai markdownify yt-dlp youtube-transcript-api`

### Execution

Run the conversion script on the `runtime-data.js` file:

```bash
export GEMINI_API_KEY="your_api_key_here"
python3 .agents/skills/articulate_rise_to_markdown/scripts/convert_rise.py --input path/to/runtime-data.js --output path/to/output_dir --base-url "https://storage.googleapis.com/.../content"
```

The `--base-url` parameter should point to the root `content/` folder of the course (e.g., `https://storage.googleapis.com/cloud-training/cls-html5-courses/P-DLGITD-I/content`) so the script can download the assets and videos.
