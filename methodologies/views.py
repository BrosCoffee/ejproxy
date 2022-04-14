from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostListView(ListView):
    paginate_by = 6
    model = Post
    template_name = 'methodologies/post_list.html'

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        object_list = self.model.objects.all().order_by('-date_added')
        object_list = object_list.filter(title__icontains=title)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
