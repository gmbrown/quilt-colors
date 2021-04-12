class House:
    allowed_colors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    def __init__(self, wall_color, door_color, roof_color, sky_color):
        self.color_set = set()
        for color in [wall_color, door_color, roof_color, sky_color]:
            if not color in self.allowed_colors:
                raise Exception(color + " is not one of the allowed colors")

            if color in self.color_set:
                raise Exception("a house must be all unique colors")

            self.color_set.add(color)

        self.wall_color = wall_color
        self.door_color = door_color
        self.roof_color = roof_color
        self.sky_color = sky_color

    def colors(self):
        return [self.wall_color, self.door_color, self.roof_color, self.sky_color]

    def __str__(self):
        return self.wall_color + self.door_color + self.roof_color + self.sky_color