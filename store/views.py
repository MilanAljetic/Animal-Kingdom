from django.shortcuts import get_object_or_404, render

from .models import Animal, Category


def all_animals(request):
    animals = Animal.objects.all()
    cat = Category.objects.all()
    return render(request, 'store/home.html', {'animals': animals, 'cat':cat})


def animal_detail(request, slug):
    animal = get_object_or_404(Animal, slug=slug, in_stock=True)
    return render(request, 'store/animals/detail.html', {'animal':animal})
     

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    animals = Animal.objects.filter(category=category)
    cat = Category.objects.all()
    return render(request, 'store/animals/category.html', {'category':category, 'animals':animals, 'cat':cat})