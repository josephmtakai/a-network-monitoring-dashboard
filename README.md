Network Monitoring Dashboard
A real-time network monitoring dashboard that displays network statistics and alerts for potential security issues. Built with Flask for the backend and HTML/CSS for the frontend, utilizing Python libraries psutil and scapy to gather network data.

Features
Real-time network statistics display
Customizable alerting for network issues
Dashboard with HTML/CSS frontend
Backend built with Flask and Python
Network data gathered using psutil and scapy

Project Structure
network_monitoring_dashboard/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── utils.py
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
├── network_monitor.py
├── config.py
└── run.py

Prerequisites
Python 3.8 or higher
Pip (Python package installer)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/network-monitoring-dashboard.git
cd network-monitoring-dashboard
Set Up a Virtual Environment (Recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

bash
Copy code
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install flask flask-socketio flask-wtf flask-login flask-sqlalchemy psutil scapy
Running the Application
Run the Flask Application:

bash
Copy code
python run.py
The application will start and be accessible at http://127.0.0.1:5000.

Access the Dashboard:

Open a web browser and go to http://127.0.0.1:5000 to view the dashboard.

Project Files
app/__init__.py: Initializes the Flask app and SocketIO.
app/routes.py: Defines the routes and API endpoints.
app/utils.py: Contains utility functions (e.g., network stats gathering).
network_monitor.py: Script for network monitoring using psutil and scapy.
config.py: Configuration settings for the Flask app.
run.py: Entry point to start the Flask application.
static/styles.css: CSS styles for the frontend.
templates/index.html: HTML template for the dashboard.

Technologies Used
Backend: Flask, Flask-SocketIO
Frontend: HTML, CSS, JavaScript
Libraries: psutil, scapy
Database: SQLite (optional, if using Flask-SQLAlchemy)

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or feedback, please reach out to joseph.mtakai@outlook.com.

