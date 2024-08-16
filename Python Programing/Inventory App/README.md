                                    Library Management System

● Overview:
The Library System is a desktop application built with Python's Tkinter library. 
This application allows administrators to manage a library's book inventory and enables users to check out and return books. 
The system also handles user fines for overdue books.


● Features:
- Admin Features:
  - Add new books to the inventory
  - Update existing book details
  - Delete books from the inventory

- User Features:
  - Browse available books
  - Add books to a user's account
  - Return books and check for any fines
  - View a history of checked-out books and fines

● Project Structure:
Library Management System
├── library_Management_System.py
├── library_database.py
├── requirements.txt
└── README.md


● Installation:
To set up the Library System on your local machine, follow these steps:

1. Clone the repository:
    git clone https://github.com/Sumit0ubey/Internship.git

2. Navigate to the project directory:
    cd Internship/Python\ Programing/Library\ System

3. Set up a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install the required dependencies:
    pip install -r requirements.txt

5. Initialize the database:
    Run the library_database.py script to set up the SQLite database:
    `python library_database.py`

6. Run the application:
    Start the Tkinter application by executing:
    `python library_management_system.py`

    The application window will appear, allowing you to interact with the library system.

● Usage

- Admin Interface: Manage the library’s book inventory by adding, updating, or deleting books.
- User Interface:
  - Check out books and return them.
  - View your checked-out books and any fines incurred.
- Fine Management: The system calculates and displays fines for overdue books with the qrcode for the payment.

● License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

● Acknowledgments
  ☆ `Sumit Dubey` - 「 Project lead and developer 」

Feel free to reach out if you have any questions or need further assistance.
