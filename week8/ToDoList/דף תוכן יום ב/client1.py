# import requests

# # response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# # if response.status_code == 200 :
#     # user = response.json()
#     # print(user)
#     # print({"Name":user["name"] ,"Email": user["email"] , "City": user["address"]["city"]})

#     # response = requests.get("https://jsonplaceholder.typicode.com/posts")
#     # posts = response.json()
#     # print(len(posts))

# response= requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
# for post in response.json():
#     print(post["title"])

#תרגיל 2
# import requests

# def safe_get(url):
#     try:
#         response = requests.get(url) 
#         if response.status_code == 200:
#             return response.json()
        
#         elif response.status_code == 404:  
#             return None  

#         else:
#             raise Exception(f"Request failed with status code: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         raise Exception(e) 
    
#תרגיל 3 

# from fastapi import FastAPI

# p = FastAPI()
# @p.get("/greet")
# def greet(name = "world"):
#     return {f"message:{name}!"}

#תרגיל 4 
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
post = response.json()
  

users = requests.get("https://jsonplaceholder.typicode.com/users?userId=2")
users = users.json()


for p in post:
    userId = p["userId"]
    for user in users:
        if user["id"] == userId:
            p["user_name"] = user["name"]

output = []
 
for p in post:
    print(f"post title {p["title"]} by {p["user_name"]}")
    