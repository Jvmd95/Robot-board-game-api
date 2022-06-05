from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Board successfully created"}


def test_robot_deploy():
    response = client.post(
        "/robot/deploy",
        json={"robot_name": "Sergio", "position_x": 0, "position_y": 1, "direction": "N"},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Robot successfully deployed"}


def test_dino_deploy():
    response = client.post(
        "/dino/deploy",
        json={"position_x": 0, "position_y": 0},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Dinosaur successfully deployed"}


def test_robot_command():
    response = client.post(
        "/robot/command",
        json={"robot_name": "Sergio", "command": "turn right"},
    )

    print(response.content)
    assert response.status_code == 200
    assert response.json() == {"message": "Command given"}
