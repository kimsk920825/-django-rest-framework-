import requests   # pip install requestsimport requests

JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2l"
    "kIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNjQxOTcwNTY0LCJlbWFpbCI6IiJ9"
    ".J2y-MCvdd2pX37wkTOuG1O0ocKhHmqIDiMHomW338mA"
        )
headers = {
    # 'Authorization': f'Token {TOKEN}',  # Token 인증
    'Authorization': f'JWT {JWT_TOKEN}',  # JWT 인증
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())