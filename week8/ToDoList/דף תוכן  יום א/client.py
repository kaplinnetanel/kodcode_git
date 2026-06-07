import requests    
updated = {"id": 1, "title": "New Title", "body": "New content", "userId": 1}
r = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated)
print(r.status_code)   

print(r.text) 


r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(r.status_code) 
print(r.json())