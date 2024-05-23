# Finance Tracking - Personal Finance Management System

- **Project Setup and Structure**:
  - Initialized a new Django project and configure it to use PostgreSQL as the database.
  - Used Django REST Framework for creating API endpoints.
  - Organized the project in a clean and modular architecture, separating concerns appropriately (e.g., models, serializers, views).

- **Core Features**:
  - **Income and Expense Models**:
    - Defined models for tracking income and expenses.
    - Each transaction is included fields like amount, category, date, and a description.
  - **Savings Goal Model**:
    - Defined a model for savings goals, including fields like amount, current amount, and deadline.
  - **Transaction API**:
    - Created RESTful API endpoints to list, create, update, and delete incomes, expenses.
    - These endpoints require authentication.
  - **Savings Goal API**:
    - Implemented API endpoints to view and manage savings goals.
  - **User Authentication**:
    - Implement a custom user model and use Django REST Framework to create a login API.
    - Authentication is based on tokens, returning an access token and a refresh token upon successful login.
  - **Registration API**:
    - New user can register through an API endpoint, creating a new user profile.

- **Authentication and Permissions**:
  - Managed user sessions and securing API endpoints.
  - Only authenticated users can create, update, or delete incomes, expenses and savings goals.
  - Users can manage their profiles and financial data only.

- **Database Design**:
  - Database schema with PostgreSQL, ensuring relationships between users, incomes, expenses, and savings goals are efficiently modeled.
  - Implemented migrations for your database models.

- **All API Endpoints**:
  - **Register API**:
    - POST - https://finance-tracking-drf.onrender.com/users/register/
  - **Login API**:
    - POST - https://finance-tracking-drf.onrender.com/users/login/

  - **Savings Goal API**:
    - GET - https://finance-tracking-drf.onrender.com/savings-goals/list/
    - POST - https://finance-tracking-drf.onrender.com/savings-goals/create/
    - PUT - https://finance-tracking-drf.onrender.com/savings-goals/update/[id]/
    - DELETE - https://finance-tracking-drf.onrender.com/savings-goals/delete/[id]/
  - **Income API**:
    - GET - https://finance-tracking-drf.onrender.com/incomes/list/
    - POST - https://finance-tracking-drf.onrender.com/incomes/create/
    - PUT - https://finance-tracking-drf.onrender.com/incomes/update/[id]/
    - DELETE - https://finance-tracking-drf.onrender.com/incomes/delete/[id]/
  - **Expense API**:
    - GET - https://finance-tracking-drf.onrender.com/expenses/list/
    - POST - https://finance-tracking-drf.onrender.com/expenses/create/
    - PUT - https://finance-tracking-drf.onrender.com/expenses/update/[id]/
    - DELETE - https://finance-tracking-drf.onrender.com/expenses/delete/[id]/
  - **Transactions Histories API**:
    - GET - https://finance-tracking-drf.onrender.com/transactions/list/