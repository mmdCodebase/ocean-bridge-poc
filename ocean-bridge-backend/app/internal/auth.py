from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader


api_key_header = APIKeyHeader(name="Authorization")

# Validate token here
def validate_token(apiKey: str = Security(api_key_header)):
    if 1 == 0:
        raise HTTPException(status_code=403, detail="Invalid API_KEY")
    else :
        return True

def parse_cookies(cookie_string):
    cookies = {}
    for cookie in cookie_string.split(';'):
        try:
            key, value = cookie.split('=', 1)
            if key == '.ASPXAUTH' or key == 'ASP.NET_SessionId':
                cookies[key.strip()] = value.strip()
        except Exception as e:
            print(e)
            pass
    return cookies
