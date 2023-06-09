# Event Management

Event Management is a web application built with Django that helps users organize and manage various types of events.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Event creation
- User can Register for upcoming events
- User profile management
## Technologies

The Event Management application is built using the following technologies:

- Django: a high-level Python web framework
- SQLite: a lightweight and file-based relational database (can be replaced with other databases like PostgreSQL, MySQL, etc.)
- HTML/CSS: for frontend design and styling
- JavaScript: for frontend interactivity (if applicable)
- Bootstrap: a popular CSS framework for responsive and mobile-first design
- Python: the programming language used for the backend development

Please note that the technologies used in your specific project may vary. Feel free to customize this list to accurately reflect the technologies utilized in your Django web application.


## Installation

- Clone the repository:
```shell
  git clone https://github.com/SATISH84461/event_management.git
```

- Navigate to the project directory
```shell
  cd event_management
```
- Create a virtual environment
```shell
  python -m venv venv
```
- Activate the virtual environment
```shell
  .\venv\Scripts\activate
```
- Install the dependencies
```shell  
  pip install -r requirements.txt
```
- Run command to create new tables.
```shell
  python manage.py makemigrations
```
- Apply the database migrations
```shell
  python manage.py migrate
```
- Create a superuser account
```shell
  python manage.py createsuperuser
```
- Start the development serve
```shell
  python manage.py runserver  
```
- Access the application by visiting `http://localhost:8000` in your web browser.

Note: The above instructions assume that you have Python and pip installed on your system. If not, make sure to install them before proceeding with the steps.

For more details on deploying the application to a production environment or using a different database, please refer to the documentation or specific deployment guides.


Please customize the instructions based on your project requirements, and provide any additional details or steps necessary for the successful installation of your Django application.

## Usage

1. Register a new user account or log in with an existing one.

2. Create an event by providing the necessary details such as event name, date, etc.

3. See the upcoming and past events.

4. Register for upcoming Event.

5. Update your user profile with any changes or preferences.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make the necessary changes and commit them.

4. Push your branch to your forked repository.

5. Submit a pull request describing your changes.
