Here's your updated README section with the prerequisites:

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (version 3.11.6 ) - [Download Python](https://www.python.org/downloads/)
- MySQL (version 8.0.34) - [Download MySQL](https://dev.mysql.com/downloads/)
- Git - [Download Git](https://git-scm.com/downloads)
- Visual Studio Code (optional, but recommended) - [Download Visual Studio Code](https://code.visualstudio.com/Download)

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sumit-Bhosle/TheClothStore.git
   cd TheClothStore
   ```

2. **Install Dependencies**

   Use pip to install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Setting Up Environment Variables**

   Create a `.env` file in the root directory of your project and define the necessary environment variables. For example:

   ```plaintext
   DB_NAME=cloth_db
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   ```

   Replace `your_database_user` and `your_database_password` with your MySQL database username and password respectively.

4. **Creating the Database**

   Ensure MySQL is installed on your system. Then, create a database with the name specified in your `settings.py` file (`cloth_db` in this case):

   ```bash
   mysql -u your_database_user -p
   # Enter your MySQL password when prompted
   CREATE DATABASE cloth_db;
   ```

5. **Applying Migrations**

   Apply the database migrations to create the necessary tables in your database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Creating a Superuser**

   Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your superuser account.

7. **Running the Development Server**

   Start the development server and begin working on your project:

   ```bash
   python manage.py runserver
   ```

   Access your project at -  http://127.0.0.1:8000/

---

for any further queries and suggestions write me at sumit.bhosle98@gmail.com
