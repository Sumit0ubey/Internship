                                    Inventory Management System


● Overview:
The Inventory App is a desktop application designed to help users manage and track inventory items. 
It provides features for adding, updating, and deleting items, as well as viewing current inventory levels and item details.


● Features:
- Manage Inventory:
  - Add new items to the inventory
  - Update existing item details
  - Delete items from the inventory
  - View inventory levels and details

- User Interface:
  - Easy-to-use graphical interface built with Tkinter
 
● Project Structure:

Inventory App

├── inventoryManagementSystem.py

├── inventory_database.py

├── requirements.txt

└── README.md



● Installation:
To set up the Inventory App on your local machine, follow these steps:

1. Clone the repository:
    `
    git clone https://github.com/Sumit0ubey/Internship.git
    `

2. Navigate to the project directory:
    `
    cd Internship/Python\ Programing/Inventory\ App
    `

3. Set up a virtual environment (optional but recommended):
    `
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    `

4. Install the required dependencies:
    `pip install -r requirements.txt`

5. **Initialize the database:**

    Run the inventory_database.py script to create the SQLite database and set up the initial schema:
    `python inventory_database.py`

6. Run the application:
    Start the Inventory App by executing:
    `python inventoryManagementSystem.py`
    The application window will appear, allowing you to manage your inventory.


● Usage

- Main Window: The starting point of the application where you can navigate to different functionalities.
- Add Item: Use the form to add new items to the inventory.
- Update Item: Modify the details of existing inventory items.
- Delete Item: Remove items from the inventory.

● License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

● Acknowledgments
  ☆ `Sumit Dubey` - 「 Project lead and developer 」

Feel free to reach out if you have any questions or need further assistance.
