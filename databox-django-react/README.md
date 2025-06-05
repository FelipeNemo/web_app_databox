# Databox Django and React Project

This project is a web application built using Django for the backend and React for the frontend. It aims to provide a platform for users to interact with data, utilize AI strategies, and visualize metrics effectively.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built with Django and contains the following components:

- **databox/**: The main Django project directory.
  - `__init__.py`: Marks the directory as a Python package.
  - `asgi.py`: ASGI configuration for the Django project.
  - `settings.py`: Configuration settings for the Django project, including installed apps and middleware.
  - `urls.py`: URL routing for the Django application.
  - `wsgi.py`: WSGI configuration for the Django project.
  
- **applications/**: Contains Django applications.
  - **home/**: The home application.
    - `__init__.py`: Marks the directory as a Python package.
    - `admin.py`: Registers models with the Django admin site.
    - `apps.py`: Configuration for the home application.
    - `models.py`: Data models for the home application.
    - `tests.py`: Tests for the home application.
    - `urls.py`: URL routing specific to the home application.
    - `views.py`: View functions for the home application.

- `manage.py`: Command-line utility for interacting with the Django project.
- `requirements.txt`: Lists the Python packages required for the backend.

### Frontend

The frontend is built with React and contains the following components:

- **public/**: Contains static files for the React application.
  - `index.html`: Main HTML file for the React application.
  - `favicon.ico`: Favicon for the web application.

- **src/**: Contains the source code for the React application.
  - **assets/**: Contains images used in the application.
    - `logo_databox.png`: Logo image for the application.
    - `data_icon.png`: Icon for data mapping.
    - `ia_icon.png`: Icon for AI strategies.
    - `dash_icon.png`: Icon for dashboards.
  
  - **components/**: Contains reusable React components.
    - `CardButton.jsx`: Represents a button card with an icon and text.
  
  - **pages/**: Contains React components for different pages.
    - `Home.jsx`: Home page component.
    - `Diagnostico.jsx`: Diagnostic page component.
    - `Estrategias.jsx`: Strategies page component.
    - `Dashboards.jsx`: Dashboards page component.
    - `Login.jsx`: Login page component.
    - `Perguntas.jsx`: Questions page component.
  
  - `App.jsx`: Main component that sets up routing and renders the application.
  - `index.js`: Entry point for the React application.
  - **styles/**: Contains custom CSS styles.
    - `custom.css`: Custom styles for the application.

- `package.json`: Configuration file for npm, listing dependencies and scripts for the frontend.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd databox-django-react
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required packages:
     ```
     pip install -r requirements.txt
     ```
   - Run the Django server:
     ```
     python manage.py runserver
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required packages:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.