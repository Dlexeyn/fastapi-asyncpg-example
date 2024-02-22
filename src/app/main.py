from fastapi import FastAPI

from app.configuration.server import Server
from app.internal.routes import heroes
from app.db import db


server = Server(FastAPI())
