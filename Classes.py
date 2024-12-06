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
        return f"The student {self.studentid} is {self.name} from {self.degree}."

    @property
    def degree(self):
        return self._degree
    
    @degree.setter
    def degree(self, degree):
        if degree not in ["ECE", "BIO", "MECH", "EEE"]:
            raise ValueError("Invalid degree input.")
        self._degree = degree

class Course:
    def __init__(self, coursename, coursecode, enrolledstudents, strenrolled):
        if not coursename:
            raise ValueError("The name of the course is invalid because it is empty.")
        if not coursecode or type(coursecode) is not str:
            raise ValueError("The course code is invalid.")
        if not enrolledstudents or type(enrolledstudents) is not list:
            raise ValueError("The list of enrolled students input is not valid.")
        self.coursename = coursename
        self.coursecode = coursecode
        self.enrolledstudents = enrolledstudents
        self.strenrolled = self.strenrolledstudents()
    def addstudent(self, student):
        self.enrolledstudents.append(student)
    
    def removestudent(self, student):
        self.enrolledstudents.remove(student)
    
    def strenrolledstudents(self):
        string = ""
        for i in self.enrolledstudents:
            string += str(i)
        return string


    def __str__(self):
        return f"The Course name is: {self.coursename} with code {self.coursecode} and the students enrolled are:\n{self.strenrolled}"

class GraduateStudent(Student):
    def __init__(self, name, degree, studentid, researchtopic):
        super().__init__(name, degree, studentid)
        if not researchtopic or type(researchtopic) is not str:
            raise ValueError("The research topic is invalid.")
        self.researchtopic = researchtopic
    
class UndergraduateStudent(Student):
    def __init__(self, name, degree, studentid, yearinindustry, foundation, repeater):
        super().__init__(name, degree, studentid)
        if not yearinindustry or type(yearinindustry) is not bool:
            raise ValueError("The value for whether the student is doing a degree in industry is invalid.")
        self.yearinindustry = yearinindustry
        if not foundation or type(foundation) is not bool:
            raise ValueError("The value for whether the student has done a foundation year is invalid.")
        self.foundation = foundation
        if not repeater or type(repeater) is not bool:
            raise ValueError("The value for whether the student is repeating the year is invalid.")
