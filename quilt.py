from house import House

class Quilt:
    def __init__(self):
        self.house_rows = []
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
        self.house_rows[row][column] = house

    def __str__(self):
        print_str = ""
        for row in self.house_rows:
            for house in row:
                print_str += str(house)
                print_str += " "
            print_str += "\n"
        return print_str