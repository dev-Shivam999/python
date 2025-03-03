class Car:
  
  def __init__(self,brand,model):
    self.__brand=brand
    self.__model=model
   
  def get_brand(self):
    return self.__brand 
  @property
  def model(self):
    return self.__model  

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
# my_car.model="ttt"
# print(my_car.model)
my_ec=Ec("c","20","10")
# print(my_ec.get_Fule())
# print(my_car.get_description()) 

# print(my_car.model)

# print(isinstance(my_ec,Car))
# print(isinstance(my_car,Ec))








class Battery:
  def bettery_info(self):
    return "Battery is 1000w"

 

class Engine:
  def engine_info(self):
    return "Engine is 1000cc"



class EvCar(Battery,Engine,Car):
  def __init__(self,brand,model):
    Car.__init__(self,brand,model)
    Battery.__init__(self)
    Engine.__init__(self)
  def get_Fule(self):
    return "Electric"
  



mynewCar=EvCar("lol",20)

print(mynewCar.get_brand())
print(mynewCar.engine_info())