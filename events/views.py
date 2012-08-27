from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import sys
from eventfeed import EventFeed

def index(request):
	e = EventFeed()
	e.get_feed()