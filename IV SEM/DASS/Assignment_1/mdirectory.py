import csv
from prettytable import PrettyTable

class MarksManager:
    def __init__(self) -> None:
        self.entries = {}
        # self.updated = False
        self.table = PrettyTable()
        self.table.field_names = ["First Name", "Last Name", "Roll Number", "Course Name","Semester","Exam Type","Total Marks","Scored Marks"]
        pass
    def addEntry(self):
        
        stdDetails = input("Student Details(FirstName LastName RollNo): ").split()
        stdDetails = tuple(stdDetails)
        
        if stdDetails not in self.entries:
            self.entries[stdDetails] = {}
        entry = self.entries[stdDetails]
        
        semester = str(input("Semester: "))
        
        if(semester not in entry):
            entry[semester] = {}
        entry = entry[semester] 
        
        course = (str(input("Course Name: ")))

        if course not in entry:
            entry[course] = {}
        entry = entry[course]

        Et = (str(input("Exam Type: ")))
        TM = int(input("Total Marks: "))
        SM = int(input("Scored Marks: "))
        
        if Et not in entry:
            entry[Et] = (TM,SM)
        else:
            print("Entry already there")

        # print(f"{stdDetails}:{self.entries[stdDetails]}")

        pass

    def displayTable(self):
        self.table.clear_rows()
        for stdDetails, semesters in self.entries.items():
            for semester, courses in semesters.items():
                for course, exams in courses.items():
                    for exam_type, marks in exams.items():
                        row_data = list(stdDetails) + [semester, course, exam_type, marks[0], marks[1]]
                        self.table.add_row(row_data)
        print(self.table)

    
    def removeEntry(self):
        stdDetails = input("Student Details(FirstName LastName RollNo): ").split()
        stdDetails = tuple(stdDetails)

        semester = str(input("Semester: "))
        course = str(input("Course Name: "))
        Et = str(input("Exam Type: "))

        if stdDetails in self.entries and semester in self.entries[stdDetails] and course in self.entries[stdDetails][semester] and Et in self.entries[stdDetails][semester][course]:
            del self.entries[stdDetails][semester][course][Et]
            print("Entry removed successfully.")
        else:
            print("Entry not found.")
    
    def updateEntry(self):
        stdDetails = input("Student Details(FirstName LastName RollNo): ").split()
        stdDetails = tuple(stdDetails)

        semester = str(input("Semester: "))
        course = str(input("Course Name: "))
        Et = str(input("Exam Type: "))

        if stdDetails in self.entries and semester in self.entries[stdDetails] and course in self.entries[stdDetails][semester] and Et in self.entries[stdDetails][semester][course]:
            TM = int(input("New Total Marks: "))
            SM = int(input("New Scored Marks: "))
            self.entries[stdDetails][semester][course][Et] = (TM, SM)
            print("Entry updated successfully.")
        else:
            print("Entry not found.")

    def searchEntry(self):
        search_attribute = input("Enter the attribute to search for (e.g., FirstName, Semester, Course): ").strip().lower()

        if search_attribute not in ["firstname", "lastname", "rollno", "semester", "coursename", "examtype"]:
            print("Invalid search attribute.")
            return
        attr = {"firstname":None, "lastname":None, "rollno":None, "semester":None, "coursename":None, "examtype":None}
        for searchA in search_attribute:
            attr[searchA] = input(f"Enter {searchA}: ")
        
        self.table.clear_rows()
        for stdDetails, semesters in self.entries.items():
            if (attr["firstname"] != None and stdDetails[0] != attr["firstname"]) or (attr["lastname"] != None and stdDetails[1] != attr["lastname"]) or (attr["rollno"] != None and stdDetails[2] != attr["rollno"]) :
                continue
            for semester, courses in semesters.items():
                if attr["semester"] != None and attr["semester"] != semester:
                    continue
                for course, exams in courses.items():
                    if attr["coursename"] != None and attr["coursename"] != course:
                        continue
                    for exam_type, marks in exams.items():
                        if attr["eaxmtype"] != None and attr["eaxmtype"] != exam_type:
                            continue
                        row_data = list(stdDetails) + [semester, course, exam_type, marks[0], marks[1]]
                        self.table.add_row(row_data)
        print(self.table)
        pass
    

MM = MarksManager()
MM.addEntry()

MM.displayTable()
# MM.removeEntry()
# MM.displayTable()
