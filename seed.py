from faker import Faker
from api.db import db
from api.models.models import Device, Data
from datetime import datetime

fake = Faker()

def generate_fake_devices_and_data(num_devices=5, num_entries_per_device=10):
    # Create fake devices
    for _ in range(num_devices):
        device_id = fake.uuid4()
        token = fake.uuid4()

        device = Device(device_id=device_id, token=token)
        db.session.add(device)

        for _ in range(num_entries_per_device):
            data = Data(
                device_id=device.device_id,
                created=fake.date_this_year(),
                temperature=fake.random_number(digits=2),
                humidity=fake.random_number(digits=2),
                leds_stats=fake.json(),
                servo=fake.random_int(min=0, max=100),
                brightness=fake.random_number(digits=2)
            )
            db.session.add(data)

    db.session.commit()
    print(f"Generated {num_devices} devices with {num_devices * num_entries_per_device} data entries.")

if __name__ == "__main__":
    from api import create_api

    app = create_api()
    with app.app_context():
        generate_fake_devices_and_data()

