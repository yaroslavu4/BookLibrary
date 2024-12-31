# Library Web App

## Overview

This is a library web application built using Django. The application allows users to view a list of books available in
the library, view details about the books, and manage book loans. The application is containerized using Docker and
Docker Compose for easy deployment.

The application also includes features like:

- Background task processing using `Celery`.
- A scheduler for periodic tasks using `Celery Beat`.
- A task monitoring UI using `Celery Flower`.
- `Redis` as a message broker for task queuing.

### API Hosting

The site is hosted on the DigitalOcean Droplet and the backend API is accessible at:

**API URL:** `http://178.128.37.135:8000/library/`

## Functional Requirements

### As a user, I can:

- **View the list of books available in the library**  
  This feature is implemented and accessible to all users.

- **View the list of readers registered in the library**  
  This feature is also implemented and available.

- **View the details of a book**  
  Available to all users who are logged in. Guests can view the book list, but only logged-in users can view the full
  details.

- **Assign a book to a reader**  
  This can only be done by the admin (librarian) through the `Django Admin` interface.

- **View the details of a reader and books taken by them**  
  Only admins can view the details of all readers and their borrowed books. Regular users can only view their own
  borrowed books by accessing `MY Profile`.

### Bonus Features

- **Ability to log in as a library admin or reader**  
  Implemented with Django's user authentication. Admins are superusers, and other users are readers.

- **Time limit (expiration) on book loans**  
  Books are assigned a loan period of 2 weeks. A button is provided in ***"MY Profile"*** to return books. Celery Task
  is used
  to monitor overdue books and reassign them to the next reader in the queue.

- **Ability to request a book**  
  Regular users can request unavailable books through the "Request Book" button, and they will be notified once the book
  becomes available.

- **Deployment: app available on a public URL**  
  The app is deployed and accessible via the following URLs:

---

## Deployment URLs

1. **Web Application URL:**  
   Your site is available at:  
   `http://178.128.37.135:8000/library/`  
   ![Site Preview]()

2. **PgAdmin UI (for database management):**  
   PgAdmin UI can be accessed at:  
   `http://178.128.37.135:5050/`

3. **Django Admin Panel:**  
   The Django admin panel is available at:  
   `http://178.128.37.135:8000/admin/`

4. **Celery Flower (Task Monitoring):**  
   Celery Flower for monitoring tasks is available at:  
   `http://178.128.37.135:5555/`

---

## Technologies Used

- **Django** - Web framework for building the application.
- **Docker** - For containerization and easy deployment.
- **Postgres** - Database used to store book and reader information.
- **Celery** - For background task processing.
- **Celery Beat** - For scheduling tasks periodically.
- **Redis** - Message broker for Celery.
- **PgAdmin** - UI for managing Postgres databases.
- **Celery Flower** - UI for monitoring Celery tasks.

---

## List of existing Users

#### (*Or you could create new ones via 'register' pane*)

### Admin

- **Username:** admin
- **password:** admin

### Readers

1. **Username:** jdoe92  
   **password:** Test User 1

2. **Username:** sarah_smith  
   **password:** Test User 2

3. **Username:** michael_king  
   **password:** Test User 3

4. **Username:** emily_wilson  
   **password:** Test User 4

5. **Username:** david_jones  
   **password:** Test User 5

6. **Username:** alice_brown  
   **password:** Test User 6

7. **Username:** tom_harris  
   **password:** Test User 7

8. **Username:** charlotte_miller  
   **password:** Test User 8

9. **Username:** james_clark  
   **password:** Test User 9  
