from src.simulation import *
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
sim = Simulation()

templates = Jinja2Templates(directory="templates")

'''''''''''''''
Main endpoints
'''''''''''''''


class Robot(BaseModel):
    robot_name: str
    position_x: int
    position_y: int
    direction: str


class Dino(BaseModel):
    position_x: int
    position_y: int


class Command(BaseModel):
    robot_name: str
    command: str


@app.get("/")
def create_board():
    try:
        sim.create_board()
        return {"message": "Board successfully created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/robot/deploy")
async def deploy_robot(robot: Robot):

    if not _valid_direction(robot.direction):
        raise HTTPException(status_code=400, detail="Invalid direction. Direction can be one of the following values: "
                                                    "'N', 'S', 'E', 'W'")

    if not _valid_position(robot.position_x, robot.position_y):
        raise HTTPException(status_code=400, detail="Invalid position. Position X and Y need to be in range [0-50]")

    try:
        sim.create_robot(robot.robot_name, (robot.position_x, robot.position_y), robot.direction)
        return {"message": "Robot successfully deployed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/dino/deploy")
async def deploy_dino(dino: Dino):

    if not _valid_position(dino.position_x, dino.position_y):
        raise HTTPException(status_code=400, detail="Invalid position. Position X and Y need to be in range [0-50]")

    try:
        sim.create_dinosaur((dino.position_x, dino.position_y))
        return {"message": "Dinosaur successfully deployed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/robot/command")
async def robot_commands(command: Command):

    if _valid_command(command):
        raise HTTPException(status_code=400, detail="Invalid command. Commands can be one of the following: "
                                                "'turn left', 'turn right', 'move forward', 'move backward', 'attack'")

    try:
        sim.robot_instructions(command.robot_name, command.command)
        return {"message": "Command given"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/board", response_class=HTMLResponse)
def show_board(request: Request):
    try:
        board = sim.board.board
        return templates.TemplateResponse("board.html", {"request": request, "board": board, "toggle": toggle_color})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


'''''''''''''''''
Helper functions
'''''''''''''''''


def toggle_color(i, j):
    return "white" if ((i * 50) + j + i) % 2 == 0 else "grey"


def _valid_direction(direction):
    directions = ["N", "S", "E", "W"]
    if direction not in directions:
        return False
    else:
        return True


def _valid_position(position_x, position_y):
    if not (0 <= position_x <= 50 and 0 <= position_y <= 50):
        return False
    else:
        return True


def _valid_command(command):
    commands = ["turn left", "turn right", "move forward", "move backward", "attack"]
    if command not in commands:
        return False
    else:
        return True
