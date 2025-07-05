
import requests

url = "https://dev.azure.com/{organization}/{project}/_apis/pipelines/{pipelineId}/runs?api-version=6.0-preview.1"
response = requests.post(url, auth=('username', 'personal_access_token'))

if response.status_code == 200:
    print("Pipeline triggered successfully.")
else:
    print(f"Error: {response.status_code}, {response.text}")
