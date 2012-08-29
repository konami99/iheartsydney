import feedparser
import sys

class EventFeed:
	
	def get_feed(self):
		f = feedparser.parse('http://whatson.cityofsydney.nsw.gov.au/events/today.rss')
		return f