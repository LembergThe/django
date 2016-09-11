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

# Views for Groups
def groups_list(request):
    #print(request)
    groups = (
        {
        'id': 1,
        'name': 'KN-40',
        'institute': 'IKNI',
        'department': 'ASU',
        'students': 27,
        'success': 1
        },
        {
            'id': 2,
            'name': u'KN-41',
            'institute': u'IKNI',
            'department': u'ASU',
            'students': 27,
            'success': 2
        }
    )
    return render(request, 'students/groups_list.html', {
        'groups': groups
    })

def group(request, gid):
    return HttpResponse('<h1>Group %s </h1>'  % gid)

def group_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def group_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def group_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

def institute(request, id):
    return HttpResponse('<h1>Institute %s</h1>' % id)

def department(request, id):
    return HttpResponse('<h1>Department %s</h1>' % id)

def group_journal(request, gid):
    return HttpResponse('<h1>Group Journal %s</h1>' % gid)
