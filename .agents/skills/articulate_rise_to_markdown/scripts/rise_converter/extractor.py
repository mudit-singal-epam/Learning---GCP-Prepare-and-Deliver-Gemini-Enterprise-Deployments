import base64
import json

def extract_json_from_js(js_path):
    """Reads the runtime-data.js file, decodes the base64 payload, and returns the JSON dictionary."""
    with open(js_path, 'r', encoding='utf-8') as f:
        data = f.read()
    
    start = data.find('","') + 3
    end = data.rfind('")')
    
    if start < 3 or end == -1:
        raise ValueError("Could not find base64 JSON payload in JS file.")
        
    b64_str = data[start:end]
    json_str = base64.b64decode(b64_str).decode('utf-8')
    return json.loads(json_str)
