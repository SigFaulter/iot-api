from api import create_api
from api.db import init_db

app = create_api()

if __name__ == '__main__':
    app.run(debug=True)

