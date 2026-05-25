

#תרגיל 2 
student ="Dan,85,90,78\nMOMO,92,88,95\nYoni,70,65,80\nAvi,100,95,98\nSara,60,72,68\n"
filename = "grades.txt"
def create_grades_file(filename , data):
    with open (filename,"w",encoding="UTF-8")as f:
            f.writelines(data)

def calculate_averages(filename):
      with open(filename,"r",encoding="UTF-8") as f:
            average ={}
            for line in f :
                line = line.strip()
                parts = line.split(",")
                name = parts[0]
                sum_a = 0
                count = 0 
                for char in parts[1:]:
                   sum_a += int(char)
                   count += 1
                if count > 0 :
                    average[name] = sum_a / count
            return average    

def calculate_averages(filename):
    averages = {}
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            name = parts[0].strip()
            grades = [int(grade.strip()) for grade in parts[1:]]
            if grades:
                averages[name] = sum(grades) / len(grades)      
    return averages    

def save_results(averages, output_filename):

    with open(output_filename ,"w", encoding = "UTF-8") as f:
        f.write("=== Student Results ===\n") 
        i = 1
        for name, avg in averages.items():
            f.write(f"{i} = {name} :{avg}\n")
            i += 1

create_grades_file(filename, student)
averages_dict = calculate_averages(filename)
save_results(averages_dict, "neta.py")