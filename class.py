class car:
    
    def __init__(self,brand,colour,cost):
        self.brand=brand
        self.colour=colour
        self.cost=cost
    
    def show_info(self):
        print(f"{self.brand} car")
        print(f"Colour: {self.colour}")
        print(f"Cost: ${self.cost}")

    def discount(self,persentage):
        self.persentage=persentage
        new_cost=(self.cost-(self.cost*persentage/100))
        print("The discounted price for ",self.brand,"is",new_cost)

    def comparison(self,other_car):
        if self.cost>other_car.cost:
            print(f"{self.brand}, is expensive")
        else:
            print(other_car.brand," is more expensive")


car1=car("BMW","Blue",400)
car2=car("Thar","Black",60)

car1.comparison(car2)
