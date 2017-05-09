#!/usr/bin/env python2.7

from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor












class ServerConnection(Protocol):
	def __init__(self, addr):
		#print "here 2"
		self.addr = addr
	def connectionMade(self):
		#print "here 3"
		return 0
	def dataReceived(self, data):
		#print "here 4"
		print data

class ServerConnectionFactory(Factory):
	def buildProtocol(self, addr):
		#print"here"
		return ServerConnection(addr)

reactor.listenTCP(40098, ServerConnectionFactory())
#print "running"
reactor.run()
