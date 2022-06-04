from simulation import *
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
sim = Simulation()

templates = Jinja2Templates(directory="templates")

'''
Main endpoints
'''


class Robot(BaseModel):
    position_x: int
    position_y: int
    direction: str


class Dino(BaseModel):
    position_x: int
    position_y: int


class Command(BaseModel):
    position_x: int
    position_y: int
    command: str


@app.post("/create-board")
def create_board():
    try:
        sim.create_board()
        return {"message": "Board successfully created"}
    except Exception as e:
        return {"message": "Failure in board creation", "error": e}


@app.post("/deploy-robot")
def deploy_robot(robot: Robot):
    try:
        sim.create_robot((robot.position_x, robot.position_y), robot.direction)
        return {"message": "Robot successfully deployed"}
    except Exception as e:
        return {"message": "Failure in deploying robot", "error": e}


@app.post("/deploy-dino")
def deploy_dino(dino: Dino):
    try:
        sim.create_dinosaur((dino.position_x, dino.position_y))
        return {"message": "Dinosaur successfully deployed"}
    except Exception as e:
        return {"message": "Failure in deploying dinosaur", "error": e}


@app.post("/robot-command")
def robot_commands(command: Command):
    try:
        sim.robot_instructions((command.position_x, command.position_y), command.command)
        return {"message": "Command given"}
    except Exception as e:
        return {"message": "Failure in giving command", "error": e}


@app.get("/show-board", response_class=HTMLResponse)
def show_board(request: Request):
    board = sim.board.board
    return templates.TemplateResponse("board.html", {"request": request, "board": board, "toggle": toggle_color})


'''
Helper methods
'''


def toggle_color(i, j):
    return "white" if ((i * 50) + j + i) % 2 == 0 else "grey"
