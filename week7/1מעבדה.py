import os 
# #חלק א 



# def creates_file():
#     with open("diary.txt " ,"w",encoding= "utf-8") as f :
#         f.writelines("היה יום  עמוס פרויקט \n  למדתי עעל FILE HANDING בPYTHON \n השלמתי את התרגיל הראשון \n")
#         try:
#             if  os.path.exists("iary.txt"):
#                 print("הקובץ נוצר בהצלחה ")
#         except NameError as  f:
#             print(f)
# creates_file()  

# def reed_file():
#     with open("diary.txt ","r", encoding="utf8") as f:
#         for r in f:
#             print(r.strip())

# reed_file()
# #חלק ב

# data = "יום נפלא - סיימתי צתרגיל 1 \n"

# def add_entry(filename, date): 
#     with open(filename,"a",encoding="UTF-8") as f:
#         f.write(date)


# add_entry("diary.txt ",data)  

# #חק ג 

# def search_diary(filename, keyword): 
#     with open(filename,"r",encoding="UTF-8") as file  :
#         for line in file:
#             if keyword in line:
#                 print(line)

# search_diary("diary.txt ","ע")
#  #בונוס 
# def creates_file():
#     try:
#         with open("dry.txt ", "r", encoding="utf-8") as f:
#             תוכן = f.read()
#             print(תוכן)

#     except FileNotFoundError:
#         print(
#              "אופס! השגיאה נתפסה בהצלחה: הקובץ המבוקש לא נמצא בתיקייה."
#         )
# creates_file()