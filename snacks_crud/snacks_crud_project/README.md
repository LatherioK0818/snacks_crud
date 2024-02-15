# LAB - Class 28

## Project: Django CRUD and Forms - Snacks CRUD Project

### Author: Latherio Kidd

### Links and Resources

- Back-end server URL (when applicable): `N/A`
- Front-end application (when applicable): `N/A`

### Setup

#### `.env` requirements (where applicable)

- `N/A` (This Django project does not require environment variables for basic setup.)

#### How to initialize/run your application

- Create a virtual environment: `python -m venv .venv`
- Activate the virtual environment: 
  - Windows: `.venv\Scripts\activate`
  - MacOS/Linux: `source .venv/bin/activate`
- Install the dependencies: `pip install -r requirements.txt`
- Run migrations: `python manage.py migrate`
- Start the Django development server: `python manage.py runserver`
- Access the application in your browser at: `http://127.0.0.1:8000/`

#### How to use the application

- Navigate to the homepage to see a list of snacks.
- Use the navigation links to:
  - Add a new snack
  - View details about a snack
  - Update snack information
  - Delete a snack

### Tests

- How to run tests: Run `python manage.py test` in the terminal.
- All views should have tests verifying they are accessible and render the correct templates.
- The Snack model should have tests verifying string representation and all fields.

### Description

This project adds full CRUD (Create, Read, Update, Delete) functionality to a Django web application. The project involves creating a `snacks_crud_project` with a `snacks` app, where users can manage snack items through a web interface. The application utilizes Django's class-based views for handling CRUD operations and integrates with Django's admin interface for backend management.

### Feature Tasks and Requirements

- **Create `snacks_crud_project` Django project**
- **Create `snacks` app**
- **Create `Snack` model with fields:**
  - `title`
  - `purchaser`
  - `description`
- **Register model with admin**
- **Implement Views:**
  - `SnackListView`
  - `SnackDetailView`
  - `SnackCreateView`
  - `SnackUpdateView`
  - `SnackDeleteView`
- **Configure URLs for all views**
- **Create templates for all views**
- **Add navigation links**

### Stretch Goals

- Add multiple models to the project.
- Use an alternate test runner.
- Add more advanced fields to models, e.g., created timestamp.
- Enhance the application with additional styling.

### Implementation Notes

This project follows the "Django way" of implementing functionality, ensuring that best practices are followed. Refer back to Django documentation and demos for guidance.

### Configuration

Create a virtual environment inside the `snacks_crud` directory to isolate the project dependencies.


