import json

students = {1:{"firstname":"Erzhan", "lastname":"Muratov","age":"23", "sex":"Male", "department":"Python"},
            2:{"firstname":"Agahan", "lastname":"Imamidinov","age":"21", "sex":"Male", "department":"Python"},
            3:{"firstname":"Feruza", "lastname":"Asanova","age":"22", "sex":"Female", "department":"Head of Neobis"},
            4:{"firstname":"Medet", "lastname":"Musaev","age":"23", "sex":"Male", "department":"Python Mentor"},
            5:{"firstname":"Turan", "Kulig":"Muratov","age":"23", "sex":"Male", "department":"Python"}}

with open("students_data.json", "w") as file:
     json.dump(students, file, indent=4)
