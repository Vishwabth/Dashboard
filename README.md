# Business Insights Dashboard

A dynamic and interactive Django-based web application designed to visualize and analyze global business trends and data insights across various sectors, countries, and topics. 

## Features

- **Interactive Filtering**: Filter data based on Sector, Country, Topic, Region, PESTLE factors, and Source.
- **Dynamic Visualizations**: Interactive charts depicting Intensity, Likelihood, Relevance, Country, Region, and Topic distributions using Chart.js.
- **Real-time Updates**: AJAX-based real-time data updates without page reloads.
- **Data Summaries**: Overview cards displaying total records, unique sectors, and countries.
- **Responsive UI**: Fully responsive design, mobile-friendly navigation, and user-friendly interface.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Visualization**: Chart.js
- **Database**: SQLite (default, configurable)
- **REST Framework**: Django REST Framework for API handling

## Project Structure
```bassh
dashboard/
├── dashboard/ (Main Django Project)
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── visualization/ (Django App)
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── templates/index.html
│ ├── load_json.py
│ └── migrations/
│
├── staticfiles/ (Static Assets and JS files)
├── manage.py
└── requirements.txt
```

## Installation

Follow these steps to set up and run the dashboard locally:

**1. Clone the Repository**
```bash
git clone https://github.com/Vishwabth/Dashboard.git
cd dashboard
```
**2. Set up virtual enviroment**
```bash
python -m venv env
source env/bin/activate   # For Linux/macOS
env\Scripts\activate      # For Windows
```
**3. Install Dependencies**
```bash
pip install -r requirements.txt
```
**4. Apply Migrations**
```bash
python manage.py migrate
```
**5. Load Initial Data**
```bash
python manage.py shell
>>> from visualization.load_json import load_initial_data
>>> load_initial_data()
>>> exit()
```
**6. Run the Development Server**
```bash
python manage.py runserver
```

## Open your browser and navigate to:
http://localhost:8000

## Usage

- **Applying Filters**: Use the sidebar filters to refine the data visualizations based on specific parameters.
- **Charts**: Click the expand icon (⤢) on any chart to view it in fullscreen mode for better visibility.
- **Real-time Filtering**: Apply or reset filters dynamically without needing to refresh the page.



## Screenshots


<img width="1894" height="898" alt="Screenshot 2025-07-22 080942" src="https://github.com/user-attachments/assets/722dbe82-f968-4753-b3ea-38ed22087820" />
<img width="1897" height="914" alt="Screenshot 2025-07-22 080959" src="https://github.com/user-attachments/assets/4566f126-c73c-458c-8bf1-88415e548f56" />
