from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from ClothApp.models import Category

class Command(BaseCommand):
    help = 'Initialize the database: makemigrations, migrate, create superuser, default categories'

    def handle(self, *args, **kwargs):
        self.stdout.write("🔄 Running makemigrations...")
        call_command('makemigrations')

        self.stdout.write("✅ Running migrate...")
        call_command('migrate')

        # Create Superuser
        User = get_user_model()
        admin_data = {
            "first_name": "Admin",
            "last_name": "User",
            "username": "admin",
            "email": "admin@theclothstore.com",
            "password": "admin123"
        }

        if not User.objects.filter(username=admin_data["username"]).exists():
            self.stdout.write("👑 Creating default superuser...")
            User.objects.create_superuser(
                first_name=admin_data["first_name"],
                last_name=admin_data["last_name"],
                username=admin_data["username"],
                email=admin_data["email"],
                password=admin_data["password"]
            )
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser created — username: {admin_data['username']}, password: {admin_data['password']}"))
        else:
            self.stdout.write("✅ Superuser already exists.")

        # Default Categories
        default_categories = ['Men', 'Women', 'Unisex']

        self.stdout.write("🛒 Checking for default categories...")
        for cat in default_categories:
            if not Category.objects.filter(category_name=cat).exists():
                Category.objects.create(category_name=cat)
                self.stdout.write(self.style.SUCCESS(f"✅ Created category: {cat}"))
            else:
                self.stdout.write(f"✔️ Category already exists: {cat}")

        self.stdout.write(self.style.SUCCESS("🎉 Database fully initialized!"))
