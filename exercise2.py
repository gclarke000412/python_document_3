def area():
    length = float(input('Input length of house '))
    width = float(input('Input width of house '))
    area  = (length) * (width)
    print(f'The square footage of the house is {area} sq ft.')


def circumference():
    radius = float(input("What is the circle's raidus in ft?"))
    circum = 2 * 3.14159 * radius
    print(f'The circumference of the cirlce is {circum} ft.')