from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models import Products,Category
from django.db.models import Q

# Temperory migration for RENDER HOSTING
from django.core.management import call_command
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
import os

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def setup(request):
    setup_flag = os.path.join(settings.BASE_DIR, 'setup_done.flag')

    if os.path.exists(setup_flag):
        return HttpResponse("⚠️ Setup already completed. Access disabled.", status=403)

    try:
        call_command('migrate', interactive=False)
        call_command('initialize')

        with open(setup_flag, 'w') as f:
            f.write(f"Setup run by: {request.user.username}\n")

        return HttpResponse("""
            <html>
            <head>
                <meta http-equiv="refresh" content="3; url=/" />
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background-color: #f4f6f8;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .card {
                        background-color: #ffffff;
                        padding: 35px 45px;
                        border-radius: 12px;
                        box-shadow: 0 8px 18px rgba(0,0,0,0.08);
                        text-align: center;
                        max-width: 420px;
                        border-top: 6px solid #00c853;
                    }
                    .card img.logo {
                        width: 80px;
                        margin-bottom: 15px;
                    }
                    .check {
                        font-size: 48px;
                        color: #00c853;
                        animation: pop 0.3s ease-out;
                    }
                    .card h2 {
                        color: #2e7d32;
                        margin: 15px 0 5px;
                    }
                    .card p {
                        color: #555;
                        margin: 0;
                    }
                    @keyframes pop {
                        0% { transform: scale(0.5); opacity: 0; }
                        100% { transform: scale(1); opacity: 1; }
                    }
                </style>
            </head>
            <body>
                <div class="card">
                    <img src="/static/ClothStore.png" class="logo" alt="Logo">
                    <div class="check">✅</div>
                    <h2>Setup Completed</h2>
                    <p>Your store is ready to go!<br>Redirecting to home page...</p>
                </div>
            </body>
            </html>
        """)
    except Exception as e:
        return HttpResponse(f"❌ Error during setup: {str(e)}", status=500)

# Create your views here.


def home_page(request):
    all_data = Products.objects.all()
    context = {
        "info":all_data
    }
    return render(request,'index.html',context)

def get_all_cat(request):
    all_cat = Category.objects.all()
    cat_context = {
        'cat':all_cat
    }
    return render(request, 'includes/navbar.html',cat_context)

def product_detail(request,id):

    product_detail = Products.objects.get(id=id)
    context = {
        'product_info':product_detail
    }
    return render(request,'product_detail.html',context)

def category_data(request,id):
    category_id = id    # id fetch through url
    category = get_object_or_404(Category,id=category_id)   #logic to get ategory id or show 404 error
    products = Products.objects.filter(product_category=category_id)
    context = {
        'product_by_category':products
    }
    return render(request,'product_category_list.html',context)
    
def search_product(request):
    if request.method == "GET":
        searched_data = request.GET.get('search')
        if (len(searched_data)== 0):
            raise Http404("ENTER VALID INPUT")
        else:
            # result = Products.objects.filter(product_name__icontains=searched_data)
            query = (Q(product_name__icontains=searched_data) | Q (product_description__icontains=searched_data))
            result = Products.objects.filter(query)
            context={
                'object':result
            }
            return render(request,'search.html',context)
        


