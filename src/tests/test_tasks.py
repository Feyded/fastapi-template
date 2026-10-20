def test_get_tasks(client):
    payload = {"title": "title", "description": "description"}

    client.post("/tasks", json=payload)

    response = client.get("/tasks")

    body = response.json()

    assert isinstance(body["data"], list)
    assert len(body["data"]) == 1


def test_get_task(client, sample_task):

    response = client.get(f"/tasks/{sample_task.id}")

    body = response.json()

    assert body["data"]["id"] is not None
    assert body["data"]["title"] == "Sample task"
    assert body["data"]["description"] == "Created by a fixture"


def test_create_task(client):

    payload = {"title": "title", "description": "description"}

    response = client.post("/tasks", json=payload)

    assert response.status_code == 201

    body = response.json()

    assert body["message"] == "Task created successfully"
    assert body["data"]["title"] == payload["title"]
    assert body["data"]["description"] == payload["description"]

    assert body["data"]["id"] is not None


def test_update_task(client, sample_task):

    update_payload = {
        "title": "Updated title",
    }

    response = client.patch(
        f"/tasks/{sample_task.id}",
        json=update_payload,
    )

    assert response.status_code == 200

    body = response.json()

    assert body["data"]["id"] == sample_task.id
    assert body["data"]["title"] == "Updated title"
    assert body["data"]["description"] == "Created by a fixture"


def test_delete_task(client, sample_task):

    delete_response = client.delete(f"/tasks/{sample_task.id}")

    assert delete_response.status_code == 204


def test_get_task_returns_404_when_not_found(client):

    response = client.get("/tasks/9999999")

    assert response.status_code == 404


def test_create_task_returns_422_when_invalid_payload(client):
    payload = {
        "title": "Original title",
    }

    response = client.post("/tasks", json=payload)

    assert response.status_code == 422


def test_get_task_returns_existing_task(client, sample_task):
    response = client.get(f"/tasks/{sample_task.id}")

    assert response.status_code == 200
    assert response.json()["data"]["title"] == "Sample task"
