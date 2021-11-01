class MarsRover:
    def __init__(self, x_co, y_co, orientation):
        self.x_co = x_co
        self.y_co = y_co
        self.orientation = orientation

    def position(self):
        return [self.x_co, self.y_co]

    def move(self, instructions):
        if not instructions:
            pass
        for instruction in instructions:
            if instruction == 'F' or instruction == 'B':
                move_by = 1
                if self.orientation == "South" or self.orientation == "West":
                    move_by = -move_by
                if self.orientation == "North" or self.orientation == "South":
                    if instruction == 'F':
                        self.y_co += move_by
                    elif instruction == 'B':
                        self.y_co -= move_by
                if self.orientation == "East" or self.orientation == "West":
                    if instruction == 'F':
                        self.x_co += move_by
                    elif instruction == 'B':
                        self.x_co -= move_by
            elif instruction == 'R' or instruction == 'L':
                compass = ["North", "East", "South", "West"]
                current_compass_index = compass.index(self.orientation)
                if instruction == 'R':
                    current_compass_index += 1
                elif instruction == 'L':
                    current_compass_index -= 1
                if current_compass_index >= len(compass):
                    current_compass_index = 0
                self.orientation = compass[current_compass_index]
