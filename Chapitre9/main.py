import requests

try:
    response = requests.get("https://hello-world.zdarkblackshadow.com")
    if response.status_code == 200:
        print(response.status_code)
    else:
        print(f"status code : {response.status_code}")
except(e):
    print(e)