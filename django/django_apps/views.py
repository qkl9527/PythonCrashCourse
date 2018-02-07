from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
	return render(request, 'django_apps/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	content = {'topics': topics}
	return render(request, 'django_apps/topics.html', content)

def topic(request, id):
	topic = Topic.objects.get(id=id)
	entries = topic.entry_set.order_by('-date_added')
	content = {'topic': topic, 'entries': entries}
	return render(request, 'django_apps/topic.html', content)
