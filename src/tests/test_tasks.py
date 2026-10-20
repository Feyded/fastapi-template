def test_get_tasks(client):
    payload = {"title": "title", "description": "description"}

    client.post("/tasks", json=payload)

    response = client.get("/tasks")

    body = response.json()

    assert isinstance(body["data"], list)
    assert len(body["data"]) == 1


def test_get_task(client):
    payload = {"title": "title", "description": "description"}

    create_reponse = client.post("/tasks", json=payload)

    assert create_reponse.status_code == 201

    task_id = create_reponse.json()["data"]["id"]

    response = client.get(f"/tasks/{task_id}")

    body = response.json()

    assert body["data"]["id"] is not None
    assert body["data"]["title"] == "title"
    assert body["data"]["description"] == "description"


def test_create_task(client):

    payload = {"title": "title", "description": "description"}

    response = client.post("/tasks", json=payload)

    assert response.status_code == 201

    body = response.json()

    assert body["message"] == "Task created successfully"
    assert body["data"]["title"] == payload["title"]
    assert body["data"]["description"] == payload["description"]

    assert body["data"]["id"] is not None


def test_update_task(client):
    create_payload = {
        "title": "Original title",
        "description": "Original description",
    }

    create_response = client.post("/tasks", json=create_payload)

    assert create_response.status_code == 201

    task_id = create_response.json()["data"]["id"]

    update_payload = {
        "title": "Updated title",
        "description": "Updated description",
    }

    response = client.patch(
        f"/tasks/{task_id}",
        json=update_payload,
    )

    assert response.status_code == 200

    body = response.json()

    assert body["data"]["id"] == task_id
    assert body["data"]["title"] == "Updated title"
    assert body["data"]["description"] == "Updated description"


def test_delete_task(client):
    create_payload = {
        "title": "Original title",
        "description": "Original description",
    }

    create_response = client.post("/tasks", json=create_payload)

    assert create_response.status_code == 201

    task_id = create_response.json()["data"]["id"]

    delete_response = client.delete(f"/tasks/{task_id}")

    assert delete_response.status_code == 204
