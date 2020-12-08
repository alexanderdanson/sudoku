import random
import math


class Grid:

    grid = []
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    attempts = 0

    def __init__(self):
        success = False
        while not success:
            self.grid = []
            for i in range(81):
                self.grid.append(0)
            success = self.populate_grid()
            self.attempts += 1

    def populate_grid(self):
        for n in self.possible_numbers:
            rows = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            possible_columns = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            while len(possible_columns) > 0:
                for row in rows:
                    random.shuffle(possible_columns)
                    column = self.try_column_index(possible_columns, row, n)
                    if column == -1:
                        return False
                    else:
                        possible_columns.remove(column)
        return True

    def try_column_index(self, possible_columns, row, n):
        for c in possible_columns:
            index = c + (row * 9)
            if (self.grid[index] == 0) & (self.check_section(index, n)):
                self.grid[index] = n
                return c
        return -1

    @staticmethod
    def get_section_start_from_index(index):
        section_starts = [0, 3, 6, 27, 30, 33, 54, 57, 60]
        row = math.floor(index / 9)
        col = index % 9
        sectionRow = math.floor(row / 3)
        sectionCol = math.floor(col / 3)
        section_index = sectionRow * 3 + sectionCol
        return section_starts[section_index]

    @staticmethod
    def get_section_indices(section_start):
        generator_array = [0, 1, 2, 9, 10, 11, 18, 19, 20]
        indices = []

        for n in generator_array:
            indices.append(n + section_start)

        return indices

    def check_section(self, index, number):
        section_start = self.get_section_start_from_index(index)
        section_indices = self.get_section_indices(section_start)
        for i in section_indices:
            if self.grid[i] == number:
                return False
        return True

#
# new_grid = Grid()
# print(new_grid.grid)
# # print(new_grid.grid[0:9])
# # print(new_grid.grid[9:18])
# # print(new_grid.grid[18:27])
# # print(new_grid.grid[27:36])
# # print(new_grid.grid[36:45])
# # print(new_grid.grid[45:54])
# # print(new_grid.grid[54:63])
# # print(new_grid.grid[63:72])
# # print(new_grid.grid[72:81])
#
# print("number of attempts was: {}".format(new_grid.attempts))
