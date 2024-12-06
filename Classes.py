class Student:
    def __init__(self, name, degree, studentid):
        if not name:
            raise ValueError("The name is invalid because it is empty.")
        if degree not in ["ECE", "BIO", "MECH", "EEE"]:
            raise ValueError("Invalid degree input.")
        if len(str(studentid)) != 6 or type(studentid) is not int:
            raise ValueError("The student ID entered is invalid.")
        self.name = name
        self.degree = degree
        self.studentid = studentid
    
    def __str__(self):
        return f"{self.studentid}:{self.name} from {self.degree}\n"

    @property
    def degree(self):
        return self._degree
    
    @degree.setter
    def degree(self, degree):
        if degree not in ["ECE", "BIO", "MECH", "EEE"]:
            raise ValueError("Invalid degree input.")
        self._degree = degree

class Course:
    def __init__(self, coursename, coursecode, enrolledstudents):
        if not coursename:
            raise ValueError("The name of the course is invalid because it is empty.")
        if not coursecode or type(coursecode) is not str:
            raise ValueError("The course code is invalid.")
        if type(enrolledstudents) is not list:
            raise ValueError("The list of enrolled students input is not valid.")
        self.coursename = coursename
        self.coursecode = coursecode
        self.enrolledstudents = enrolledstudents
        self.strenrolled = self.strenrolledstudents()
    def addstudent(self, student):
        if student not in self.enrolledstudents:
            self.enrolledstudents.append(student)
            self.strenrolled = self.strenrolledstudents()
        else:
            raise ValueError("That student is already in the list of enrolled students.")
    
    def removestudent(self, student):
        if student in self.enrolledstudents:
            self.enrolledstudents.remove(student)
            self.strenrolled = self.strenrolledstudents()
        else:
            raise ValueError("That student is not in the list of enrolled students.")
    def strenrolledstudents(self):
        string = ""
        for i in self.enrolledstudents:
            string += str(i)
        return string


    def __str__(self):
        return f"The Course name is: {self.coursename} with code {self.coursecode} and the students enrolled are:\n{self.strenrolled}"

    def __add__(self, other):
        listofall = []
        for i in other.enrolledstudents:
            if i not in self.enrolledstudents:
                listofall.append(i)
        return Course(self.coursename, self.coursecode, listofall)

class GraduateStudent(Student):
    def __init__(self, name, degree, studentid, researchtopic):
        super().__init__(name, degree, studentid)
        if not researchtopic or type(researchtopic) is not str:
            raise ValueError("The research topic is invalid.")
        self.researchtopic = researchtopic
    
class UndergraduateStudent(Student):
    def __init__(self, name, degree, studentid, yearinindustry, foundation, repeater):
        super().__init__(name, degree, studentid)
        if type(yearinindustry) is not bool:
            raise ValueError("The value for whether the student is doing a degree in industry is invalid.")
        self.yearinindustry = yearinindustry
        if type(foundation) is not bool:
            raise ValueError("The value for whether the student has done a foundation year is invalid.")
        self.foundation = foundation
        if type(repeater) is not bool:
            raise ValueError("The value for whether the student is repeating the year is invalid.")
