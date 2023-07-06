# Running the Image Resizer App

Follow these steps to run the Image Resizer app using Django:

## Prerequisites

- Python 3.x is installed on your system.

## Setup

1. Clone the repository or download the source code for the Image Resizer app.
    ```
    git clone https://github.com/BLGALEX/resize_image.git
    ```

2. Open a terminal or command prompt and navigate to the project's root directory.
    ```
    cd resize_image
    ```

3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv .venv
   ```

4. Activate the virtual environment:
   - On macOS/Linux:
     ```
     source env/bin/activate
     ```
   - On Windows:
     ```
     .\env\Scripts\activate
     ```

5. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Development Server

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. The app will now be running locally at `http://localhost:8000`.

## Using the API

1. Use Postman or any other tool to interact with the API endpoints.

2. To resize an image, make a POST request to the `resize_picture` endpoint:
   - URL: `http://localhost:8000/api/resize_picture/`
   - Parameters:
     - `file`: The image file to resize (required).
     - `width`: The desired width of the resized image (required).
     - `height`: The desired height of the resized image (optional).

3. The API will return a JSON response containing the URL of the resized image.

## Testing

1. Run the tests for the Image Resizer app:
   ```
   python manage.py test image_resizer
   ```

2. The test results will be displayed in the terminal, showing the success or failure of each test case.


## Media Files

1. The resized images will be saved in the `<project folder>/media` directory by default.

2. If you want to change the directory where the resized images are saved, open the `settings.py` file and change the `MEDIA_ROOT` setting to the desired directory path.

## Log files

1. The log files will be saved in the `<project folder>/logs` directory by default.
