from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

# Create your views here.
def persons_list(request):
	persons = Person.objects.all() #select * from RESOURCE
	return render(request, 'person.html', {'persons':persons})


def aux_persons_new(request):
	if request.method == 'POST':
		form = PersonForm(request.POST, request.FILES)

		print("É POST")
		print("?:", form.is_valid())
		if form.is_valid():
			print("É VALIDO")
			form.save()
			
			redirect('person_list')

	else: #SE FOR GET, RETORNA UM FORM VAZIO
		form = PersonForm()

def persons_new(request):
	form = PersonForm(request.POST, request.FILES, None)

	if form.is_valid():
		print("É VALIDO")
		form.save()
			
		return redirect('person_list')

	print("RENDERIZOU O person_form.html")
	return render(request, 'person_form.html', {'form':form})

