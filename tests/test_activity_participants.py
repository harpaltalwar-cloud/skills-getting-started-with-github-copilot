from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_from_activity():
    response = client.delete(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"

    updated_activity = client.get("/activities").json()["Chess Club"]
    assert "michael@mergington.edu" not in updated_activity["participants"]


def test_unregister_missing_participant_returns_404():
    response = client.delete(
        "/activities/Chess Club/signup",
        params={"email": "ghost@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
