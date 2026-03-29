students = []


def add_student():
    name = input("Enter name: ").strip()
    roll = input("Enter roll no: ").strip()
    marks_input = input("Enter marks: ").strip()

    if not name or not roll or not marks_input:
        print("All fields are required!\n")
        return

    roll = roll.upper()

    for s in students:
        if s["roll"].upper() == roll:
            print("A student with this roll number already exists!\n")
            return

    try:
        marks = float(marks_input)
    except ValueError:
        print("Marks must be a number!\n")
        return

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100!\n")
        return

    student = {"name": name, "roll": roll, "marks": marks}
    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found!\n")
    else:
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
        print()


def search_student():
    roll = input("Enter roll no to search: ").strip().upper()
    for s in students:
        if s["roll"].upper() == roll:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}\n")
            return
    print("Student not found!\n")


def delete_student():
    roll = input("Enter roll no to delete: ").strip().upper()
    for index, s in enumerate(students):
        if s["roll"].upper() == roll:
            del students[index]
            print("Deleted successfully!\n")
            return
    print("Student not found!\n")


def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    menu()
