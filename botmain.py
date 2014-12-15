import socket 
import re
import simplejson
import urllib
import urllib2

url = "https://www.virustotal.com/vtapi/v2/url/report"
server = "server"
channel = "#channel"
botnick = "botnick"

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) #connect to server using 6667
ircsock.send(u'NICK %s\n' % (botnick))#user auth
ircsock.send(u'USER %s bla %s :%s\n' % (botnick, server, botnick)) 

def ping():
	ircsock.send("PONG :pong\n")

def sendmsg(chan, msg):
	ircsock.send("PRIVMSG "+chan+" :" + msg +"\n")

def joinchan(chan):
	ircsock.send("JOIN " + chan +"\n")

def extracturl(msg):
	url = re.search("(?P<url>https?://[^\s]+)", msg)
	if url is not None: 
    		return url.group("url")
	else:
		return False
	

joinchan(channel)

while True:	
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip('\n\r')
	
	if extracturl(ircmsg) != False:
		link = extracturl(ircmsg)
		parameters = {"resource": link,
			      "apikey": "virus total api key"}
		data = urllib.urlencode(parameters)
		req = urllib2.Request(url, data) 
		response = urllib2.urlopen(req)
		json = response.read()
		response_dict = simplejson.loads(json)
		positives = response_dict.get('positives')
		
	print(ircmsg)
	if ircmsg.find("PING :") != -1:	#respond to server pings
		ping()
