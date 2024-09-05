from .models import Category

def add_portfolio_categories():
    categories = [
        "3D Work",
        "Cadre Personnalisé",
        "Conception 3D Stand de Foire",
        "Création Logos",
        "Impression Numérique - UV et Sérigraphie",
        "Panneaux Publicitaire",
        "PLV Publicité sur lieu de vente",
        "Stand d'éxposition"
    ]

    for category_name in categories:
        Category.objects.create(name=category_name, order=categories.index(category_name) + 1)