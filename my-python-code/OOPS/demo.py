# create a class name Student and crete object to it ,call the methid talk () to display the student detail
class Student :
    """This is the student class

    this class is creted by sujeet suman
    on the date of 07-05-2020
    """
    def __init__(self,name,s_class,roll):
        self.name=name
        self.s_class=s_class
        self.roll=roll
    # this is talk method  used for the display the data
    def talk(self):
        print(self.name)
        print(self.s_class)
        print(self.roll)

print(Student.__doc__) #This is the student class
    #this class is creted by sujeet suman
    #on the date of 07-05-2020
# here Stuedent is the refrence variable
student=Student(input("Enter the name"),input(("enter the class ")),int(input("enter the roll")))




