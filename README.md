# Image Database Manager

This project provides a simple interface to manage image uploads and displays using a PostgreSQL database. It allows you to insert images from a directory into the database and display them on demand.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or higher
- PostgreSQL database server
- Python packages listed in the `requirements.txt` file (`asyncio`, `psycopg3`, `PIL`)
- A reference directory to store the images. This directory should be created before running the project.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/sako-ranj/psycopg3-python.git
cd psycopg3-python
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

3. Set up the PostgreSQL database and configure the database connection in `config.py`:

```python
DATABASE_CONFIG = {
    'database': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}

IMAGE_PATH = 'path_to_your_image_directory'  # e.g., 'references/'
```

Replace `'your_database_name'`, `'your_username'`, `'your_password'`, and `'path_to_your_image_directory'` with your actual database credentials and image directory path.

## Usage

To use the Image Database Manager, follow these steps:

1. Ensure your PostgreSQL server is running.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the main script with one of the following commands:

   - To insert all images from the specified directory into the database:
   
     ```sh
     python main.py insert
     ```

   - To display all images stored in the database:
   
     ```sh
     python main.py display
     ```

Note: Make sure to replace `python` with the appropriate command if you're using a virtual environment.



## Acknowledgements

- Thanks to the developers of `psycopg3` and `PIL` for their contributions to the Python ecosystem.
- Special thanks to the community for feedback and support.

Feel free to customize the project further based on your needs or contribute to its development. Enjoy managing your image database!