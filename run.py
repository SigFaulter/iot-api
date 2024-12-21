from api import create_api
from api.db import init_db
from flask_cors import CORS

app = create_api()
CORS(app, origins=["http://localhost:5000"])

if __name__ == '__main__':
    app.run(debug=True)

