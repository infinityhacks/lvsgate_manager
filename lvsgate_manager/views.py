import functools

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect 

def permission_required(fn):
  @functools.wraps(fn) 
  def need_login(request, *args, **kwargs):
    if request.user.is_authenticated():     
      return fn(request, *args, **kwargs)
    else:
      return HttpResponseRedirect("accounts/login/")
  return need_login

@permission_required
def home(request):
  return render_to_response("index.html")

@permission_required
def list_vs(request):
  return render_to_response("vs.html", {'title': 'Virtual server'})
 

def add_vs(request):
  pass

def del_vs(request):
  pass

def list_localaddress(request):
  pass

def add_localaddress(request):
  pass

def del_localaddress(request):
  pass
