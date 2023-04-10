"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqnmheuhlq287bu9t0-a.oregon-postgres.render.com",
        database="demo_todo_i5wm",
        user="demo_todo_i5wm_user",
        password="A34uu7xa5OzUGe4hyElP7ZqzLanB2xJ7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
