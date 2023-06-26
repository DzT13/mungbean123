import base64
import requests

url = "https://proxy.yugogo.xyz/vmess/sub"
response = requests.get(url)

if response.status_code == 200:
    decoded_content = base64.b64decode(response.content)
    with open("umah.txt", "wb") as f:
        f.write(decoded_content)
        print("File saved!")
else:
    print("Error: Unable to fetch content from URL")
