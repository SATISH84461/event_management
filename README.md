# Event Management

Event Management is a web application built with Django that helps users organize and manage various types of events.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Technologies](#technologies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Event creation and management
- RSVP functionality for attendees
- Event search and filtering
- Event reminders and notifications
- User profile management

## Demo

You can find a live demo of the application at [Demo Link](https://your-demo-link.com).

## Technologies

The project is built using the following technologies:

- Django: a high-level Python web framework
- PostgreSQL (or any other preferred database): for data storage
- HTML/CSS: for frontend design and styling
- JavaScript: for frontend interactivity (if applicable)


## Installation

1. Install my-project with npm
```shell
  git clone https://github.com/SATISH84461/event_management.git
```

2. Navigate to the project directory
```shell
  cd event_management
```
3. Create a virtual environment
```shell
  python -m venv venv
```
4. Activate the virtual environment
```shell
  venv/bin/activate
```
5. Install the dependencies
```shell  
  pip install -r requirements.txt
```
6. Apply the database migrations
```shell
  python manage.py migrate
```
7. Create a superuser account
```shell
  python manage.py createsuperuser
```
8. Start the development serve
```shell
  python manage.py runserver  
```
10. Access the application by visiting `http://localhost:8000` in your web browser.
        

## Usage

1. Register a new user account or log in with an existing one.

2. Create an event by providing the necessary details such as event name, date, time, location, etc.

3. Browse existing events, search for specific events, and filter them based on criteria like date or location.

4. RSVP to events you wish to attend.

5. Receive notifications and reminders for upcoming events.

6. Update your user profile with any changes or preferences.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make the necessary changes and commit them.

4. Push your branch to your forked repository.

5. Submit a pull request describing your changes.
