kilo = float(input("Please enter the number of kilograms you wish to convert: "))
pounds = int(kilo * 2.2046226218487756625)
ounces = (kilo * 35.2739619495804106) - (pounds * 16)
print(kilo, "kilograms is", pounds, "pounds and", ounces, "ounces.")