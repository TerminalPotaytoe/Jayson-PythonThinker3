answer_key = ["A", "B", "C", "D"]

studentAnswers = {
    "Jake": ["A", "B", "C", "D"],
    "WillyWanker": ["A", "A", "D", "A"],
    "MrBeast": ["A", "D", "C", "B"],
    "Jack": ["A", "C", "D", "B"]
}

def menu_system():
    while True:
        print("\nQuiz Grading System Menu")
        print("1. Grade all students")
        print("2. Calculate Class Average")
        print("3. Find Highest Scorer")
        print("4. Display All Results")
        print("5. Exit")
        
        option = input("Option: ")

        if option == "1":
            scores = grade_students(answer_key, studentAnswers)
            display_results(scores)
        elif option == "2":
            if not scores:
                print("Please choose option 1 to grade students first.")
            else:
                scores = grade_students(answer_key, studentAnswers)
                calculate_average(scores)
        elif option == "3":
            if not scores:
                print("Please choose option 1 to grade students first.")
            else:
                scores = grade_students(answer_key, studentAnswers)
                highest_scorer(scores)
        elif option == "4":
            if not scores:
                print("Please choose option 1 to grade students first.")
            else:
                scores = grade_students(answer_key, studentAnswers)
                display_results(scores)
        elif option == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

def grade_students(answer_key, student_answers):
    scores = {name: 0 for name in student_answers}

    for name, answers in student_answers.items():
        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                scores[name] += 1
    
    return scores

def display_results(quiz_scores):
    if not quiz_scores:
        print("Nothing to see here")
        return
    
    print("\nClass Results:")
    for name, score in quiz_scores.items():
        print(f"{name}: {score}")

def calculate_average(scores):
    if not scores:
        print("No students to calculate average.")
        return
    
    avg = sum(scores.values()) / len(scores)
    print(f"Average Score: {avg:.2f}")

def highest_scorer(scores):
    if not scores:
        print("No students to find highest scorer.")
        return

    max_score = max(scores.values())
    top_students = []

    for name, score in scores.items():
        if score == max_score:
            top_students.append(name)
    print("\nHighest Scorer(s):")
    for student in top_students:
        print(f"{student} with a score of {max_score}")

menu_system()
