from app import create_app
import os

app = create_app(config_name=os.getenv('APP-SETTINGS'))

if __name__ == '__main__':
    app.run(debug=True)