class student :
    #初始化建構
    def __init__(self,school=None,department=None,grade=None,credit=None,GPA=None,school_address=None,Personal_mailing_address=None) :
        self.school,self.department,self.grade,self.credit,self.GPA,self.school_address,self.Personal_mailing_address=school,department,grade,credit,GPA,school_address,Personal_mailing_address
    #儲存學校名稱
    def set_school_name(self,school):
        self.school = school
    #儲存科系名稱
    def set_department_name(self,department):
        self.department =department
    #儲存年級
    def set_grade(self,grade):
        self.grade = grade
    #儲存學分
    def set_credit(self,credit):
        self.credit =credit
    #儲存GPA
    def set_GPA(self,GPA):
        self.GPA = GPA
    #儲存學校地址
    def set_school_address(self,school_address):
        self.school_address =school_address
    #儲存個人通訊地址
    def set_Personal_mailing_address(self,Personal_mailing_address):
        self.Personal_mailing_address =Personal_mailing_address
    #取得學校名稱
    def get_school_name(self,school):
        return self.school
    #取得科系名稱
    def get_department_name(self,department):
        return self.department
    #取得年級
    def get_grade(self,grade):
        return self.grade
    #取得學分
    def get_credit(self,credit):
        return self.credit
    #取得GPA
    def get_GPA(self,GPA):
        return self.GPA
    #取得學校地址
    def get_school_address(self,school_address):
        return self.school_address
    #取得個人通訊地址
    def get_Personal_mailing_address(self,Personal_mailing_address):
        return self.Personal_mailing_address
    #列印全部
    def print_ALL(self):
        print("school:",self.school,"department:",self.department,"grade:",self.grade,"credit:",self.credit,"GPA:",self.GPA,"school_address:",self.school_address,"Personal_mailing_address:",self.Personal_mailing_address)

def main():
    Allen = student("STUST","infomation_engineer",4,127,20)
    Allen.set_school_address("A")
    Allen.print_ALL()

if __name__==main():
    main()