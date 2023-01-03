from django.shortcuts import render;
from django.http import HttpResponse;


def f1(request):
	return HttpResponse("<h1>Hello from DemoApp1 f1()</h1><hr />");
def f2(request):
	return HttpResponse("<h1>Hello from DemoApp1 f2()</h1><hr />");

def f11(request):
	return HttpResponse("<h1>Hello from DemoApp1 f11()</h1><hr />");

def f22(request):
	return HttpResponse("<h1>Hello from DemoApp1 f22()</h1><hr />");

