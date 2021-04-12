class InvalidHouseException(Exception):
    pass

class House:
    allowed_colors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    def __init__(self):
        self.color_set = set()
        self.wall_color = None
        self.door_color = None
        self.roof_color = None
        self.sky_color = None

    def set_wall_color(self, wall_color):
        if self.wall_color:
            raise InvalidHouseException("wall color already set")
        if not wall_color in self.allowed_colors:
            raise InvalidHouseException(wall_color + " is not one of the allowed colors")
        if wall_color in self.color_set:
                raise InvalidHouseException("a house must be all unique colors")
        self.wall_color = wall_color

    def set_door_color(self, door_color):
        if self.door_color:
            raise InvalidHouseException("door color already set")
        if not door_color in self.allowed_colors:
            raise InvalidHouseException(door_color + " is not one of the allowed colors")
        if door_color in self.color_set:
                raise InvalidHouseException("a house must be all unique colors")
        self.door_color = door_color

    def set_roof_color(self, roof_color):
        if self.roof_color:
            raise InvalidHouseException("roof color already set")
        if not roof_color in self.allowed_colors:
            raise InvalidHouseException(roof_color + " is not one of the allowed colors")
        if roof_color in self.color_set:
                raise InvalidHouseException("a house must be all unique colors")
        self.roof_color = roof_color

    def set_sky_color(self, sky_color):
        if self.sky_color:
            raise InvalidHouseException("sky color already set")
        if not sky_color in self.allowed_colors:
            raise InvalidHouseException(sky_color + " is not one of the allowed colors")
        if sky_color in self.color_set:
                raise InvalidHouseException("a house must be all unique colors")
        self.sky_color = sky_color

    def is_complete(self):
        return self.wall_color and self.door_color and self.roof_color and self.sky_color

    def __str__(self):
        w = " "
        if self.wall_color:
            w = self.wall_color
        d = " "
        if self.door_color:
            d = self.door_color
        r = " "
        if self.roof_color:
            r = self.roof_color
        s = " "
        if self.sky_color:
            s = self.sky_color
        return w + d + r + s