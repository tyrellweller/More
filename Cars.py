def make_car(name , model , **other):
    car = {}
    car['name'] = name
    car['model'] = model
    for key , value in other.items():
        car[key] = value
    return car
car = make_car("yamaha" , 'outback' , color = "green" , price = 2.2 , size = "large")
for key , value in car.items():
    print(key + " : " + str(value))