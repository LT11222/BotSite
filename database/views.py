from django.shortcuts import render
from .models import Fights, Characters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, 'database/index.html')

def fights(request):
    queryResultsList = Fights.objects.all().order_by('matchid')
    paginator = Paginator(queryResultsList, 100)

    page = request.GET.get('page')
    try:
        queryResults = paginator.page(page)
    except PageNotAnInteger:
        queryResults = paginator.page(1)
    except EmptyPage:
        queryResults = pageinator.page(paginator.num_pages)

    return render(request, 'database/fights.html', {'queryResults':queryResults, 'end':paginator.num_pages})

def characters(request):
    queryResultsList = Characters.objects.all().order_by('name')
    print(queryResultsList[0])
    paginator = Paginator(queryResultsList, 100)

    page = request.GET.get('page')
    try:
        queryResults = paginator.page(page)
    except PageNotAnInteger:
        queryResults = paginator.page(1)
    except EmptyPage:
        queryResults = pageinator.page(paginator.num_pages)

    return render(request, 'database/characters.html', {'queryResults':queryResults, 'end':paginator.num_pages})
