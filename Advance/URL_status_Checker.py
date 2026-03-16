import requests

urls = [
    "https://google.com",
    "https://github.com",
    "https://example.com"
]

for url in urls:
    try:
        r = requests.get(url)
        print(url, "Status:", r.status_code)
    except:
        print(url, "Failed")
