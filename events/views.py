from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from xml.dom.minidom import parseString
from xml.dom import minidom
from eventfeed import EventFeed
from BeautifulSoup import BeautifulSoup
import simplejson as json, urllib, pprint
import feedparser
import pprint

def index(request):
	ef = EventFeed()
	feed = ef.get_feed()
		
	return render_to_response('index.html', {'feed': feed})
	
	
def detail(request, namespace):
	# select * from html where url="http://whatson.cityofsydney.nsw.gov.au/events/9201-pine-streets-term-3-art-workshops" and xpath='//*[@id="main"]'
	# http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D%22http%3A%2F%2Fwhatson.cityofsydney.nsw.gov.au%2Fevents%2F9201-pine-streets-term-3-art-workshops%22%20and%20xpath%3D'%2F%2F*%5B%40id%3D%22main%22%5D'&diagnostics=true
	# http://developer.yahoo.com/python/python-json.html
	# http://net.tutsplus.com/tutorials/javascript-ajax/how-to-build-an-rss-reader-with-jquery-mobile-2/
	# //*[@id="main"]/h1
	
	args = {'q':'select * from html where url="http://whatson.cityofsydney.nsw.gov.au/events/' + namespace + '" and xpath=\'//*[@id="main"]\''}
	
	
	#url = 'http://query.yahooapis.com/v1/public/yql' + '?' + urllib.urlencode(args)
	
	#url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D%22http%3A%2F%2Fwhatson.cityofsydney.nsw.gov.au%2Fevents%2F9201-pine-streets-term-3-art-workshops%22%20and%20xpath%3D'%2F%2F*%5B%40id%3D%22main%22%5D'"
	
	
	
	
	url = "http://query.yahooapis.com/v1/public/yql?" + urllib.urlencode(args)
	
	
	# print url
	
	# result = feedparser.parse("http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D%22http%3A%2F%2Fwhatson.cityofsydney.nsw.gov.au%2Fevents%2F9201-pine-streets-term-3-art-workshops%22%20and%20xpath%3D'%2F%2F*%5B%40id%3D%22main%22%5D'&diagnostics=false")
	
	#result = json.load(urllib.urlopen(url))["query"]["results"]
	#title = result["div"]["h1"]
	# detail = result["div"]["details"]
	# pprint.pprint(result["div"]["div"][1][2])
	
	xmldoc = BeautifulSoup(urllib.urlopen(url))
	
	title = xmldoc.query.results.h1.string
	des = xmldoc.query.results.findAll("div","description",limit=1)[0].p.string
	
	pprint.pprint(des)
	
	return render_to_response('detail.html', {'title': title, 'result': des})
	
	#return render_to_response('detail.html')