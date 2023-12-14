class student:
    def __init__(self,name=None,id=0,department=None) :
        self.name = name
        self.id = id
        self.department =department
        self.Class = []
    
    def addclass(self,Class):
        self.Class.append(Class)

    def checkclass(self):
        return self.Class

if __name__ == '__main__' :
    joson = student("joson",1,"資工")
    joson.addclass("資料庫")
    joson.addclass("python")
    print(joson.checkclass())