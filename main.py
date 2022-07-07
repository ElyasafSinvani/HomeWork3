# Name:Elyasaf Sinvani ID:318551728
class Course:
    def __init__(self, namecourse):
        """
        The builder of a "course" gets the name of a course that builds a new object of the course type whose name is the same as the one we got in the builder, and initializes the grade in the course to be 101
        :param namecourse: the name of the course
        """
        self.nameC = namecourse
        self.Grade = 101

    def setGrade(self, grade):
        """
        The method accepts the current object "Course", and tells, if the number we got between 0 and 100, the method will change the current course score to the number we got, if not the course score will not change
        :param grade: A number that describes the score
        :return:There is no return value
        """
        if grade > -1 and grade < 101:
            self.Grade = grade

    def __add__(self, other):
        """
        Connection operator of a course object, receives the current course and another parameter, if the additional parameter is also of course type A combination of the scores of the two course type objects will be returned, if the parameter is a number, a connection of the current course score will be returned with the number we received as a parameter
        :param other: Course type or number type parameter
        :return:if the additional parameter is also of course type A combination of the scores of the two course type objects will be returned, if the parameter is a number, a connection of the current course score will be returned with the number we received as a parameter
        """
        if (type(other) == type(self)):
            return self.Grade + other.Grade
        elif type(other) == int:
            return self.Grade + other

    def __str__(self):
        """
        A method that returns a string of the current course name and its grade
        :return: a string of the current course name and its grade
        """
        return f'course ({self.nameC})=garde {self.Grade}'

    def __repr__(self):
        """
        A method that returns a string of the object type
        :return:a string of the object type
        """
        return 'Course()'


class Student:
    def __init__(self, namestudent, id):
        """
        The builder of the "Student" department, which receives as parameters the student's name, and ID card, the builder creates a new student type object whose name is the name we received as a parameter, and the ID card is the ID card we received as a parameter, and initializes the student's course list to a blank list
        :param namestudent: Student Name
        :param id: Student ID
        """
        self.__ID = id
        self.name = namestudent
        self.course = []

    def getID(self):
        """
        A method that accepts the current "student" object, and returns its ID
        :return: The current student ID
        """
        return self.__ID

    def addCourse(self, nameC, grade):
        """
        Method that receives as parameters a course name and course number in the course, the method will check if the course grade is between 0 and 100, then if the course already exists for the student the method will replace the grade in the course for the grade we received, otherwise the method will add a new course And the score is the score we got as a parameter, if the score we got is not between 0 and 100 we will not change anything
        :param nameC: the name of the course
        :param grade: Course grade
        :return: There is no return value
        """
        if grade > -1 and grade < 101:
            if len(list(filter(lambda x: x.nameC == nameC, self.course))) == 0:
                C = Course(nameC)
                C.setGrade(grade)
                self.course += [C]
            else:
                list(filter(lambda x: x.nameC == nameC, self.course))[0].setGrade(grade)

    def __add__(self, other):
        """
        Student object connection operator, accepts the current object and another parameter, if the parameter is also of the student type a connection list of the two students' course list will be returned, otherwise if the parameter is a list of courses the student's list list will be returned with the list of courses we received as a parameter
        :param other:A student-type object or a list-type object of courses
        :return:if the parameter is also of the student type a connection list of the two students' course list will be returned, otherwise if the parameter is a list of courses the student's list list will be returned with the list of courses we received as a parameter
        """
        if (type(other) == type(self)):
            return self.course + other.course
        else:
            return self.course + other

    def __str__(self):
        """
        A method that returns a string of the student's name, ID card and all his courses and grades
        :return:a string of the student's name, ID card and all his courses and grades
        """
        return f'Stutent : {self.name} {self.__ID} {list(map(lambda x: str(x), self.course))}'

    def __repr__(self):
        """
        A method that returns a string of the object type
        :return:a string of the object type
        """
        return "Student()"


def Average_student(S):
    """
    The function accepts as a student object type parameter and returns the average student in all the courses he studied
    :param S:"Student" object
    :return:The average grade of the student in all the courses he studied
    """
    from functools import reduce
    if S.course == []:
        return "There are no courses available for this student"
    return reduce(lambda x, y: y + x, S.course) / len(S.course)


def Average_course(arrS, namec):
    """
    The function receives as parameters a set of students and the name of a course, the function will go over all the courses of the students in the set, and return an average of the course we received as a parameter
    :param arrS: Array of "Student" objects
    :param namec: Name of a particular course
    :return: Average of the course we received as a parameter, on all students in the set
    """

    def this_course(C):
        """
        An internal function that receives a course-type object, and returns true if the name of the course we received as a parameter in the external function is the name of the course we received as a parameter, otherwise returns false
        :param C:Course-type object
        :return:True if the name of the course we received as an object in the internal function is the same as the name we received in the external function, otherwise returns false
        """
        if C.nameC == namec:
            return True
        return False

    from functools import reduce
    v = reduce(lambda x, y: y + x, arrS)
    if len(arrS) == 1:
        v = arrS[0].course
    if len(list(filter(this_course, v))) == 1:
        return list(filter(this_course, v))[0].Grade
    elif len(list(filter(this_course, v))) == 0:
        return "The course does not exist for students"
    return reduce(lambda a, b: b + a, list(filter(this_course, v))) / len(list(filter(this_course, v)))


nameFile = input("Please enter a file name :\n")
try:
    file = open(nameFile, 'r')
except FileNotFoundError:
    print("[Errno 2] No such file or directory Solution")
studentArr = []
for line in file:
    # Read each line in the file, and insert the information into the "Student" object
    L = str(str(line).replace(";", "\t")).split("\t")
    S = Student(L[0], L[1])
    L.remove(L[0])
    L.remove(L[0])
    if L[0] != '\n' and L[0] != "":
        for l in L:
            c = str(l).split("#")
            S.addCourse(c[0], int(c[1].replace("\n", "")))
    studentArr += [S]
file.close()
choice = 0
while choice != 4:
    while True:
        # Input integrity check
        print(
            "1 - Calculating the average of a particular student\n2 - Calculating the average in a particular course\n3 - Average of all students\n4 - Exit the program")
        choice = input("Please enter your choice :\n")
        try:
            choice = int(choice)
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")

    if choice == 1:
        # Absorption of the student's name, calculation of the average and printing of the student's ID number and his average
        name_stu = input("Please enter the name of the student :\n")
        t = list(filter(lambda s: s.name == name_stu,
                        studentArr))  # A list in which the student is with the name entered by the user
        if len(t) == 0:
            print("There is no student with this name, please try again ...\n")
        else:
            print(t[0].getID(), Average_student(t[0]))
    elif choice == 2:
        # Absorption of the course name, calculation of the course average for all students whose course is on the course list, and printing of the course name and its average
        name_cou = input("Please enter the name of the course :\n")
        print(name_cou, Average_course(studentArr, name_cou))
    elif choice == 3:

        nameFile2 = input("Please enter the name file :\n")
        with open(nameFile2, 'w') as f:
            w = list(map(lambda x: str(x.getID() + " " + str(Average_student(x))),
                         studentArr))  # A list in which each organ is a string with its student ID and average
            f.write(str(w).replace("[", "").replace("]", "").replace(", ", "\n").replace("'", ""))
        print("Writing the information to the file was successful!!\n")
    elif choice == 4:
        print('Have a nice day, goodbye :)')
    elif choice > 4 or choice < 1:
        print('Invalid input, please try again ...')
