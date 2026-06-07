from  fastapi import FastAPI,HTTPException
#1
a = FastAPI()

@a.get("/numbers/{n}")
def number(n : int):
    if  n < 0:
        raise HTTPException (status_code= 400 , detail= "Number must be non-negative")
    return {"value": n}

#2
students = {"101": "Moshe", "102": "Yosef"}

@a.get("/students/{student_id}")
def student_by_id(student_id : int):
    if student_id not in students:
        raise HTTPException (status_code= 404,detail="Student not found")
    return {"name":students[setudent_id]}

#3
@a.post("/students/{student_id}",status_code= 201)
def student_post_id(student_id : int):
    if student_id  in students:
        raise HTTPException(status_code= 409 )
    students[student_id] = student_info.dict()    

