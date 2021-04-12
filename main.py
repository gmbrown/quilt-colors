from house import House, InvalidHouseException
from quilt import Quilt, InvalidQuiltException

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

    while(True):
        number += 1
        if number == 10000:
            number = 0
        try:
            return house_from_number(number)
        except InvalidHouseException:
            pass

def try_build_quilt(bad_door_values):
    q = Quilt()
    h = None
    for row in range(10):
        for column in range(10):
            h = House()
            h.set_wall_color(House.allowed_colors[(column + row) % 10])
            h.set_sky_color(House.allowed_colors[(column + row + 2) % 10])
            q.set_house(row, column, h)

    for row in range(10):
        for column in range(10):
            h = q.house_rows[row][column]
            empty_house = House()
            q.set_house(row, column, empty_house)

            found_solution = False
            for color in House.allowed_colors:
                if color in bad_door_values[row][column]:
                    continue
                try:
                    new_house = House()
                    new_house.set_wall_color(h.wall_color)
                    new_house.set_sky_color(h.sky_color)
                    new_house.set_door_color(color)
                    q.set_house(row, column, new_house)
                    found_solution = True
                    break
                except InvalidHouseException:
                    print("invalid house")
                    pass
                except InvalidQuiltException:
                    print("invalud quilt")
                    pass
            if not found_solution:
                raise Exception("could not find valid house")

    for row in range(10):
        for column in range(10):
            h = q.house_rows[row][column]
            empty_house = House()
            q.set_house(row, column, empty_house)

            found_solution = False
            for color in House.allowed_colors:
                try:
                    new_house = House()
                    new_house.set_wall_color(h.wall_color)
                    new_house.set_sky_color(h.sky_color)
                    new_house.set_door_color(h.door_color)
                    new_house.set_roof_color(color)
                    q.set_house(row, column, new_house)
                    found_solution = True
                    break
                except InvalidHouseException as e:
                    pass
                except InvalidQuiltException as e1:
                    pass
            if not found_solution:
                print(q)
                bad_door_values[row][column].append(h.door_color)
                return bad_door_values

    print(q.is_complete())

    print(q)
    return "success"

bad_door_values = []
for i in range(10):
    bad_door_values.append([])
    for j in range(10):
        bad_door_values[i].append([])

for i in range(100):
    bad_door_values = try_build_quilt(bad_door_values)
    print(bad_door_values)
    if bad_door_values is "success":
        break
