import reflex as rx

class Config(rx.Config):
    app_name = "frontend"
    api_url = "http://127.0.0.1:8001"  # URL del backend en FastAPI

config = Config()
