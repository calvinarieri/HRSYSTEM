## HRMS Application - README

This document provides instructions on setting up and running the HRMS (Human Resource Management System) application built with Django.

**Prerequisites:**

* Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* pip (usually comes bundled with Python)
* PostgreSQL database ([https://www.postgresql.org/](https://www.postgresql.org/))

**Installation:**

1. Clone this repository:

```bash
git clone https://<your_repository_link>
```

2. Navigate to the project directory:

```bash
cd hrapp
```

3. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install required dependencies:

```bash
pip install -r requirements.txt
```

5. Create a PostgreSQL database and user for the application. Update `DATABASES` settings in `hrapp/settings.py` with your database credentials (name, user, password, host).

6. Apply database migrations:

```bash
python manage.py migrate
```

**Running the Application:**

1. Start the development server:

```bash
python manage.py runserver
```

This will start the server at http://127.0.0.1:8000 by default.

**Authentication:**

The application currently uses Django's built-in authentication system. You'll need to create admin and employee user accounts. You can use the Django admin interface (http://127.0.0.1:8000/admin/) for initial setup:

* Username: admin
* Password: (set a strong password)

**API Endpoints:**

The application uses Django REST framework for API functionalities. Here's a summary of the main endpoints (refer to the code for detailed arguments and responses):

**Employee Management:**

* **GET /employees/:** List all employees. (Requires authentication)
* **GET /employee/<int:id>/:** Retrieve details of a specific employee. (Requires authentication)
* **POST /employees/:::** Create a new employee account. (Admin permission required)

**Emergency Contacts:**

* **GET /next_of_kin/<int:id>/:** Retrieve next of kin information for an employee. (Requires authentication)
* **POST /next_of_kin/<int:id>/:** Add next of kin information for an employee. (Requires authentication)

**Employee Skills:**

* **GET /skills/<int:id>/:** List skills for an employee. (Requires authentication)
* **POST /skills/<int:id>/:** Add a new skill for an employee. (Requires authentication)
* **PUT /skill/<int:id>/:** Update an existing employee skill. (Requires authentication)
* **DELETE /skill/<int:id>/:** Delete an employee skill. (Requires authentication)

**Leave Applications:**

* **GET /leaves/<int:id>/:** List leave applications for an employee. (Requires authentication)
* **POST /leaves/<int:id>/:** Apply for leave. (Requires authentication)
* **PUT /leave/<int:id>/:** Approve or reject leave applications (Admin permission required)

**Testing the API:**

You can use tools like Postman or curl to test the API endpoints. Remember to include authentication credentials (e.g., access token) in your requests for authenticated endpoints.

**Additional Notes:**

* This is a basic implementation of an HRMS application. You can extend it with more functionalities like leave balance calculations, reports, etc.
* Refer to the code for detailed comments and documentation on models and functionalities.
* Security best practices like strong password hashing and proper authorization checks are essential for a production environment.

**Contribution:**

Feel free to clone, modify, and improve this codebase. If you wish to contribute changes, please create a pull request on the repository.
