# insert_images.py
import os
import asyncio
import platform
from config import DATABASE_CONFIG
from db_operations import get_connection, create_table, insert_image
from image_operations import read_image, list_image_files

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def insert_all_images():
    async with await get_connection(DATABASE_CONFIG) as aconn:
        async with aconn.cursor() as acur:
            await create_table(acur)

            # Insert all images from the references folder
            image_files = list_image_files("references")
            for image_file in image_files:
                image_data = read_image(image_file)
                image_name = os.path.basename(image_file)
                await insert_image(acur, image_name, image_data)

if __name__ == "__main__":
    asyncio.run(insert_all_images())
