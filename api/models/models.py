from api.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), unique=True, nullable=False)
    token = db.Column(db.String(64), unique=True, nullable=False)

    # Establish a relationship with the Data table
    data = db.relationship('Data', backref='device', lazy=True)

@dataclass
class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), db.ForeignKey('devices.device_id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    leds_stats = db.Column(db.JSON, nullable=False)
    servo = db.Column(db.Integer, nullable=False)

