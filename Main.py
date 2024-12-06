import Classes

def main():
    student1 = Classes.UndergraduateStudent("A", "ECE", 999999, False, True, False)
    student2 = Classes.GraduateStudent("B", "MECH", 123456, "ffffff")
    student3 = Classes.GraduateStudent("C", "BIO", 111111, "a")
    student4 = Classes.UndergraduateStudent("D", "EEE", 222222, True, True, False)
    coursea = Classes.Course("a", "ssssss", [])

    coursea.addstudent(student1)
    coursea.addstudent(student4)

    print(coursea)

    print(student1.degree())

    student2.degree("ECE")

if __name__ == "__main__":
    main()