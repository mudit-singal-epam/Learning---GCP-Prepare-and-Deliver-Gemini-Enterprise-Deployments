try:
    from markdownify import markdownify as md
except ImportError:
    md = lambda x: x # Fallback if not installed

def format_text(html_content):
    """Converts HTML paragraph to Markdown."""
    text = md(html_content).strip()
    return text + "\n\n"

def format_list(items):
    """Converts a list of HTML items to a Markdown bulleted list."""
    list_content = ""
    for li in items:
        list_content += "- " + md(li.get("paragraph", "")).strip() + "\n"
    return list_content + "\n"

def format_interactive(item):
    """Parses flashcards, tabs, accordions into markdown lists or headers."""
    content = ""
    variant = item.get("variant", "")
    items = item.get("items", [])
    
    if variant == "flashcard":
        for idx, card in enumerate(items):
            front = md(card.get("front", {}).get("description", "")).strip()
            back = md(card.get("back", {}).get("description", "")).strip()
            content += f"* {front}\n"
            content += f"  * {back}\n"
    elif variant in ["accordion", "tabs"]:
        for idx, panel in enumerate(items):
            title = md(panel.get("title", "")).strip()
            desc = md(panel.get("description", "")).strip()
            content += f"### {title}\n\n{desc}\n\n"
    elif variant == "process":
        for idx, step in enumerate(items):
            title = md(step.get("title", "")).strip()
            desc = md(step.get("description", "")).strip()
            content += f"{idx+1}. **{title}**\n   {desc}\n"
    else:
        content += f"> [!NOTE]\n> Interactive Element (Type: {variant}) - Review Original Course\n\n"
        
    return content
