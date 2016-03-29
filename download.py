#!/usr/bin/python
#Script to download mp3 files off a website
from bs4 import BeautifulSoup
import urllib2, wget, os, datetime, glob

#Get links of the files to download 
url = 'http://www.wallyswebpages.net/moorzy/Rock/'
req = urllib2.Request(url)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page.read(), 'html.parser')
link_list = []


for link in soup.find_all("a"):
	link_list.append("http://www.wallyswebpages.net/moorzy/Rock/" + link.get('href'))

print "Found {} links.".format(len(link_list))  

print "Started download at: {}".format(str(datetime.datetime.now())) 

#Use wget module to download links
os.chdir('C:\\Users\\Brandon\\Music') 
download_count = 0

for link in link_list:
	wget.download(link)
	download_count += 1
	print "Downloaded: {}/{}".format(download_count, len(link_list)) 
	#Rename the files 
	for name in glob.glob('*.mp3'):
		new_filename = name.replace("%20","")
		os.rename(name, new_filename)
if download_count == len(link_list):
	print "Finished downloading at: {}".format(str(datetime.datetime.now())) 








