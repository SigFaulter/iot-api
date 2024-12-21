from api.db import db
from datetime import datetime

class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), unique=True, nullable=False)
    token = db.Column(db.String(64), unique=True, nullable=False)

    data = db.relationship('Data', backref='device', lazy=True)

class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), db.ForeignKey('devices.device_id'), nullable=False)  # Foreign key added
    servo = db.Column(db.Integer, nullable=False)
    leds_stats = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        return {
            'servo': self.servo,
            'brightness': self.brightness
        }

class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), db.ForeignKey('devices.device_id'), nullable=False)  # Foreign key added
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    leds_stats = db.Column(db.JSON, nullable=False)
    servo = db.Column(db.Integer, nullable=False)
    brightness = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'device_id': self.device_id,
            'created': self.created,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'leds_stats': self.leds_stats,
            'servo': self.servo,
            'brightness': self.brightness
        }

