import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from my_fastapi_app_v2.database import Base


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
