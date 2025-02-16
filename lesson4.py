students = {
    "Jack": [True, False, True],
    "Emily": [False, False, False],
    "Henry": [True, True, True],
    "Jeffry": [False, False, True],
    "Jake": [False, False, False]
}

def show_menu():
    print("****** School Attendance System ******\n 1. Take Attendance \n 2. Calculate Attendance Percenatage For A Student\n 3. Notify Low Attendance\n 4. Exit Program\n")
    choice = int(input("Enter your choice: "))
    

def take_attendance(students: dict) -> dict:
    print("Taking Class Attendance Now...")
    for student, attendance_list in students.items():
        while True:
            attendance = str(input(f"Is {student} present? y/n: ")).lower()
            if attendance == "y":
                students[student].append(True)
                break
            elif attendance == "n":
                students[student].append(False)
                break
            else:
                print("Invalid Response, only y OR n. Try again!")
    print("Class attendance is taken.")
    return students

updated_students = take_attendance(students)
print(updated_students)

def attendance_percentage(student: str, students: dict) -> float:
    if student in students:
        attendance_list = students[student]
        num = attendance_list.count(True)
        denom = len(attendance_list)
        return (num/denom) * 100
    else:
        print(f"{student} not found.")
        return None

def notifyLowAttendance(student: str, attendance: float):
    if attendance is not None and attendance < 50:
        print(f"{student} has a low attendance! ({attendance}% attendance)")

studente = str(input("Which student would you like to check?: "))
value = attendance_percentage(studente, students)
if value is not None:
    print(f"{studente} attendance: {value}%")
    notifyLowAttendance(studente, value)

notifyLowAttendance("Jake")