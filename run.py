from app import create_app

app = create_app('production')   # add 'production' config to config.py

if __name__ == '__main__':
    app.run()
