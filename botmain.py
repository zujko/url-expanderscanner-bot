import socket 
import re

server = "chat.freenode.net"
channel = "#bot"
botnick = "mrcoolman"

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
		url = extracturlVerify(url)
	 
	print(ircmsg)
	if ircmsg.find("PING :") != -1:	#respond to server pings
		ping()
