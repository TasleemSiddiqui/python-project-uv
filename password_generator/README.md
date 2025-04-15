# Password Generator

A simple and user-friendly password generator built with Streamlit. This application allows you to create secure passwords with customizable options.

## Features

- Generate passwords with customizable length (8-32 characters)
- Option to include numbers
- Option to include special characters
- Clean and intuitive user interface

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the project files
2. Create a virtual environment (recommended):
   ```bash
   uv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required packages:
   ```bash
   uv add streamlit
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the following command:
   ```bash
   streamlit run main.py
   ```
3. The application will open in your default web browser

## Usage

1. Use the slider to select your desired password length (8-32 characters)
2. Check the boxes to include numbers and/or special characters
3. Click the "Generate Password" button
4. Your new password will be displayed on the screen

## Project Structure

- `main.py` - Contains the main application code
- `README.md` - This documentation file

## Dependencies

- streamlit
- random (Python standard library)
- string (Python standard library)

## License

This project is open source and available for personal and commercial use.
