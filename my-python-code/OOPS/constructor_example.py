class Employee():
    def __init__(self,name,eid,loc):
        self.name=name;
        self.eid=eid;
        self.loc=loc
    def eDetail(self):
         print("Hello :",self.name)
         print("Hello :",self.eid)
         print("Hello :",self.loc)
EE=Employee("sujeet",2,"kol")
EE.eDetail()
EE.__init__()