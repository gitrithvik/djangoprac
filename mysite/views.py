from django.http import HttpResponse, Http404
import datetime

def hello(request):
	return HttpResponse("Hello World")

def current_time(request):
	now = datetime.datetime.now()
	html = "<html><body>The time now is %s.</body.</html>" %now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	total = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>The time after {} hours is {}</body></html>".format(offset,total)
	return HttpResponse(html)

