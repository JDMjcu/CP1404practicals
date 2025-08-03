"""
CP1404/CP5632 Practical
SilverServiceTaxi class test
JDM
"""

from silver_service_taxi import SilverServiceTaxi

# Test the Hummer taxi 
hummer_taxi = SilverServiceTaxi("Hummer", 200, fanciness=4)
print(hummer_taxi)

# Test the fare calculations
test_taxi = taxi = SilverServiceTaxi("TheFancyMobile", 200, fanciness=2)
print(test_taxi)
test_taxi.start_fare()
test_taxi.drive(18)
taxi_fare = taxi.get_fare()
print(f"Fare for 18km trip: ${taxi_fare:.2f}")
# assert taxi_fare == 48.78, f"Expected fare: $48.78, got: ${taxi_fare:.2f}"
assert taxi_fare == 48.80, f"Expected fare: $48.78, got: ${taxi_fare:.2f}"