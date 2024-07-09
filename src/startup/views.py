from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits
def home_page_view(requests):

    query_set = PageVisits.objects.all()
    PageVisits.objects.create()



    context = {
        "page_title":"SaaS",
        "page_visit_count" : query_set.count()

    }
    return render(requests, 'index.html', context)
    