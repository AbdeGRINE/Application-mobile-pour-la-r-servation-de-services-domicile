# gunicorn_config.py
bind = '127.0.0.1:8000'  # Change this to your desired host and port
workers = 4  # Adjust the number of workers based on your server's resources
timeout = 120