
import requests

windsurf_api = "https://api.windsurf.ai/v1/generate"
payload = {"figma_file_url": "your-figma-url"}

response = requests.post(windsurf_api, json=payload)
if response.status_code == 200:
    with open('windsurf_stories.json', 'w') as f:
        f.write(response.text)
print("Windsurf stories generated.")
