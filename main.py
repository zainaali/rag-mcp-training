from inventory.product import Product
from inventory.calculation import calculate_total

product1 = Product("Towels", 500)
product2 = Product("Bedsheets", 5200)

product1.display()
product2.display()

total = calculate_total(500, 100) + calculate_total(5200, 50)

print("Total inventory:", total)