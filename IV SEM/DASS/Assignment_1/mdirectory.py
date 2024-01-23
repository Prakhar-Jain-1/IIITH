import csv
import sys
from prettytable import PrettyTable
import subprocess as sp

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
        input("Press Enter to continue...")

    
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
        search_attributes = input("Enter the attributes to search for (e.g., FirstName, Semester, Course): ").strip().lower().split(',')

        invalid_attributes = [attr for attr in search_attributes if attr not in ["firstname", "lastname", "rollno", "semester", "coursename", "examtype", ""]]

        if invalid_attributes:
            print(f"Invalid search attribute(s): {', '.join(invalid_attributes)}")
            return

        attr = {"firstname":None, "lastname":None, "rollno":None, "semester":None, "coursename":None, "examtype":None}
        for searchA in search_attributes:
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
                        if attr["examtype"] != None and attr["examtype"] != exam_type:
                            continue
                        row_data = list(stdDetails) + [semester, course, exam_type, marks[0], marks[1]]
                        self.table.add_row(row_data)
        print(self.table)
        input("Press Enter to continue...")
        pass
    
    def loadFromCSV(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    stdDetails = tuple(row[:3])
                    semester, course, Et, TM, SM = row[3:]
                    if stdDetails not in self.entries:
                        self.entries[stdDetails] = {}
                    entry = self.entries[stdDetails]
                    if semester not in entry:
                        entry[semester] = {}
                    entry = entry[semester]
                    if course not in entry:
                        entry[course] = {}
                    entry = entry[course]
                    if Et not in entry:
                        entry[Et] = (int(TM), int(SM))
                    else:
                        print("Entry already there")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")

    def saveToCSV(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for stdDetails, semesters in self.entries.items():
                for semester, courses in semesters.items():
                    for course, exams in courses.items():
                        for exam_type, marks in exams.items():
                            writer.writerow(list(stdDetails) + [semester, course, exam_type, marks[0], marks[1]])

def main():
    MM = MarksManager()

    # Load entries from a CSV file (if the file exists)
    MarksCsv = "marks.csv"
    if len(sys.argv) > 1:
        MarksCsv = sys.argv[0]
    # else:
        # MarksCsv = 
    # print(MarksCsv)
    MM.loadFromCSV(MarksCsv)
    # print("df") 

    while True:
        tmp = sp.call('clear', shell=True)
        print("\nOptions:")
        print("1. Add Entry")
        print("2. Display Table")
        print("3. Remove Entry")
        print("4. Update Entry")
        print("5. Search Entry")
        print("6. Save to File")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")
        tmp = sp.call('clear', shell=True)

        if choice == "1":
            MM.addEntry()
        elif choice == "2":
            MM.displayTable()
        elif choice == "3":
            MM.removeEntry()
        elif choice == "4":
            MM.updateEntry()
        elif choice == "5":
            MM.searchEntry()
        elif choice == "6":
            # Save entries to a CSV file before quitting
            MM.saveToCSV(MarksCsv)
        elif choice == '7':
            MM.saveToCSV(MarksCsv)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

