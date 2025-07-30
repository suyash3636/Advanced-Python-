import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code) 
# print(response.headers["Content-Type"])  
# print(response.json())      


# payload = {'title': 'foo', 'body': 'bar', 'userId': 99}
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

# print(response.status_code)   
# print(response.json())        


# params = {'q': 'python'}
# r = requests.get("https://www.google.com/search", params=params)
# print(r.url)  



try:
    r = requests.get("https://httpbin.org/status/404")
    r.raise_for_status()  # Raises HTTPError for 4xx/5xx codes
except requests.exceptions.HTTPError as e:
    print("Error:", e)
