#!/usr/bin/python
# Python example
# http://jasminsms.com
import urllib2
import urllib

# Send an SMS-MT and request terminal level acknowledgement callback to http://myserver/acknowledgement
params = {'username':'xxxxx', 'password':'xxxxx', 'from':'label','to':'0744xxxxxx', 'content':'Como estas?', 
          'coding':'2', 'priority':'1', 'tags':'1223', 
          'dlr-url':'http://myserver/acknowledgement', 'dlr-level':2}
urllib2.urlopen("http://localhost:1401/send?%s" % urllib.urlencode(params)).read()