import requests
def test_ok_text_message(self):
    url = "https://test3.perksdev.com/api/v1/test"

payload={}
headers = {
  'Auth  orization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6InBzc3RAdHNzdC5jb20iLCJuYW1laWQiOiIzMzk4OTkyYS1hOWNkLTQyMWQtOGFhOS1hNjVkYjlmNzllOTQiLCJlbWFpbCI6InBzc3RAdHNzdC5jb20iLCJUZW5hbnRJZCI6IjkiLCJuYmYiOjE2MzQ3MjE0MDgsImV4cCI6MTYzNzMxMzQwOCwiaWF0IjoxNjM0NzIxNDA4LCJpc3MiOiJQRVJLUyBtb2JpbGUgZGV2In0.XDFfwMzw31j0P2xwv6Bkz-043JXiNYxEF1wcf80RqUQ'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
assert[response] == "test"