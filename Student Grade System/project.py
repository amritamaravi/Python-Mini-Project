student_grades = {}

#Add a new student and their grade
def add_student(name, grade):
    student_grades[name] = grade
    #[sagar]=100
    print(f"Added {name} with a {grade}")
    #added sagar with a 100

#Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        #Sagar=200
        print(f"{name} with marks are updated {grade}")
    
    else:
        print(f"{name} not found.")
        #student sagar not found
#Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        #delete sagar
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} not found.")   

#View all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}:{grade}")
    else:
        print("No students found/added.")


def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name to update: ")
            grade = int(input("Enter new grade: "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name to delete: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Exiting the Student Grade System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()