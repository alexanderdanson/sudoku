import React, { useState, useEffect, moment } from 'react';
import logo from './logo.svg';
import './App.css';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import Alert from 'react-bootstrap/Alert';

function App() {

  const [sudoku_grid, setSudokuGrid] = useState([]);

  useEffect(() => {
    fetch('/generate_board').then(res => res.json()).then(data => {
      setSudokuGrid(data.board);
    });
  }, []);

  const [show, setShow] = useState(true);


  return (
    <div className="App">
      <header className="App-header">


        <p>{sudoku_grid}</p>

        <Button onClick={() => window.location.reload()}>Generate New Board</Button>

      </header>
      <body>
        <Alert show={show} variant="success">
          <Alert.Heading>Welcome to Sudoku!</Alert.Heading>
          <p>
            I hope you can solve the puzzle. The aim is to place each of the numbers 1-9 in the grid, 9 times! Easy?
            <br></br>
            Well... you're not allowed the same number in the same row twice!
            <br></br>
            Aaannd....you're not allowed to use the same number in the same column twice either!
            <br></br>
            And just to make it extra hard, you can't have the same number in the same section either.
            <br></br>
            Good luck my friend!!
        </p>
          <hr />
          <div className="d-flex justify-content-end">
            <Button onClick={() => setShow(false)} variant="outline-success">
              Close Instructions!
          </Button>
          </div>
        </Alert>

        {!show && <Button onClick={() => setShow(true)} variant="outline-danger">Show Instructions</Button>}
      </body>
    </div>
  );
}

export default App;
