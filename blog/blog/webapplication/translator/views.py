from django.shortcuts import render
from .models import post
from django.views import generic
# Create your views here.
#def home(requests):
#   dest = post.objects.all()
#  return render(requests,'index.html',{'object':dest})

class BlogView(generic.DetailView): #detailed view is used when we need data from the database
    model = post
    template_name = 'index.html'

class main(generic.TemplateView): # template view is used when there is no connection between the template and the database
    template_name = 'main.html'

class about(generic.TemplateView):
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = post.objects.filter(status = 1).order_by('date_created')
    template_name = 'home.html'