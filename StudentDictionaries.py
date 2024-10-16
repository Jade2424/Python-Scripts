def add_grade():
    """Adds a new grade for a student."""
    student_name = input("Enter student's name: ")
    subject = input("Enter subject: ")
    grade = float(input("Enter grade (0-100): "))
    grades.setdefault(student_name, {})[subject] = grade
    print(f"Grade for {student_name} in {subject} added successfully!")
 
def view_grades():
    """Displays all grades for all students."""
    if not grades:
        print("No grades entered yet.")
        return
    for student, subjects in grades.items():
        print(f"\n{student}: {', '.join(f'{subj}: {grade}' for subj, grade in subjects.items())}")
 
def display_students():
    """Displays all student names."""
    if grades:
        print("Students:", ', '.join(grades.keys()))
    else:
        print("No students found.")
 
def calculate_average():
    """Calculates and displays the average grade for a student."""
    student_name = input("Enter student's name: ")
    if student_name in grades:
        avg = sum(grades[student_name].values()) / len(grades[student_name])
        print(f"{student_name}'s average grade is: {avg:.2f}")
    else:
        print(f"No grades found for {student_name}.")
 
# Initialize grades with data Provided
grades = {
    "Matome": {"Java Programming": 85, "Systems Software": 90, "Web Development": 78, "Networks": 88, "Business Analysis": 92, "DevOps": 75},
    "Bongani": {"Java Programming": 75, "Systems Software": 80, "Web Development": 85, "Networks": 90, "Business Analysis": 70, "DevOps": 68},
    "Thato": {"Java Programming": 92, "Systems Software": 88, "Web Development": 95, "Networks": 91, "Business Analysis": 85, "DevOps": 87},
    "Teddy": {"Java Programming": 80, "Systems Software": 75, "Web Development": 70, "Networks": 78, "Business Analysis": 82, "DevOps": 90},
    "Cecilia": {"Java Programming": 88, "Systems Software": 92, "Web Development": 84, "Networks": 86, "Business Analysis": 90, "DevOps": 80}
}
 
# Main program loop
while True:
    choice = input("\n1. Add Grade\n2. View Grades and Subjects\n3. Display All Students\n4. Calculate Average\n5. Exit\nEnter your choice: ")
    if choice == '1': add_grade()
    elif choice == '2': view_grades()
    elif choice == '3': display_students()
    elif choice == '4': calculate_average()
    elif choice == '5': break
    else: print("Invalid choice.")