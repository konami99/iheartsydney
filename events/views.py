from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import sys
from eventfeed import EventFeed

def index(request):
	ef = EventFeed()
	feed = ef.get_feed()
	return render_to_response('index.html', {'feed': feed})