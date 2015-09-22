import functools

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect 

from lvsgate_manager import models

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
  return render_to_response("index.html",
         {'title': 'LVSGate manager'})

@permission_required
def list_vs(request):
  vs_list = models.VirtualServer.objects.all() 
  return render_to_response("vs.html",
        {'title': 'Virtual server', 'vs_list': vs_list})
 

def add_vs(request):
  title = "Add virtual server"
  return render_to_response("vs_edit.html",
        {'title': title, 'rise_nums': range(2, 11),
         'fall_nums': range(2, 11),})

def del_vs(request):
  pass

def list_localaddress(request):
  pass

def add_localaddress(request):
  pass

def del_localaddress(request):
  pass
