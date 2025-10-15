import requests

BASE_URL = "https://use1-omada-northbound.tplinkcloud.com/openapi"

def omada_login(username, password):
    # Step 1: Login
    login_res = requests.post(f"{BASE_URL}/authorize/login", json={
        "username": username,
        "password": password
    })
    session_id = login_res.json()["result"]["sessionId"]

    # Step 2: Get Authorization Code
    code_res = requests.get(f"{BASE_URL}/authorize/code", headers={
        "Cookie": f"JSESSIONID={session_id}"
    })
    auth_code = code_res.json()["result"]["code"]

    # Step 3: Get Access Token
    token_res = requests.post(f"{BASE_URL}/authorize/token", json={
        "code": auth_code,
        "grant_type": "authorization_code"
    })
    token = token_res.json()["result"]["access_token"]
    omadac_id = token_res.json()["result"]["omadacId"]

    return {"token": token, "omadac_id": omadac_id}

