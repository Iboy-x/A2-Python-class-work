# CONTAINMENT :  creating and using object of one class in another class 
# course : lessons, assessments 


class Lesson:
    def __init__(self, t, d, r):
        self.LessonTitle = t
        self.DurationMinutes = d
        self.RequiresLab = r

    def OutputLessonDetails(self):
        print(self.LessonTitle)
        print("Total time in minutes:", self.DurationMinutes)


class Assessment:
    def __init__(self, t, m):
        self.AssessmentTitle = t
        self.MaxMarks = m

    def OutputAssessmentDetails(self):
        print(self.AssessmentTitle)
        print("Maximum marks:", self.MaxMarks)


class Course:
    def __init__(self, t, m):
        self.CourseTitle = t
        self.MaxStudents = m
        self.CourseLessons = []
        self.CourseAssessment = None

    def AddLesson(self, t, d, r):
        self.CourseLessons.append(Lesson(t, d, r))

    def AddAssessment(self, t, m):
        self.CourseAssessment = Assessment(t, m)

    def OutputCourseDetails(self):
        print(self.CourseTitle)
        print("Max number:", self.MaxStudents)

        for lesson in self.CourseLessons:
            lesson.OutputLessonDetails()

        if self.CourseAssessment:
            print("Assessment")
            self.CourseAssessment.OutputAssessmentDetails()


myCourse = Course("Computer Science", 30)
myCourse.AddLesson("OOP", 300, True)
myCourse.AddLesson("Hardware", 200, False)
myCourse.AddLesson("AI", 100, False)
myCourse.AddAssessment("Final exam", 75)
myCourse.OutputCourseDetails()
