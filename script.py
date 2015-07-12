import requests

proxylist = [line.strip() for line in open('proxylist.txt')]

proxyDict = {  
              "http" : "http://167.114.71.58:3128",
              "https" : "https://167.114.71.58:3128"
            }

url = "http://niteshsinghaliitg.wordpress.com/"

for p in proxylist:
	try:
		proxyDict = {"http" : "http://"+p,"https" : "https://"+p}
		r = requests.get(url, proxies=proxyDict, timeout=3)
		print p
	except:
		pass
