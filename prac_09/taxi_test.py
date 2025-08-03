from taxi import Taxi

def main():
    """Test the taxi calss provided."""
    price_per_km = 1.23
    my_taxi = Taxi("Prius 1", 100, price_per_km)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()