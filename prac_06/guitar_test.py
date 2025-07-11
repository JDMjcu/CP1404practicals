"""
Prac-06
Guitar test code

"""

from guitar import Guitar

object_1 = Guitar("Gibson L-5 CES", 100, 699)
object_2 = Guitar("Another guitar", 2023, 1200120102)

print(object_1)
print(object_2)
# Test get_age
print(f"{object_1.name} get age () - expected 1925 got {object_1.get_age()}")
print(f"{object_2.name} get age () - expected 2 got {object_2.get_age()}")
# Test is_vintage method
print(f"{object_1.name} is_vintage() - expected True got {object_1.is_vintage()}")
print(f"{object_2.name} is_vintage() - expected False got {object_2.is_vintage()}")
