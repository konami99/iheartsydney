from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from xml.dom.minidom import parseString
from eventfeed import EventFeed
import simplejson as json, urllib, pprint
import feedparser

def index(request):
	ef = EventFeed()
	feed = ef.get_feed()
		
	return render_to_response('index.html', {'feed': feed})
	
	
def detail(request, namespace):
	# select * from html where url="http://whatson.cityofsydney.nsw.gov.au/events/9201-pine-streets-term-3-art-workshops" and xpath='//*[@id="main"]'
	# http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D%22http%3A%2F%2Fwhatson.cityofsydney.nsw.gov.au%2Fevents%2F9201-pine-streets-term-3-art-workshops%22%20and%20xpath%3D'%2F%2F*%5B%40id%3D%22main%22%5D'&diagnostics=true
	# http://developer.yahoo.com/python/python-json.html
	# http://net.tutsplus.com/tutorials/javascript-ajax/how-to-build-an-rss-reader-with-jquery-mobile-2/
	
	# args = {'q':'select * from html where url="http://whatson.cityofsydney.nsw.gov.au/events/' + namespace + '" and xpath=\'//*[@id="main"]\'',
	#		'diagnostics':'false'
	#		}
	
	# url = 'http://query.yahooapis.com/v1/public/yql' + '?' + urllib.urlencode(args)
	# result = feedparser.parse("http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D%22http%3A%2F%2Fwhatson.cityofsydney.nsw.gov.au%2Fevents%2F9201-pine-streets-term-3-art-workshops%22%20and%20xpath%3D'%2F%2F*%5B%40id%3D%22main%22%5D'&diagnostics=false")
	
	result = json.load(urllib.urlopen("http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D%22http%3A%2F%2Fwhatson.cityofsydney.nsw.gov.au%2Fevents%2F9201-pine-streets-term-3-art-workshops%22%20and%20xpath%3D'%2F%2F*%5B%40id%3D%22main%22%5D'&format=json"))
	print result
	
	return render_to_response('detail.html')