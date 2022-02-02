#!/usr/bin/python3

import urllib.request

from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, user_agent='wswp' ,num_retries=2):
	print("Downloading!!",url)
	request=urllib.request.Request(url)
	request.add_header('User-agent',user_agent)
	try:
		html= urllib.request.urlopen(url).read()
	except (URLError, HTTPError, ContentTooShortError) as e:
		print('Download error: ',e.reason)
		html=None
# Some times we encounter code error like 404, 503 to simplify Any code 4xx is an error in request we made
# Code 5xx is an error of server ..we can try no of times to overcome such code error
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				#recursively retry 5xx Http errors
				return download(url,num_retries - 1)
	print(html)		
	return html

download("http://www.meetup.com")  # Cant find a webpage which allows download will on some tryhackme Machine

# http://httpstat.us/500 can be use to test the 500 error

# Sometimes we encounter 403 Forbidden because some sites prevent using python urllib .3x user agent
# So we need to change the default user agent with wswp(Web Scarping with Python )
# try meetup.com which gave 403 error to deafult user agent
