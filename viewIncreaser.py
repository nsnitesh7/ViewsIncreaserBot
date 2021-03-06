import requests
import subprocess
import json
import sys
import thread
import time
import random

numberOfViewers = 4
proxylist = []

def getURL(): # Get tokens
	return "http://www.twitch.tv/buttonboy13"

def build(): # Builds a set of tokens, aka viewers
	global numberOfSockets
	global numberOfViewers
	while True:
		if numberOfSockets < numberOfViewers:
			numberOfSockets += 1
			print ("Building viewers " + str(numberOfSockets) + "/" + str(numberOfViewers))
			urls.append(getURL())

def view(proxy,url): # Opens connections to send views
	while True:
		startmillis = int(round(time.time() * 1000))

		
		#print("Proxy Lenght is: "+ str(proxylist.__len__()))
		#randomnumber = random.randint(0, proxylist.__len__()-1)

		#currentrpoxy = proxylist[randomnumber]
		proxies = {
  			"http": "http://"+proxy
		}

		try:
			requests.head(url, proxies = proxies)
			#requests.head(url)
		except Exception:
			#print("Removing Wrong Proxy: "+proxy)
			pass
			#proxylist.remove(currentrpoxy)
		time.sleep(0.1)
		endmillis = int(round(time.time() * 1000))
		print("Time took for request: "+str((endmillis-startmillis)/1000))		
if __name__ == '__main__':
	proxylist = [line.strip() for line in open('proxylistMain.txt')]
	url = getURL()
	print(proxylist)
	for i in range(numberOfViewers):
		proxy = proxylist[i]
		print("starting thread with proxy: "+proxy)
		thread.start_new_thread(view, (proxy,url))
	while True:
		time.sleep(0)
