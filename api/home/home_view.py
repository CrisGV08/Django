from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_const import LOGING_URL
@login_required(login_url=LOGING_URL)
# Create your views here.
def home_view(request):
    template_view = "home.html"
    
    return render(request, template_name=template_view)

@login_required(login_url=LOGING_URL)
def home_shop(request):
    template_view = "shop.html"
    
    return render(request, template_name=template_view)
@login_required(login_url=LOGING_URL)
def home_about(request):
    
    template_view = "about.html"
    return render(request, template_name=template_view)
@login_required(login_url=LOGING_URL)
def home_services(request):
    template_view = "services.html"
    
    return render(request, template_name=template_view)
@login_required(login_url=LOGING_URL)
def home_blog(request):
    template_view = "blog.html"
    
    return render(request, template_name=template_view)
@login_required(login_url=LOGING_URL)
def home_contact(request):
    template_view = "contact.html"
    
    return render(request, template_name=template_view)
@login_required(login_url=LOGING_URL)
def home_cart(request):
    template_view = "cart.html"
    
    return render(request, template_name=template_view)
@login_required(login_url=LOGING_URL)
def home_checkout(request):
    template_view = "checkout.html"
    
    return render(request, template_name=template_view)
@login_required(login_url=LOGING_URL)
def home_thankyou (request):
    template_view = "thankyou.html"
    
    return render(request, template_name=template_view)