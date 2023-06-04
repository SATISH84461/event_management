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

The project is built using the following technologies:

- Django: a high-level Python web framework
- PostgreSQL (or any other preferred database): for data storage
- HTML/CSS: for frontend design and styling
- JavaScript: for frontend interactivity (if applicable)


## Installation

- Install my-project with npm
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
4. Activate the virtual environment
```shell
  .\venv\Scripts\activate
```
5. Install the dependencies
```shell  
  pip install -r requirements.txt
```
6. Run command to create new tables.
```shell
  python manage.py makemigrations
```
8. Apply the database migrations
```shell
  python manage.py migrate
```
8. Create a superuser account
```shell
  python manage.py createsuperuser
```
9. Start the development serve
```shell
  python manage.py runserver  
```
10. Access the application by visiting `http://localhost:8000` in your web browser.
        

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
