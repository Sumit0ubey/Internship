                                              Push-up Logger


● Overview:

The Push-up Logger is a Python application designed to help users track and log their push-up exercises with the help of Flask. 
It provides an easy-to-use interface to record the number of push-ups performed each day and visualize progress over time.


● Features:
  - Record daily push-up counts
  - View historical data in a tabular format
  - Generate simple visualizations of progress over time
  - User-friendly command-line interface


● Structure:

Push-up Logger

├── instance

│ └── db.sqlite

├── static

│ ├── background.jpg

│ ├── Muscle.ico

│ ├── Profile_pic.png

│ ├── push-ups.gif

│ └── sololearn.png

├── templates

│ ├── common.html

│ ├── index.html

│ ├── signup.html

│ ├── Profile.html

│ ├── Postfeed.html

│ ├── login.html

│ ├── createworkout.html

│ ├── updateworkout.html

│ └── allworkouts.html

├── create_db.py

├── main.py

└── requirements.txt


● Installation:
To get started with the Push-up Logger, follow these steps:
1. Clone the repository:
    git clone https://github.com/Sumit0ubey/Internship.git

2. Navigate to the project directory:
    cd Internship/Python\ Programing/Push-up\ Logger
   
4. Set up a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate

5. Install the required dependencies:
    pip install -r requirements.txt

● Usage
To start logging push-ups, run the main script:
python main.py

● License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
