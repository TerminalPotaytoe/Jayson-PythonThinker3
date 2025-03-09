students = {
    "Jack": [True, False, True],
    "Emily": [False, False, False],
    "Henry": [True, True, True],
    "Jeffry": [False, False, True],
    "Jake": [False, False, False]
}

def show_menu():
    print("****** School Attendance System ******\n 1. Take Attendance \n 2. Calculate Attendance Percentage For A Student\n 3. Notify Low Attendance\n 4. Exit Program\n")
    choice = int(input("Enter your choice: "))
    return choice

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

while True:
    choice = show_menu()

    if choice == 1:
        students = take_attendance(students)
    elif choice == 2:
        student = input("Which student would you like to check?: ")
        value = attendance_percentage(student, students)
        if value is not None:
            print(f"{student}'s attendance: {value}%")
    elif choice == 3:
        student = input("Which student would you like to check for low attendance?: ")
        value = attendance_percentage(student, students)
        if value is not None:
            notifyLowAttendance(student, value)
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")
