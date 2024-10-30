import reflex as rx

class Config(rx.Config):
    app_name = "frontend"
    api_url = "http://127.0.0.1:8001"  # URL del backend en FastAPI
    backend_host = "127.0.0.1"  # Dirección del backend
    backend_port = 8001      # Puerto del backend

config = Config()
