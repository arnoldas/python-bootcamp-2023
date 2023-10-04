# Function with unlimited keyword arguments
def calculate(**kwargs):
    #print(type(kwargs)) #Dictionary type
    #print(kwargs) #{'add': 3, 'multiply': 5}
    for key, value in kwargs.items():
        print(f"key - {key} with value: {value}")
    print(kwargs["multiply"]) # prints 5


calculate(add=3, multiply=5)

# Exmaple when in one function are unlimited arguments and unlimited keyword arguments
def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)  # 4 (7, 3, 0) {'x': 10, 'y': 64}

# class example with key arguments
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]   # throw an error if in kw doesn't exist "make" argument
        #self.model = kw["model"]
        self.model = kw.get("model") # better use get method because if "model" doesn't exist in kw argument then
                                     # just return none instead of throw an error

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)