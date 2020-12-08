import unittest
import sudoku
from datetime import datetime


class SudokuPerformanceTest(unittest.TestCase):

        def test_performance(self):
            number_of_boards = 100
            start_time = datetime.now()
            attempts_array = []
            for i in range(number_of_boards):
                new_grid = sudoku.Grid()
                attempts_array.append(new_grid.attempts)
                self.assertEqual(set(new_grid.grid), {1, 2, 3, 4, 5, 6, 7, 8, 9})
            total = sum(attempts_array)
            count = len(attempts_array)
            average_attempts = total / count
            finish_time = datetime.now()
            print(" \n")
            print("................................................................")
            print("The total time for creating {} boards was: {}".format(number_of_boards, finish_time-start_time))
            print("The average number of attempts was: {}".format(average_attempts))
            print("................................................................")
            print(" \n")

        def test_number_presence(self):
            new_grid = sudoku.Grid()
            self.assertEqual(set(new_grid.grid), {1, 2, 3, 4, 5, 6, 7, 8, 9})

        def test_rows(self):
            test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            new_grid = sudoku.Grid()
            row_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            row_starts = [0, 9, 18, 27, 36, 45, 54, 63, 72]
            for row_start in row_starts:
                row_numbers = []
                for n in row_indexes:
                    index = n + row_start
                    row_numbers.append(new_grid.grid[index])
                self.assertEqual(set(row_numbers), test_set)

        def test_columns(self):
            test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            new_grid = sudoku.Grid()
            column_starts = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            column_indexes = [0, 9, 18, 27, 36, 45, 54, 63, 72]
            for column_start in column_starts:
                column_numbers = []
                for n in column_indexes:
                    index = n + column_start
                    column_numbers.append(new_grid.grid[index])
                self.assertEqual(set(column_numbers), test_set)

        def test_sections(self):
            test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            new_grid = sudoku.Grid()
            section_starts = [0, 3, 6, 27, 30, 33, 54, 57, 60]
            section_indices = [0, 1, 2, 9, 10, 11, 18, 19, 20]
            for section_start in section_starts:
                section_numbers = []
                for n in section_indices:
                    index = n + section_start
                    section_numbers.append(new_grid.grid[index])
                self.assertEqual(set(section_numbers), test_set)


if __name__ == '__main__':
    unittest.main()