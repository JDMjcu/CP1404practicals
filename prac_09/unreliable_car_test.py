from unreliable_car import UnreliableCar


my_unreliable_car = UnreliableCar("TheUnreliableMobile", 100, 40)

for i in range(20):
    print(f"{my_unreliable_car.name} is attempting to drive {i}km: it drove {my_unreliable_car.drive(1)}")

print(my_unreliable_car)