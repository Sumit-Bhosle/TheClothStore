from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models import Products,Category
from django.db.models import Q

# Temperory migration for RENDER HOSTING

from django.core.management import call_command

def setup(request):
    call_command('migrate')
    import accounts.management.commands.initialize as initialize
    initialize.run()
    return HttpResponse("Migration & Initial Data Loaded ✅")




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
        


