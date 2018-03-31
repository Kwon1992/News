from django.shortcuts import render
from .models import ArticleEntries

# Create your views here.
def displayList(request):
    queryset = ArticleEntries.objects.order_by('-id')[:1000] # LIMIT 1000, ORDER BY id (Descendencing)
    context = {
        'Title' : 'news DB',
        'object_list' : queryset,
    }
    return render(request, 'news/index.html', context)
