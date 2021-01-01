from django.shortcuts import render
from .models import Person

# Create your views here.
def persons_list(request):
	persons = Person.objects.all() #select * from RESOURCE
	return render(request, 'person.html', {'persons':persons})


def persons_new(request):
	pass