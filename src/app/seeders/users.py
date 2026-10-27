
from sqlalchemy import select

import app.models
from app.core.security import hash_password
from app.database import SessionLocal
from app.features.users.model import User


def seed_users() -> None:
    users = [
        {
            "name": "Admin",
            "email": "admin@example.com",
            "role": "admin",
        },
        {
            "name": "John Doe",
            "email": "john@example.com",
            "role": "user",
        },
    ]

    with SessionLocal() as db:
        try:
            default_password = hash_password("P@ssw0rd")

            existing_emails = set(
                db.scalars(
                    select(User.email).where(
                        User.email.in_([item["email"] for item in users])
                    )
                ).all()
            )

            for item in users:
                if item["email"] in existing_emails:
                    print(f"Skipped existing user: {item['email']}")
                    continue

                db.add(
                    User(
                        name=item["name"],
                        email=item["email"],
                        hashed_password=default_password,
                        role=item["role"],
                    )
                )

            db.commit()

        except Exception:
            db.rollback()
            raise

    print("User seeding completed.")


if __name__ == "__main__":
    seed_users()
