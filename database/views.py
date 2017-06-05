from django.shortcuts import render
from .models import Fights
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    queryResultsList = Fights.objects.all()
    paginator = Paginator(queryResultsList, 100)

    page = request.GET.get('page')
    try:
        queryResults = paginator.page(page)
    except PageNotAnInteger:
        queryResults = paginator.page(1)
    except EmptyPage:
        queryResults = pageinator.page(paginator.num_pages)

    return render(request, 'database/index.html', {'queryResults':queryResults})
