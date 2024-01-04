#建立員工類別
class employer :
    #預設建構輸入員工參數
    def __init__(self,Name,Seniority,working_hours) :
        self.name=Name
        self.seniority =Seniority
        self.working_hours = working_hours
    #查詢名字
    def print_name(self):
        print(self.name)
        return self.name

    #查詢年資
    def print_seniority(self):
        print(self.name,'的年資',self.seniority)
        return self.seniority
    
    #查詢工時
    def print_working_hours(self):
        print(self.name,'的工時',self.working_hours)
        return self.working_hours

    #查詢月薪
    def monthly_salary(self):
        monthly_salary = self.seniority / 12
        print(monthly_salary)
        return monthly_salary

    #增加工時
    def add_working_hours(self,working_hours):
        self.working_hours += working_hours

    #增加年資
    def add_seniority(self,seniority):
        self.seniority += seniority

#飲料類別
class drink:
    #預設建構輸入價格、名稱、甜度
    def __init__(self,money,name,sweet) :
        self.money = money
        self.name = name
        self.sweet = sweet
    #調整名稱
    def rename(self,name):
        self.name = name
    #調整甜度
    def resweet(self,sweet):
        self.sweet = sweet
    #調整價錢
    def remoney(self,money):
        self.money = money

#建立冰飲類別 繼承飲料類別
class ice_drink(drink):
    #繼承飲料類別的屬性再添加冰量屬性
    def __init__(self, money, name, sweet,ice):
        super().__init__(money, name, sweet)
        self.ice = ice

    #調整冰量屬性
    def reice(self,ice):
        self.money = ice
    #列印飲料資料
    def print_drink_data(self):
        print(self.name,self.money,self.sweet,self.ice)
#建立熱飲類別 繼承飲料類別
class hot_drink(drink):
    #繼承飲料類別的屬性
    def __init__(self, money, name, sweet):
        super().__init__(money, name, sweet)
    #列印飲料資料
    def print_drink_data(self):
        print(self.name,self.money,self.sweet)

def main():
    #steven的員工物件
    steven = employer("steven",40000,50)
    steven.print_name()
    steven.print_seniority()
    steven.print_working_hours()
    steven.monthly_salary()
    steven.add_working_hours(10)
    steven.add_seniority(10000)
    steven.print_seniority()
    steven.print_working_hours()

    #Any的員工物件
    Any = employer("Any",40000,50)
    Any.print_name()
    Any.print_seniority()
    Any.print_working_hours()
    Any.monthly_salary()
    Any.add_working_hours(10)
    Any.add_seniority(10000)
    Any.print_seniority()
    Any.print_working_hours()

    #peter的員工物件
    peter = employer("peter",40000,50)
    peter.print_name()
    peter.print_seniority()
    peter.print_working_hours()
    peter.monthly_salary()
    peter.add_working_hours(10)
    peter.add_seniority(10000)
    peter.print_seniority()
    peter.print_working_hours()

    #冰紅茶的冰飲物件
    ice_red_tea = ice_drink(30,"red_tea","small","small")
    ice_red_tea.print_drink_data()
    ice_red_tea.reice("very ice")
    ice_red_tea.remoney(25)
    ice_red_tea.resweet("very sweet")
    ice_red_tea.print_drink_data()

    #冰綠茶的冰飲物件
    ice_green_tea = ice_drink(30,"green_tea","small","small")
    ice_green_tea.print_drink_data()
    ice_green_tea.reice("very ice")
    ice_green_tea.remoney(25)
    ice_green_tea.resweet("very sweet")
    ice_green_tea.print_drink_data()

    #冰奶茶的冰飲物件
    ice_mike_tea = ice_drink(45,"mike_tea","small","small")
    ice_mike_tea.print_drink_data()
    ice_mike_tea.reice("very ice")
    ice_mike_tea.remoney(40)
    ice_mike_tea.resweet("very sweet")
    ice_mike_tea.print_drink_data()

    #熱紅茶的冰飲物件
    hot_red_tea =hot_drink(30,"red_tea","small")
    hot_red_tea.print_drink_data()
    hot_red_tea.remoney(25)
    hot_red_tea.resweet("very sweet")
    hot_red_tea.print_drink_data()

    #熱綠茶的冰飲物件
    hot_green_tea = hot_drink(30,"green_tea","small")
    hot_green_tea.print_drink_data()
    hot_green_tea.remoney(25)
    hot_green_tea.resweet("very sweet")
    hot_green_tea.print_drink_data()

    #熱奶茶的冰飲物件
    hot_mike_tea = hot_drink(45,"mike_tea","small")
    hot_mike_tea.print_drink_data()
    hot_mike_tea.remoney(40)
    hot_mike_tea.resweet("very sweet")
    hot_mike_tea.print_drink_data()

if __name__=='__main__':
    main()


