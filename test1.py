#建立炸雞類別
class FriedChicken:
    #預設建構輸入炸雞名稱
    def __init__(self,name):
        self.name =name
        self.sauce = None
        self.sweetness = None
        self.acidity = None
        self.spiciness = None
        self.salinity = None
#設定炸雞的味道
    def fried_chicken_smell(self, sweetness=None, acidity=None, spiciness=None, salinity=None):
        if sweetness is not None:
            self.sweetness = sweetness

        if acidity is not None:
            self.acidity = acidity

        if spiciness is not None:
            self.spiciness = spiciness

        if salinity is not None:
            self.salinity = salinity
        
#設定炸雞使用的醬料
    def fried_chicken_use_sauce(self, sauce):
        self.sauce = sauce

#列印炸雞的資料
    def print_fried_chicken_smell(self):
        print('fried chicken name:', self.name)
        print('use sauce:', self.sauce) 
        print('sweetness:', self.sweetness) 
        print('acidity:', self.acidity )
        print('salinity:', self.salinity) 
        print('spiciness:', self.spiciness)
        return [self.name,self.sauce, self.sweetness, self.acidity, self.salinity, self.spiciness]

def main():
    #韓式炸雞
    korean_fried_chicken = FriedChicken("korean_fried_chicken")  # Instantiate the class
    korean_fried_chicken.fried_chicken_smell("slightly sweet", "slightly acidic", "slightly spicy", "Not salty")
    korean_fried_chicken.fried_chicken_use_sauce("Korean hot sauce")
    korean_fried_chicken.print_fried_chicken_smell()
    #紐澳良炸雞
    New_Orleans_fried_chicken = FriedChicken("New_Orleans_fried_chicken")  # Instantiate the class
    New_Orleans_fried_chicken.fried_chicken_smell("slightly sweet", "Not acidic", "slightly spicy", "slightly salty")
    New_Orleans_fried_chicken.fried_chicken_use_sauce("New Orleans Sauce")
    New_Orleans_fried_chicken.print_fried_chicken_smell()
    #鹽酥雞
    Crispy_Salted_Chicken = FriedChicken("Crispy_Salted_Chicken")  # Instantiate the class
    Crispy_Salted_Chicken.fried_chicken_smell("Not sweet", "Not acidic", "Not spicy", "salty")
    Crispy_Salted_Chicken.fried_chicken_use_sauce("Salt")
    Crispy_Salted_Chicken.print_fried_chicken_smell()
    #蜂蜜炸雞
    Honey_fried_chicken = FriedChicken("Honey_fried_chicken")  # Instantiate the class
    Honey_fried_chicken.fried_chicken_smell("sweet", "Not acidic", "Not spicy", "Not salty")
    Honey_fried_chicken.fried_chicken_use_sauce("Honey")
    Honey_fried_chicken.print_fried_chicken_smell()

if __name__ == '__main__':
    main()