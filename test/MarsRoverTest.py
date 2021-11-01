import unittest


# Drop mars rover at co-ordinate DONE
# Drop mars rover facing direction DONE
# Move mars rover North Done
# Move East Done
# Move West Done
# Move South Done
# Move mars rover in direction (F/B) Done
# Turn mars rover (R/L)
# Move north to east (R) Done
# Move north to west (L) Done
# Move east to south (R) Done
# Move east to north (L) Done
# Move south to west (R) Done
# Move south to east (L) Done
# Move west to north (R) Done
# Move west to south (L) Done
# Test multiple instructions Done
# Move left multiple times from north Done
# Ignore invalid instruction Done
from MarsRover import MarsRover


class MarsRoverTest(unittest.TestCase):

    def setUp(self):
        self.northRover = MarsRover(4, 7, "North")
        self.southRover = MarsRover(4, 7, "South")
        self.eastRover = MarsRover(4, 7, "East")
        self.westRover = MarsRover(4, 7, "West")

    def test_drop_mars_rover_at_coordinate(self):
        self.assertEqual([4, 7], self.northRover.position())

    def test_drop_mars_rover_facing_direction(self):
        self.assertEqual("North", self.northRover.orientation)

    def test_move_mars_rover_empty_instruction(self):
        self.northRover.move("")
        self.assertEqual([4, 7], self.northRover.position())

    def test_move_forward(self):
        param_list = [self.northRover, self.southRover, self.eastRover, self.westRover]
        position_after_list = [[4, 8], [4, 6], [5, 7], [3, 7]]
        for index, rover in enumerate(param_list):
            with self.subTest():
                rover.move("F")
                self.assertEqual(position_after_list[index], rover.position())

    def test_move_backward(self):
        param_list = [self.northRover, self.southRover, self.eastRover, self.westRover]
        position_after_list = [[4, 6], [4, 8], [3, 7], [5, 7]]
        for index, rover in enumerate(param_list):
            with self.subTest():
                rover.move("B")
                self.assertEqual(position_after_list[index], rover.position())

    def test_change_direction_north_right(self):
        self.northRover.move("R")
        self.assertEqual("East", self.northRover.orientation)

    def test_change_direction_north_left(self):
        self.northRover.move("L")
        self.assertEqual("West", self.northRover.orientation)

    def test_change_direction_east_right(self):
        self.eastRover.move("R")
        self.assertEqual("South", self.eastRover.orientation)

    def test_change_direction_east_left(self):
        self.eastRover.move("L")
        self.assertEqual("North", self.eastRover.orientation)

    def test_change_direction_south_right(self):
        self.southRover.move("R")
        self.assertEqual("West", self.southRover.orientation)

    def test_change_direction_south_left(self):
        self.southRover.move("L")
        self.assertEqual("East", self.southRover.orientation)

    def test_change_direction_west_right(self):
        self.westRover.move("R")
        self.assertEqual("North", self.westRover.orientation)

    def test_change_direction_west_left(self):
        self.westRover.move("L")
        self.assertEqual("South", self.westRover.orientation)

    def test_instruction_multiple_times(self):
        self.northRover.move("FFF")
        self.assertEqual([4, 10], self.northRover.position())

    def test_direction_and_movement(self):
        self.northRover.move("RF")
        self.assertEqual([5, 7], self.northRover.position())

    def test_full_backward_rotation(self):
        self.northRover.move("LLLL")
        self.assertEqual("North", self.northRover.orientation)

    def test_long_rotation(self):
        self.northRover.move("LLLLLR")
        self.assertEqual("North", self.northRover.orientation)

    def test_invalid_instruction(self):
        self.northRover.move("qXqfg")
        self.assertEqual([4, 7], self.northRover.position())
        self.assertEqual("North", self.northRover.orientation)

    def test_valid_instructions_in_sequence_with_invalid(self):
        self.northRover.move("qvvifmFmfoFokfrwF")
        #Move forward 3 times only 'F" is valid instruction
        self.assertEqual([4, 10], self.northRover.position())

if __name__ == '__main__':
    unittest.main()
