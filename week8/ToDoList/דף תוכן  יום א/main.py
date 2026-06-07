# from fastapi import FastAPI
# from datetime import datetime

# app = FastAPI()
# #1

# @app.get("/ping")
# def get_ping():
#     return  {"status": "pong"}

# @app.get("/greet/{name}")
# def greet(name : str):
#     return {f"message": "Hello, {name}!"} 

# #2
# @app.get("/")
# def get_root():
#     return {"service": "my-api", "version": "1.0"}

# @app.get("/users/admin")
# def get_admin():
#     return {"role": "admin", "access": "full"}

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {
#         "user_id": user_id, 
#         "name": "John Doe", 
#         "email": "john@example.com"
#     }

# #3
# @app.get("/calc/{a}/{op}/{b}")
# def calc(a: int, op: str, b: int):
#     if op == "add":
#         result = a + b
#     elif op == "sub":
#         result = a - b
#     elif op == "mul":
#         result = a * b
#     elif op == "div":
#         if b == 0:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST, 
#                 detail="Cannot divide by zero ")
#         result = a / b
#     else:
#         raise HTTPException
#     return {"operation" : op , "result" : result}

# @app.get("/status")
# def status():
#     return {"current_time": str(datetime.now())}