#!/usr/bin/python

import difflib, os, re, time, urllib2

#Change this to the URL you want to monitor
URL_TO_MONITOR = "https://www.example.com/page"
#File name to save previous content.
PREVIOUS_CONTENT = "website_content.txt" 
DELAY_TIME = 10 # seconds

#Scrape webpage
request_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
request = urllib2.Request(URL_TO_MONITOR, headers=request_headers)
response = urllib2.urlopen(request).read()

#Remove unwanted HTML
items_clean = re.compile('<script.*?</script>|<meta.*?/>|<meta.*?>|return .*?;')
processed_response_html = re.sub(items_clean, '', response)

#Create the previous_content.txt if it doesn't exist
if not os.path.exists(PREVIOUS_CONTENT):
    open(PREVIOUS_CONTENT, 'w+').close()

filehandle = open(PREVIOUS_CONTENT, 'r')
previous_response_html = filehandle.read() 
filehandle.close()

#Perform difference checking
if processed_response_html == previous_response_html:
    pass #No changes, do nothing.
else:
    print("URGENT!", URL_TO_MONITOR, "HAS CHANGED!")
    filehandle = open(PREVIOUS_CONTENT, 'w')
    filehandle.write(processed_response_html)
    filehandle.close()
