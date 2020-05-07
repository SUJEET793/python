class Test :

    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def display(self):
        print("your name is :",self.name)
        print("your branch is :",self.branch)
        print()
test=Test("sujeet","CSE")
test .display()
test1=Test("Anjali","biology")
test1.display()

