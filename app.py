from advertisingManager import app
import os

if __name__ == '__main__':
    app.run(debug = True, port = int(os.environ.get('PORT', 33507)))