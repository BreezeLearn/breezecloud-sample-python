import os

import psycopg
from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        runs = conn.execute("SELECT count(*) FROM release_runs").fetchone()[0]
    return f"python ok; GREETING={os.environ.get('GREETING')!r}; release_runs={runs}\n"
