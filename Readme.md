# 🛍️ The Cloth Store - Django E-commerce Website

An elegant and responsive online clothing store built using **Django**, **MySQL**, and **Razorpay** for payment integration. Built with modular apps for product management, user authentication, cart, and checkout system.

---

## 🚀 Features

- 🧾 User registration and login system
- 🛒 Add-to-cart, update, and remove items
- 💳 Razorpay Payment Gateway integration
- 🖼️ Product images with category filtering
- 👨‍💼 Admin panel for product management
- 📦 Order management
- 🔐 Secure with environment-based configuration

---

## ⚙️ Tech Stack

- Python 3.11
- Django 4.2+
- MySQL
- Razorpay
- HTML/CSS, Bootstrap
- Render (for hosting)

---

## 🔑 Environment Variables

Create a `.env` file in your root project folder with:

```env
DJANGO_SECRET_KEY=your-django-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

MYSQL_DB=your-db-name
MYSQL_USER=your-db-user
MYSQL_PASSWORD=your-db-password
MYSQL_HOST=your-db-host

RAZORPAY_KEY_ID=your-razorpay-key-id
RAZORPAY_KEY_SECRET=your-razorpay-secret
🔧 Setup Instructions
Clone the Repository

bash
Copy
Edit
git clone https://github.com/Sumit-Bhosle/TheClothStore.git
cd TheClothStore
Create Virtual Environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run Migrations & Create Superuser

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Run the Server

bash
Copy
Edit
python manage.py runserver
🌐 Live Demo
🚧 Coming Soon on Render

📸 Screenshots
<img src="screenshots/home.png" width="100%" /> <img src="screenshots/cart.png" width="100%" /> <img src="screenshots/checkout.png" width="100%" />
🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss.

📄 License
This project is open-source and available under the MIT License.