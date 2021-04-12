from house import House

class InvalidQuiltException(Exception):
    pass

class Quilt:
    def __init__(self):
        self.house_rows = []
        self.house_color_order_set = set()
        for i in range(10):
            row = []
            for i in range(10):
                row.append(None)
            self.house_rows.append(row)

    def is_complete(self):
        for row in self.house_rows:
            for house in row:
                if not (isinstance(house, House) and house.is_complete()):
                    return False
        return True

    def set_house(self, row, column, house):
        if house.is_complete() and str(house) in self.house_color_order_set:
            raise InvalidQuiltException("All houses in the quilt must be unique")

        for neighbor in self.get_neighbors(row, column):
            for color in house.color_set:
                if color in neighbor.color_set:
                    raise InvalidQuiltException("Neighbooring houses cannot share any colors")

        if house.sky_color in self.get_all_sky_color_in_row(row):
            raise InvalidQuiltException("Sky color must be unique within each row")

        if house.sky_color in self.get_all_sky_color_in_column(column):
            raise InvalidQuiltException("Sky color must be unique within each column")

        self.house_rows[row][column] = house
        self.house_color_order_set.add(str(house))

    def get_all_sky_color_in_row(self, row):
        sky_colors_in_row = set()
        for house in self.house_rows[row]:
            if house:
                sky_colors_in_row.add(house.sky_color)
        return sky_colors_in_row

    def get_all_sky_color_in_column(self, column):
        sky_colors_in_column = set()
        for row in range(10):
            if self.house_rows[row][column]:
                sky_colors_in_column.add(self.house_rows[row][column].sky_color)
        return sky_colors_in_column

    def get_neighbors(self, row, column):
        neighbors = []
        if column != 0 and self.house_rows[row][column - 1]:
            neighbors.append(self.house_rows[row][column - 1])
        if column != 9 and self.house_rows[row][column + 1]:
            neighbors.append(self.house_rows[row][column + 1])
        return neighbors

    def __str__(self):
        print_str = ""
        for row in self.house_rows:
            for house in row:
                print_str += str(house)
                print_str += " "
            print_str += "\n"
        return print_str