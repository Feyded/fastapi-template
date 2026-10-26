from my_fastapi_app_v2.seeders.users import seed_users


def seed() -> None:
    seed_users()


if __name__ == "__main__":
    seed()
