#Mini Project
'''
Create a Dynamic Leave Application Generator --> Name,Class,Section,School,ClassTeacher name,date,subject,date of leave,reason
'''








print("Leave Application Generator")
name=str(input("Enter the name of the Student: "))
classs=str(input("Enter the class: "))
sect =str(input("Enter the Section: "))
teacher=str(input("Enter the Teacher name: "))
date_=str(input("Enter the Date: "))
subject=str(input("Enter the subject: "))
leave=str(input("Enter the reason for leave: "))
date__=str(input("Enter the Date: "))

final = f'''
Subject: {subject}
Respected {teacher}  My self {name} from the following {classs} and section {sect} would request you to grant my leave due to {leave} on the following date
{date_} till {date__}. Please grant my leave and understand my situation.
Your Respectful
-Kingslly RA
'''

print(final)