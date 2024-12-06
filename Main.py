import Classes

def main():
    student1 = Classes.UndergraduateStudent("A", "ECE", 999999, False, True, False)
    student2 = Classes.GraduateStudent("B", "MECH", 123456, "ffffff")
    student3 = Classes.GraduateStudent("C", "BIO", 111111, "a")
    student4 = Classes.UndergraduateStudent("D", "EEE", 222222, True, True, False)
    coursea = Classes.Course("a", "ssssss", list())
    courseb = Classes.Course("b", "a", list())
    coursea.addstudent(student1)
    coursea.addstudent(student4)
    coursea.addstudent(student3)

    courseb.addstudent(student1)
    courseb.addstudent(student2)

    coursec = coursea + courseb

    print(coursec)

    print(coursea)

    print(student1.degree)

    print(student2.degree)
    student2.degree = "ECE"
    print(student2.degree)


if __name__ == "__main__":
    main()