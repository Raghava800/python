import requests

file_url = "https://www.timestored.com/data/sample/titanic.parquet"

response = requests.get(file_url, stream = True)

if response.status_code == 200:
    pass
else:
    print(f"Failed to download file, {response.status_code}")
