from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

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

def group_journal(request, gid):
    return HttpResponse('<h1>Group Journal %s</h1>' % gid)