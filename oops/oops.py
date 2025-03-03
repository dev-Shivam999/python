class Car:
  
  def __init__(self,brand,model):
    self.__brand=brand
    self.model=model
   
  def get_brand(self):
    return self.__brand 

  @staticmethod
  def  get_description():
    return "car is four wheels "
  def get_Fule(self):
    return "Petrol or diesel"  
    
class  Ec(Car):
  def __init__(self, brand,model,size):  
    super().__init__(brand,model)
    self.size=size
  def get_Fule(self):
    return "Electric "  
  

my_car=Car("lol",20)
# my_ec=Ec("c","20","10")
# print(my_ec.get_Fule())
# print(my_car.get_description()) 