from src.supermaklerAPI.Session import login
import requests
from os.path import exists

API_BASE_URL="https://pkosupermakler.pl/next/v1/"
JSESSIONID_COOKIE_FILE="jsessionid.cookie"

def _handle_cookie():
    if (exists(JSESSIONID_COOKIE_FILE)):
        with open(JSESSIONID_COOKIE_FILE,'r') as f:
            jsessionid=f.read()
    else:
        jsessionid = login()
        with open(JSESSIONID_COOKIE_FILE,'w') as f:
            f.write(jsessionid)
    return jsessionid

def test():
    jsessionid = _handle_cookie()
    cookies = {"JSESSIONID": jsessionid}

    headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'X-XSRF-Token': 'UcJjCY7A-eQsFuSbp4QDuRU7-466hSyptGjo',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://webflow.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'}

    TEST_URL=API_BASE_URL+"settings-srv/user-details"
    response = requests.get(f'{TEST_URL}', headers=headers, cookies=cookies)
    return response.json()

if __name__=="__main__":
    print(test())