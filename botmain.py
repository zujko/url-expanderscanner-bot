import socket 



server = "server"
channel = "#channel"
botnick = "botnick"

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) #connect to server using 6667
ircsock.send(u'NICK %s\n' % (botnick))#user auth
ircsock.send(u'USER %s %s :%s\n' % (botnick, server, botnick)) 

def ping():
	ircsock.send("PONG :pong\n")

def sendmsg(chan, msg):
	ircsock.send("PRIVMSG "+chan+" :" + msg +"\n")

def joinchan(chan):
	ircsock.send("JOIN " + chan +"\n")


joinchan(channel)

while True:	
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip('\n\r')
	
