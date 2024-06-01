from django.http import HttpResponse

def home(req):
  return HttpResponse("<h1>This is home</h1><br><h2>Django app developed by moin khan.</h2>")


def contact(req):
  return HttpResponse("<h1>This is contact page</h1>");