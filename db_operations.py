# db_operations.py

import psycopg

async def create_table(acur):
    await acur.execute(
        "CREATE TABLE IF NOT EXISTS face(faceID SERIAL PRIMARY KEY, name TEXT, faceImg BYTEA)"
    )

async def insert_image(acur, name, image_data):
    await acur.execute(
        "INSERT INTO face(name, faceImg) VALUES (%s, %s)",
        (name, image_data),
    )

async def fetch_images(acur):
    await acur.execute("SELECT * FROM face")
    return await acur.fetchall()

async def get_connection(db_config):
    return await psycopg.AsyncConnection.connect(
        host=db_config["host"],
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"]
    )
