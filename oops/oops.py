class Car:
  
  def __init__(self,brand,model):
    self.__brand=brand
    self.model=model
    print("Car created")
   
  def get_brand(self):
    return self.__brand 
    




my_car=Car("lol",20)
print(my_car.get_brand())