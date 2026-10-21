import os

import psycopg

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS release_runs (id serial PRIMARY KEY, at timestamptz DEFAULT now())")
    conn.execute("INSERT INTO release_runs DEFAULT VALUES")
print("migrated")
