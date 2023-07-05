# Flask Student Management App

This is a simple Flask application that allows users to submit student information and store it in a SQLite database. The application provides validation for age, mobile number, email, and uniqueness of roll number, mobile number, and email.

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/flask-student-management.git

2. Navigate to the project directory:

    cd flask-student-management

3. Install the required dependencies:

    pip install -r requirements.txt

## Usage

1. Start the Flask development server:

    flask run

2. Access the application in your web browser at http://localhost:5000.
3. Fill in the student information form with the required fields (name, college, age, roll number, mobile number, email).
4. Click the "Submit" button to save the data to the database.
5. If there are any validation errors or if the entered roll number, mobile number, or email already exists in the database, appropriate error messages will be displayed.
6. To view the stored student data, navigate to http://localhost:5000/display.
