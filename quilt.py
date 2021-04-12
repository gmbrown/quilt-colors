from house import House

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
                if not isinstance(house, House):
                    return False
        return True

    def set_house(self, row, column, house):
        if str(house) in self.house_color_order_set:
            raise Exception("All houses in the quilt must be unique")

        for neighbor in self.get_neighbors(row, column):
            for color in house.colors():
                if color in neighbor.colors():
                    raise Exception("Neighbooring houses cannot share any colors")

        self.house_rows[row][column] = house
        self.house_color_order_set.add(str(house))

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