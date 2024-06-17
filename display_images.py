# display_images.py

import asyncio
import platform
from config import DATABASE_CONFIG
from db_operations import get_connection, fetch_images
from image_operations import display_image

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def display_all_images():
    async with await get_connection(DATABASE_CONFIG) as aconn:
        async with aconn.cursor() as acur:
            records = await fetch_images(acur)
            for record in records:
                display_image(record[2])
                print(f"Name: {record[1]}")

if __name__ == "__main__":
    asyncio.run(display_all_images())
