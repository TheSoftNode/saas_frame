from django.shortcuts import render
from django.conf import settings

from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    # Check if the user is authenticated, and if so, print their first name to the console (for debugging purposes)
    if request.user.is_authenticated:
        print(request.user.first_name)
    
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    # Query all PageVisit entries
    qs = PageVisit.objects.all()
    
    # Filter PageVisit entries specific to the current page path
    page_qs = PageVisit.objects.filter(path=request.path)
    
    # Calculate the percentage of visits to this page compared to all visits
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    
    my_title = "My Page"
    html_template = "home.html"
    
    # Context data to pass to the template
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),  # Number of visits to this specific page
        "percent": percent,                   # Percentage of this page's visits compared to all page visits
        "total_visit_count": qs.count(),       # Total number of visits to all pages
    }
    
    # Create a new PageVisit entry for the current page visit
    PageVisit.objects.create(path=request.path)
    
    return render(request, html_template, my_context)
