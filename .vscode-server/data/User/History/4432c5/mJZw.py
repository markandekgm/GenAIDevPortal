
import requests

builder_api = "https://api.builder.io/api/v1/write"
headers = {"Authorization": "Bearer d9bdea4ccd684c8c8c0c72e9211482a1"}
payload = {"figma_url": "your-figma-url"}

response = requests.post(builder_api, headers=headers, json=payload)
if response.ok:
    print("Builder.io UI components generated.")
else:
    print(f"Error: {response.status_code}")
