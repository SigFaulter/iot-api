from faker import Faker
import json
from api.db import db
from api.models.models import Device, Data, Status
from datetime import datetime

fake = Faker()

def generate_fake_devices_and_data(num_devices=1, num_entries_per_device=5):
    # Create fake devices
    for _ in range(num_devices):
        device_id = fake.uuid4()
        token = "b397e865-c68f-4b30-b065-126547e26abc" # testing token

        device = Device(device_id=device_id, token=token)
        db.session.add(device)

        for _ in range(num_entries_per_device):
            data = Data(
                device_id=device.device_id,
                created=fake.date_this_year(),
                temperature=fake.random_number(digits=2),
                humidity=fake.random_number(digits=2),
                leds_stats=json.dumps([1,0,1,0]),
                servo=fake.random_int(min=0, max=100),
                brightness=fake.random_number(digits=2)
            )
            db.session.add(data)

    status = Status(
        device_id=device.device_id,
        servo=fake.random_int(min=0, max=100),
        leds_stats=json.dumps([1,0,1,0]),
    )
    db.session.add(status)
    db.session.commit()
    print("Generated")

if __name__ == "__main__":
    from api import create_api

    app = create_api()
    with app.app_context():
        generate_fake_devices_and_data()

