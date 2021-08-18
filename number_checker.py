import requests, json

def check(phone):
    url = f"https://api.chat-api.com/instance291044/checkPhone?phone={phone}&token=kewfw8xbviafv0qh"

    headers = dict()
    headers["Content-Type"] = "application/json"

    resp = requests.get(url, headers=headers).json()
    return resp

if __name__ == "__main__":
    print(check(919031738599))
