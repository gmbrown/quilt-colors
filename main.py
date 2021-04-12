from house import House
from quilt import Quilt

def house_from_number(number):
    wall_color = House.allowed_colors[int(number/1000) % 10]
    door_color = House.allowed_colors[int(number/100) % 10]
    roof_color = House.allowed_colors[int(number/10) % 10]
    sky_color = House.allowed_colors[number % 10]
    return House(wall_color, door_color, roof_color, sky_color)

def number_from_house(house):
    return House.allowed_colors.index(house.wall_color) * 1000 + \
    House.allowed_colors.index(house.door_color) * 100 + \
    House.allowed_colors.index(house.roof_color) * 10 + \
    House.allowed_colors.index(house.sky_color)

# consider every house to be a 4 letter word.
# the "next" house is the next word in alphabetical order
# that is valid in that all 4 colors are unique
def next_house(house):
    number = number_from_house(house)

    while(number < 10000):
        number += 1
        try:
            return house_from_number(number)
        except:
            pass

    raise Exception("cannot find another valid house")

q = Quilt()
h = None
for row in range(10):
    for column in range(10):
        if not h:
            h = House("A", "B", "C", "D")
        else:
            h = next_house(h)
        q.set_house(row, column, h)

print(q.is_complete())

print(q)
