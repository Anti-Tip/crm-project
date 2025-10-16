# CRM Project

A Django-based Customer Relationship Management (CRM) system designed to manage products, advertisements, leads, contracts, and customers.

## Features

- **Products Management**: Create, view, edit, and delete products.
- **Advertisements Management**: Handle advertising campaigns.
- **Leads Management**: Track potential customers and leads.
- **Contracts Management**: Manage customer contracts.
- **Customers Management**: Maintain customer information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Anti-Tip/crm-project.git
   cd crm-project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`

## Usage

- Navigate to the admin panel at `http://127.0.0.1:8000/admin/` to manage data.
- Use the web interface to perform CRUD operations on products, advertisements, leads, contracts, and customers.

## Project Structure

- `crm/`: Main Django project settings.
- `products/`: App for managing products.
- `advertisements/`: App for managing advertisements.
- `leads/`: App for managing leads.
- `contracts/`: App for managing contracts.
- `customers/`: App for managing customers.
- `templates/`: HTML templates for the web interface.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
