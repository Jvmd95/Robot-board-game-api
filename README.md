# Robots vs Dinosaurs API

This a simple python-based API that simulates a board game of robots vs dinosaurs.

## Features

This API is able to:

- Create an empty simulation space - an empty 50 x 50 grid;
- Create a robot in a certain position and facing direction;
- Create a dinosaur in a certain position;
- Issue instructions to a robot - a robot can turn left, turn right, move forward, move backward, and attack;
- Display the simulation's current state;

## Rules

- A robot attack destroys dinosaurs around it (in front, to the left, to the right or behind);
- Dinosaurs dont move
- Two or more entities (robots or dinosaurs) cannot occupy the same position;
- Attempting to move a robot outside the simulation space is an invalid operation.

## Implementation

There are four main classes:

- Simulation handles all the features and rules related to the simulation, answers the API requests.
- Board handles the status of the board.
- Robot stores its name, position and direction. Contains method to turn left or right.
- Dinosaur stores its position. Has no methods.

## Starting the API

- Clone this repository
- Go to the project directory
- On the terminal run: docker build -t myimage .
- It will build the container. Before finishing it will execute a test to check that the code is correct.
- Once the image is built, run the container with the terminal command: docker run -p 80:80 myimage

You should be able to access the API at  http://127.0.0.1/.

To visualize the board go to http://127.0.0.1/board

You can find the documentation http://127.0.0.1/docs

## Endpoints

This API has 5 endpoints:

#### Get `/` 

Creates the board that represents the 50x50 grid of the simulation

#### Get `/board` 

Displays the board. The robots shows their name under their icon and the direction they are facing.

#### Post `/robot/deploy` 

Creates a robot in a position on the board. Takes 4 arguments:

- robot_name: The name of the robot. Robots must have an unique name.
- position x: An integer representing the row where the robot will be displayed
- position y: An integer representing the column where the robot will be displayed
- direction: direction that the robot will be facing. N, S, E or W

#### Post `/dino/deploy` 

Creates a dinosaur in a position on the board. Takes 2 argument:

- position x: An integer representing the row where the dinosaur will be displayed.
- position y: An integer representing the column where the dinosaur will be displayed.

#### Post `/robot/command` 

Gives a robot a command. Takes 2 argument:

- robot_name: The name of the robot you want to control.
- command: Commands can be "turn left", "turn right", "move forward", "move backward", "attack".

For more details about the endpoints check the docs at http://127.0.0.1/docs

