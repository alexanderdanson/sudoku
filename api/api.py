from flask import Flask
import sudoku

app = Flask(__name__)

@app.route('/generate_board')
def generate_board():
    new_grid = sudoku.Grid()
    return {'board': new_grid.grid}