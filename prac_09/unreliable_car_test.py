from unreliable_car import UnreliableCar


my_unreliable_car = UnreliableCar("TheUnreliableMobile", 100, 40)

for i in range(20):
    print(f"Attempting to drive {i}km:")
    print(f"{my_unreliable_car.name} drove {my_unreliable_car.drive(1)}")

print(my_unreliable_car)