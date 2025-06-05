# Frontend Documentation for Databox Project

This is the frontend part of the Databox project, which is built using React. The frontend communicates with the Django backend to provide a seamless user experience.

## Project Structure

The frontend directory contains the following structure:

```
frontend
├── public
│   ├── index.html        # Main HTML file for the React application
│   └── favicon.ico       # Favicon for the web application
├── src
│   ├── assets            # Contains images and icons used in the application
│   │   ├── logo_databox.png
│   │   ├── data_icon.png
│   │   ├── ia_icon.png
│   │   └── dash_icon.png
│   ├── components        # Reusable React components
│   │   ├── CardButton.jsx
│   │   └── ...
│   ├── pages             # Different pages of the application
│   │   ├── Home.jsx
│   │   ├── Diagnostico.jsx
│   │   ├── Estrategias.jsx
│   │   ├── Dashboards.jsx
│   │   ├── Login.jsx
│   │   └── Perguntas.jsx
│   ├── App.jsx           # Main application component
│   ├── index.js          # Entry point for the React application
│   └── styles            # Custom styles for the application
│       └── custom.css
├── package.json          # npm configuration file
└── README.md             # Documentation for the frontend
```

## Getting Started

To get started with the frontend, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine.
   
   ```
   git clone <repository-url>
   cd databox-django-react/frontend
   ```

2. **Install Dependencies**: Install the required npm packages.

   ```
   npm install
   ```

3. **Run the Application**: Start the development server.

   ```
   npm start
   ```

   The application will be available at `http://localhost:3000`.

## Components

- **CardButton**: A reusable component that displays a button with an icon and text. It is used throughout the application for navigation.

## Pages

- **Home**: The landing page of the application.
- **Diagnostico**: A page for diagnostic opportunities.
- **Estrategias**: A page for AI strategies.
- **Dashboards**: A page for visualizing metrics.
- **Login**: A page for user authentication.
- **Perguntas**: A page for users to submit their questions.

## Styling

Custom styles are defined in `src/styles/custom.css`. You can modify this file to change the appearance of the application.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.