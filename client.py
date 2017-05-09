#!/usr/bin/env python2.7

from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor













class ClientConnection(Protocol):
	def __init__(self, addr):
		#print "in init"
		self.addr = addr

	def connectionMade(self):
		#print "data written"
		self.transport.write("Connect")

	def dataReceived(self):
		return 0

class ClientConnectionFactory(ClientFactory):
	def buildProtocol(self, addr):
		#print "here"
		return ClientConnection(addr)

reactor.connectTCP("ash.campus.nd.edu", 40098, ClientConnectionFactory())
#print "running"
reactor.run()
