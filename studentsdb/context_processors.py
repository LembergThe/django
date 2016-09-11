from .settings import PORTAL_URL

def students_proc(request):
    print(request)
    return {'PORTAL_URL': PORTAL_URL}