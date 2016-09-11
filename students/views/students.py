from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

# Create your views here.
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/piv.png'},
    )
    return render(request, 'students/students_list.html', {
        'students' : students
    })

def student_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>delete student %s</h1>' % sid)

def institute(request, id):
    return HttpResponse('<h1>Institute %s</h1>' % id)

def department(request, id):
    return HttpResponse('<h1>Department %s</h1>' % id)