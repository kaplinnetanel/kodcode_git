from fastapi import FastAPI
import logging 
import json


logging.basicConfig(level=logging.DEBUG,format="")
app = FastAPI()
loger = logging.getLogger(__name__)
@app.get("/454")
def retu():
    loger.info("good")
    return "good luq"
m =[122,343,65,"as"]
with open("file_name", "w",encoding= "utf-8") as file:
    json.dump(m,file)
#כדי לעלות את M לתוך התכון של הקובץ 

with open("file_name","r",encoding="utf-8") as file:
    name = json.load(file)
#כדי לקבל את הקובץ שנצמצה בתוך הגיסון הוא חוזר בתור מילון שאני יכול לרוץ עליו 

