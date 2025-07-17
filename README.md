# Electric Shop Management System

This project is an Electric Shop Management System built using Django. It provides a comprehensive solution for managing an electric shop, including features for product management, sales invoicing, customer and supplier ledgers, expense tracking, profit/loss reporting, and user management.

## Features

- **Dashboard**: A central hub for accessing various functionalities of the system.
- **Product/Stock Management**: Add, edit, and delete products, and manage stock levels.
- **Sales Invoicing**: Generate invoices for sales transactions.
- **Customer Ledger**: Track customer transactions and balances.
- **Supplier Ledger**: Manage supplier information and transactions.
- **Expense Record**: Record and track business expenses.
- **Profit/Loss Report**: Generate reports to analyze business performance.
- **Multi-User Login**: Support for multiple user accounts with different roles and permissions.
- **Backup System**: Backup and restore data for safety and recovery.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd electric-shop-management
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. Apply migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```
   python manage.py runserver
   ```

9. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Log in using the superuser account to access the admin panel.
- Use the dashboard to navigate through different sections of the application.
- Manage products, customers, suppliers, and expenses through their respective sections.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.