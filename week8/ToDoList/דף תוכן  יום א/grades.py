from fastapi import FastAPI

grades = { "1": {"name": "Moshe", "grade": 88}, 
          "2": {"name": "Yaakov", "grade": 75}, 
          "3": {"name": "David", "grade": 92}, }

ap = FastAPI()

@ap.get("/student")
def student():
    return grades

@ap.get("/students/{student_id}")
def get_student_by_id(student_id: str):  
    if student_id in grades:
        return grades[student_id] 
    return {"error": "Student not found"}

@ap.get("/students/top")
def top_greed_student():
    max_greed = 0
    name_student = ""
    for student_id  in grades:
        student_data = grades[student_id]
        if student_data["grade"] > max_grade:
            max_grade = student_data["grade"]
            name_student = student_data["name"]
    return f"max top greed {name_student} is a {max_greed}"         
         
@ap.get("/students/average")
def get_class_average():
    total_grades = 0
    for student_id in grades:
        total_grades += grades[student_id]["grade"]
    average = total_grades / len(grades)
    return {"class_average": average}        

@ap.get("/students/count")
def get_students_count():
    total = len(grades)
    return {"total_students": total}