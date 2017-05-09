#!/usr/bin/env python2.7

from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
# Sam Mustipher and Noah Sarkey
# Import a library of functions called 'pygame'
import pygame
import sys
import os
import time
from math import pi

class ServerConnection(Protocol):
    def connectionMade(self):
        print "here 3"
        self.transport.write("connecting")
    def dataReceived(self, data):
        #print "here 4"
        print data

class ServerConnectionFactory(Factory):
    def __init__(self):
        self.connection = ServerConnection()
    def buildProtocol(self, addr):
        print "here"
        return self.connection
            
if __name__ == '__main__':
    reactor.listenTCP(40100, ServerConnectionFactory())
    reactor.run()
