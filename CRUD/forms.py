from django import forms

from .models import Student

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('name', 'number')
		labels = {
			'name' : 'Nama Mahasiswa',
			'number' : 'NIM',
			
		}

	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		self.fields['number'].required = False
		


