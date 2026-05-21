import time
import random
from src.data.user import User


def generate_user_data() -> User:
    ts = int(time.time() * 1000)
    firstname = f"John{ts}"
    lastname = f"Doe{ts}"
    return User(
        name=f"{firstname} {lastname}",
        email=f"user{ts}@example.com",
        password=f"Password{ts}!",
        title=random.choice(["Mr", "Mrs", "Miss", "Dr"]),
        birth_date=str(random.randint(1, 28)),
        birth_month=str(random.randint(1, 12)),
        birth_year=str(random.randint(1960, 2000)),
        firstname=firstname,
        lastname=lastname,
        company=f"Company{ts}",
        address1=f"{random.randint(1, 999)} Main St",
        address2=f"Apt {random.randint(1, 99)}",
        country="United States",
        zipcode=f"{random.randint(10000, 99999)}",
        state="California",
        city="Los Angeles",
        mobile_number=f"+1{random.randint(1000000000, 9999999999)}",
    )