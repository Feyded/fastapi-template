import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from my_fastapi_app_v2.database import Base, get_db
from my_fastapi_app_v2.main import app
from my_fastapi_app_v2.models.task import Task


@pytest.fixture
def db():
    engine = create_engine(
        "sqlite:///./test_tasks.db",
        connect_args={"check_same_thread": False},
    )

    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture
def client(db):
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def sample_task(db):
    task = Task(
        title="Sample task",
        description="Created by a fixture",
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task
