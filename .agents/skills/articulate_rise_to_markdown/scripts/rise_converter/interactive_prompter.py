def ask_deep_video_analysis(title, url):
    """
    Prompts the user in the terminal to choose between 
    deep visual analysis (slow) or fast transcript extraction.
    """
    print(f"\n--- VIDEO DETECTED ---")
    print(f"Title: {title}")
    print(f"URL: {url}")
    print("\nRunning in automated headless mode. Defaulting to fast text-only transcription (Approach 2).")
    print("\nBy default, the script uses fast text-only transcription (Approach 2).")
    print("Deep Visual Analysis (Approach 1) downloads the video to analyze visual frames.")
    print("WARNING: Approach 1 is slow, consumes bandwidth, and may fail if YouTube blocks the download.")
    return False
