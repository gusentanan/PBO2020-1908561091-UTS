from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import StudentForm
from .models import Student
# Create your views here.

class StudentList(ListView):
	template_name = 'StudentList.html'
	context_object_name = 'student_list'

	def get_queryset(self):
		return Student.objects.all()


def student_form(request, id=0):
	if request.method == 'GET':
		if id == 0:
			form = StudentForm()
		else:
			student = Student.objects.get(pk=id)
			form = StudentForm(instance=student)
		return render(request, 'StudentForm.html', {'form': form})
	else:
		if id == 0:
			form = StudentForm(request.POST)
		else:
			student = Student.objects.get(pk=id)
			form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
		return redirect('/student/list')



def student_delete(request, id):
	student = Student.objects.get(pk=id)
	student.delete()
	return redirect('/student/list')
