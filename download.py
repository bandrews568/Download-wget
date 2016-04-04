#!/usr/bin/python
#Script to download mp3 files off a website

import urllib2
import wget 
import os
import datetime
import glob

from bs4 import BeautifulSoup

#Get links of the files to download 
url = 'http://www.wallyswebpages.net/moorzy/Rock/'
req = urllib2.Request(url)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page.read(), 'html.parser')
link_list = []


for link in soup.find_all("a"):
	link_list.append("http://www.wallyswebpages.net/moorzy/Rock/" + link.get('href'))

if len(link_list) >= 1:
	print "Found {} links.".format(len(link_list)), \
		  "Started download at: {}".format(datetime.datetime.now())
else:
	print "No links found to download"

#Use wget module to download links
os.chdir('C:\\Users\\Brandon\\Music') 

download_count = 0
failed_count = 0

if len(link_list) >= 1:
	for link in link_list:
		try:
			wget.download(link)
			download_count += 1
			print "Downloaded: {}/{}".format(download_count, len(link_list)) 
			#Rename the files to take out '%20' 
			for name in glob.glob('*.mp3'):
				new_filename = name.replace("%20","")
				os.rename(name, new_filename)
		except IOError:
			failed_count += 1
			print "File not downloaded.\n Link: {}".format(link)
			continue 

	if download_count == len(link_list):
		print "Finished downloading at: {}".format(datetime.datetime.now()), \
			  "Successfully downloaded all {} files".format(len(link_list))

	else:
		failed_count = len(link_list) - len(failed_count)
		print "Finished downloading at: {}".format(datetime.datetime.now()), \
		      "Failed to download {} files".format(failed_count)