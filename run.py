from api import create_api
from api.db import db

app = create_api()

# Make sure the app context is correctly set
with app.app_context():
    # Create all tables (if they don't exist)
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
