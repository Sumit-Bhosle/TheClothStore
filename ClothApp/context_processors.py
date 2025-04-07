from .models import Category

def menu_link(request):
    links = Category.objects.all()  # fetch all categories
    return dict(links=links)


#  update this file in TEMPLATES under context processor section in SETTINGS.py
# 'APP-NAME.FILE-NAME.FUNCTION-NAME'