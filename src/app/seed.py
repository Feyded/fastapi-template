from app.seeders.users import seed_users


def seed() -> None:
    seed_users()


if __name__ == "__main__":
    seed()
