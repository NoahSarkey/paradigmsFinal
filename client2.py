#!/usr/bin/env python2.7

from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

# Sam Mustipher and Noah Sarkey
# Import a library of functions called 'pygame'
import pygame
import sys
import os
import time
from math import pi
                

class ClientConnection(Protocol):
	#def __init__(self):
	#	print "in init"
	def connectionMade(self):
		print "data written"
		self.transport.write("Connect")
	def dataReceived(self, data):
		print data

class ClientConnectionFactory(ClientFactory):
	def __init__(self):
		self.conn = ClientConnection()
	def buildProtocol(self, addr):
		return self.conn

if __name__ == '__main__':
	reactor.connectTCP('noahs-mbp.dhcp.nd.edu', 40100, ClientConnectionFactory())
	reactor.run()
