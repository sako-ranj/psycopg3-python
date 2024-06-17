# main.py
import os
import asyncio
import platform
import sys
from config import DATABASE_CONFIG, IMAGE_PATH
from db_operations import get_connection, create_table, insert_image, fetch_images
from image_operations import read_image, display_image, list_image_files

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

async def display_all_images():
    async with await get_connection(DATABASE_CONFIG) as aconn:
        async with aconn.cursor() as acur:
            records = await fetch_images(acur)
            for record in records:
                display_image(record[2])
                print(f"Name: {record[1]}")

def print_usage():
    print("Usage: python main.py [insert|display]")
    print("insert: Insert all images from the 'references' folder into the database.")
    print("display: Display all images stored in the database.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]
    if command == "insert":
        asyncio.run(insert_all_images())
    elif command == "display":
        asyncio.run(display_all_images())
    else:
        print_usage()
        sys.exit(1)
