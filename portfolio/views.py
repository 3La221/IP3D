from django.shortcuts import render
from .models import Project, Category
from .utils import add_portfolio_categories
from django.conf import settings
# Create your views here.


def home(request):
    categories = Category.objects.all()
    portfolio_items = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'categories': categories,
        'portfolio_items': portfolio_items,
        'MEDIA_URL': settings.MEDIA_URL
    })