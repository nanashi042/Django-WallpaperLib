from django.shortcuts import render
from utils.scrape import img

def home(request):
    search_term = request.GET.get('search', 'anime')  # Default to 'anime' if no search term is provided
    list_of_links = img(search_term)
    return render(request, "home.html", {"imgs": list_of_links})
