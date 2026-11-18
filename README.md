# Wanderlust Tourism App

A web-based tourism and travel package management application built with **Flask**, **Flask-SQLAlchemy**, and **MySQL**. Users can explore destinations, search and filter travel packages, book trips, manage their bookings, and manage packages through a dashboard.

---

## Features

- **User Authentication**: Register new accounts, log in, and log out with Flask session management.
- **Explore & Search Packages**: Browse popular destination cards and a fixed-price itinerary table, search packages by title or description, and filter by country/destination.
- **Booking Management**: Book travel packages, view all personal bookings on the **My Bookings** page, and cancel bookings.
- **Package Management Dashboard**: Authenticated users can access the dashboard to **add**, **edit**, and **delete** tour packages.
- **Responsive UI**: Custom CSS styling with responsive navigation menu and interactive package cards.

---

## Tech Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy, PyMySQL
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript, Jinja2 Templates

---

## Project Structure

```text
Wanderlust-Tourism-App/
├── README.md
└── tourism_system/
    ├── app.py                  # Main Flask application, models, and routes
    ├── tourism_db.sql          # MySQL database schema and sample seed data
    ├── static/
    │   ├── css/
    │   │   └── style.css       # Application stylesheet
    │   ├── js/
    │   │   └── script.js       # Client-side interactivity and animations
    │   └── images
    └── templates/
        ├── index.html          # Home page with search, filter, and packages
        ├── login.html          # User login page
        ├── register.html       # User registration page
        ├── dashboard.html      # Package management dashboard
        ├── add_package.html    # Form to create a new package
        ├── edit_package.html   # Form to edit an existing package
        └── my_bookings.html    # User's booked packages and cancellation
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server (e.g., MySQL, XAMPP, or MariaDB)

### 1. Clone the Repository

```bash
git clone https://github.com/daasrijita16-creator/Wanderlust-Tourism-App.git
cd Wanderlust-Tourism-App
```

### 2. Install Python Dependencies

Create a virtual environment (recommended) and install the required packages:

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install flask flask-sqlalchemy pymysql
```

> **Note:** If you are using MySQL 8+ with `caching_sha2_password` authentication, you may also need `pip install cryptography`.

### 3. Configure the MySQL Database

1. Start your MySQL server.
2. Import the SQL schema and sample data from `tourism_system/tourism_db.sql`:

   ```bash
   mysql -u root -p < tourism_system/tourism_db.sql
   ```

   *(Or import `tourism_system/tourism_db.sql` via phpMyAdmin.)*

3. Update the database URI in `tourism_system/app.py` if your MySQL username, password, or host differs from the default:

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/tourism_db'
   ```

### 4. Run the Application

```bash
cd tourism_system
python app.py
```

Open your browser and go to:

```text
http://127.0.0.1:5000
```

---

## Sample Credentials

The `tourism_db.sql` script seeds the following sample accounts:

| Username | Password |
| -------- | -------- |
| `admin`  | `1234`   |
| `user1`  | `1234`   |

---

## Database Schema

- **`users`**: `id`, `username`, `password`
- **`packages`**: `id`, `title`, `description`, `price`, `duration`, `image_url`
- **`bookings`**: `id`, `user_id` (FK -> `users.id`), `package_id` (FK -> `packages.id`), `booking_date`

---

## Application Routes

| Route | Method(s) | Description |
| --- | --- | --- |
| `/` | `GET` | Home page displaying all packages with `?search=` and `?country=` filtering |
| `/register` | `GET`, `POST` | Register a new user account |
| `/login` | `GET`, `POST` | Authenticate and start a user session |
| `/logout` | `GET` | Clear the active session and redirect to home |
| `/dashboard` | `GET` | View and manage all packages (requires login) |
| `/add` | `GET`, `POST` | Add a new travel package (requires login) |
| `/edit/<id>` | `GET`, `POST` | Edit an existing travel package (requires login) |
| `/delete/<id>` | `GET` | Delete a travel package (requires login) |
| `/book/<package_id>` | `GET` | Book a travel package (requires login) |
| `/my-bookings` | `GET` | View the logged-in user's bookings (requires login) |
| `/cancel-booking/<booking_id>` | `GET` | Cancel one of the logged-in user's bookings (requires login) |
