#!/usr/bin/env python2.7

from twisted.protocols.basic import LineReceiver
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

WHITE = (255,255,255)
RED = (255,0 ,0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
GREEN = (0,255,0)

# o's
class Player1(object):
    def __init__(self, gs):
        self.gs = gs

    def drawO(self, centerx, centery):
        pygame.draw.circle(self.gs.screen, BLUE, (centerx, centery), 50, 2 )

    def hoverO(self, centerx, centery):
        pygame.draw.circle(self.gs.screen, BLUE, (centerx, centery), 50, 2 )
        time.sleep(1)
        pygame.draw.circle(self.gs.screen, WHITE, (centerx, centery), 50, 2 )

# x's
class Player2(object):
    def __init__(self, gs):
        self.gs = gs

    def drawX(self, centerx, centery):
        pygame.draw.line(self.gs.screen, RED, (centerx - 50, centery - 50), (centerx + 50, centery + 50), 2)
        pygame.draw.line(self.gs.screen, RED, (centerx - 50, centery + 50), (centerx + 50, centery - 50), 2)

    def hoverX(self, centerx, centery):
        pygame.draw.line(self.gs.screen, RED, (centerx - 50, centery - 50), (centerx + 50, centery + 50), 2)
        pygame.draw.line(self.gs.screen, RED, (centerx - 50, centery + 50), (centerx + 50, centery - 50), 2)
        time.sleep(1)
        pygame.draw.line(self.gs.screen, WHITE, (centerx - 50, centery - 50), (centerx + 50, centery + 50), 2)
        pygame.draw.line(self.gs.screen, WHITE, (centerx - 50, centery + 50), (centerx + 50, centery - 50), 2)

class Boxes(object):
    def __init__(self, gs):
        self.gs = gs
        self.boxes = []

        # Initializing List of Rects to be used for collisis

        # Top Row Rects
        for i in range(3):
            self.boxes.append([i*200,0,200,200])
        # Middle Row Rects:
        for i in range(3):
            self.boxes.append([i*200,200,200,200])
        # Bottom Row Rects
        for i in range(3):
            self.boxes.append([i*200,400,200,200])

class Board:
	def __init__(self, conn):
		self.conn = conn

        def main(self):

                # Initialize the game engine
                pygame.init()
                pygame.font.init()
                myfont = pygame.font.SysFont('Comic Sans MS', 100)
                self.turn = 1
                self.xPositionInteger = 0
                self.yPositionInteger = 0
                '''
                # Define the colors we will use in RGB format
                BLACK = (  0,   0,   0)
                WHITE = (255, 255, 255)
                BLUE =  (  0,   0, 255)
                GREEN = (  0, 255,   0)
                RED =   (255,   0,   0)
                '''
                # Set the height and width of the screen
                self.size = [600, 600]
                self.screen = pygame.display.set_mode(self.size)
                self.surface = pygame.display.get_surface()

		# Initialize and instantiate classes
                pygame.display.set_caption("Tic Tac Toe Server")
                self.myTiles = Boxes(self)
                self.player1 = Player1(self)
                self.player2 = Player2(self)

                #Loop until the user clicks the close button.
                done = False
                clock = pygame.time.Clock()
                self.board_to_check =[[0]*3 for _ in range(3)]
                self.screen.fill(WHITE)

		# Create the looping call so it will work in twisted/pyagme
		lc = LoopingCall(self.game_loop)
		lc.start(1/60)

	def game_loop(self):

		    #print "CURRENT TURN IS: ", self.turn

		    # For copying over the other players moves
		    if self.turn == 2:
			newpos = [self.xPositionInteger, self.yPositionInteger]
			newpos[0] = int(self.xPositionInteger)
			newpos[1] = int(self.yPositionInteger)
			for box in self.myTiles.boxes:
			    tempRect = pygame.Rect(box)
			    for i in range(3):
				for j in range(3):
				    self.surface.fill(WHITE, box)
			    if tempRect.collidepoint(newpos[0], newpos[1]):
				self.surface.fill(RED, box)

		    if self.turn == 1:
		    	# For your own player (player1) moves
		    	for event in pygame.event.get(): # User did something
                            if event.type == pygame.QUIT: # If user clicked close
                            	done=True # Flag that we are done so we exit this loop
                            elif event.type == pygame.MOUSEMOTION or self.turn == 2:
                            	pos = pygame.mouse.get_pos()
			    	for box in self.myTiles.boxes:
                                    tempRect = pygame.Rect(box)

				    # Clear out the entire board (make the squares white)
				    for i in range(3):
				        for j in range(3):
					    if self.board_to_check[i][j] == 0:
					        self.surface.fill(WHITE, tempRect)
				    # Look to see if the collision point is a thing
                                    if tempRect.collidepoint(pos[0], pos[1]):
				        xPosition = pos[0]/200
                                        yPosition = pos[1]/200

                                        if self.turn == 1:
                                            self.xPositionInteger = int(xPosition)
                                            self.yPositionInteger = int(yPosition)

                                        #print self.xPositionInteger
                                        #print self.yPositionInteger

				        # Send data back to the client
                                        xx = "xx:"+str(pos[0])+"\n"
				        yy = "yy:"+str(pos[1])+"\n"

                                        self.conn.sendLine(xx)
                                        self.conn.sendLine(yy)

			    	        # Fill the colors in
                                        if self.turn == 1:
                                            self.surface.fill(BLUE, tempRect)
                                        else:
                                            self.surface.fill(RED, tempRect)
                                            #self.surface.fill(WHITE, tempRect)
                                            # self.player2.hoverX(tempRect.centerx, tempRect.centery)

			    # If player 1 clicks the mouse (follows same general format as above event)
                            elif event.type == pygame.MOUSEBUTTONDOWN or self.turn == 2:
                                pos = pygame.mouse.get_pos()
                                for box in self.myTiles.boxes:
                                    tempRect = pygame.Rect(box)
                                    if tempRect.collidepoint(pos[0], pos[1]):
                                        xPosition = pos[0] / 200
                                        yPosition = pos[1] / 200
                                        xPosition = int(xPosition)
                                        yPosition = int(yPosition)
				        if self.turn == 1:
					    clickedX = xPosition
					    clickedY = yPosition

                                        #print "HERE ARE THE VALUES of click: ", xPosition, " ", yPosition
                                        v = clickedX
                                        w = clickedY
                                        #if self.board_to_check[v][w] == 0:
					if self.turn == 1:
					    cX = "clickedXCoordinate:"+str(xPosition)+"\n"
					    cY = "clickedYCoordinate:"+str(yPosition)+"\n"
					    print cX, " ", cY
					    self.conn.sendLine(cX)
					    self.conn.sendLine(cY)

                                        self.surface.fill(WHITE, tempRect)
                                        if self.turn == 1:
                                            self.player1.drawO(tempRect.centerx, tempRect.centery)
                                            self.board_to_check[v][w] = 1
                                            self.turn = 2
                                        else:
                                            self.player2.drawX(tempRect.centerx, tempRect.centery)
                                            self.board_to_check[v][w] = 2
                                            self.turn = 1

					    # Send the data back to the client
                                        s = ""
            			        if self.turn == 2:
                        		    s = "turnchange:2\n"
                    		        else:
                        		    s = "turnchange:1\n"

            			        print "we are transporting ", s
                                        self.conn.sendLine(s)

                                        # pygame.draw.circle(self.screen, (250,250,250), (tempRect.centerx, tempRect.centery), 10)

                    for box in self.myTiles.boxes:
                        pygame.draw.rect(self.screen, BLACK, box, 2)

		    # This is where we would have added the functionality for the board
                    # go through board_to_check and draw O's or X's based on the value

                    #print("CHECK WIN? ", self.checkWin())
                    #print(self.board_to_check)
                    if self.checkWin() != 0:
                        # print("PLAYER ", self.checkWin(), " WINS!")
                        winner = "PLAYER" + str(self.checkWin()) + " WINS!"
                        if self.checkWin() == 1:
                            textsurface = myfont.render(winner, False, GREEN)
                            self.screen.fill(WHITE)
                            self.screen.blit(textsurface, (0,300))
                        else:
                            textsurface = myfont.render(winner, False, GREEN)
                            self.screen.fill(WHITE)
                            self.screen.blit(textsurface, (0,300))
                        done = True
                    # Go ahead and update the screen with what we've drawn.
                    # This MUST happen after all the other drawing commands.
                    pygame.display.flip()

	# Function for checking whether or not the user has won the game
	# Although this is not directly used in the final product, it is functional. This can be
	# seen in main.py

	# In addition, this game will come to an end once someone would have won; it just does not
	# display the markers to the two windows
        def checkWin(self):
                # Checks Column
                j = 0
                while j < 3:
                    kill = 0
                    sum = 0
                    i = 0
                    while i < 3:
                        if self.board_to_check[i][j] == 0:
                            kill = 1
                        sum = sum + self.board_to_check[i][j]
                        i = i + 1
                    if kill == 0 and (sum == 3 or sum == 6):
                        if sum == 3:
                            print("Player 1 WIN!")
                            return 1
                        else:
                            print("Player 2 WIN!")
                            return 2
                    j = j + 1

                # Checks Row
                i = 0
                while i < 3:
                    kill = 0
                    sum = 0
                    j = 0
                    while j < 3:
                        if self.board_to_check[i][j] == 0:
                            kill = 1
                        sum = sum + self.board_to_check[i][j]
                        j = j + 1
                    if kill == 0 and (sum == 3 or sum == 6):
                        if sum == 3:
                            print("Player 1 WIN!")
                            return 1
                        else:
                            print("Player 2 WIN!")
                            return 2
                    i = i + 1

                # Check Diagonals (Top left to bottom right)
                kill = 0
                k = 0
                sum = 0
                while k < 3:
                    if self.board_to_check[k][k] == 0:
                        kill = 1
                    sum = sum + self.board_to_check[k][k]
                    k = k + 1
                if kill == 0 and (sum == 3 or sum == 6):
                    if sum == 3:
                        print("Player 1 WIN!")
                        return 1
                    else:
                        print("Player 2 WIN!")
                        return 2

                # Check Diagonals (Bottom left to top right)
                k = 2
                w = 0
                kill = 0
                sum = 0
                while k >= 0:
                    if self.board_to_check[k][w] == 0:
                        kill = 1
                    sum = sum + self.board_to_check[k][w]
                    w = w + 1
                    k = k - 1
                if kill == 0 and (sum == 3 or sum == 6):
                    if sum == 3:
                        print("Player 1 WIN!")
                        return 1
                    else:
                        print("Player 2 WIN!")
                        return 2
                return 0	# nobody has won yet

class ServerConnection(LineReceiver):
	def __init__(self):
		self.delimiter = "\n"
		self.g = Board(self)

	def connectionMade(self):
		self.g.main()

	def lineReceived(self, line):
                data = line
                #print "Data being brought in from client: ", data

                data = data.split(':')
                if len(data) == 0:
                    print "no data"
                    return
                if data[0] == "turnchange":
		    self.g.turn = int(data[1])
                elif data[0] == "xx":
                    self.g.xPositionInteger = int(data[1])
                elif data[0] == "yy":
                    self.g.yPositionInteger = int(data[1])
		elif data[0] == "clickedXCoordinate":
		    self.g.clickedX = int(data[1])
		elif data[0] == "clickedYCoordinate":
		    self.g.clickedY = int(data[1])

class ServerConnectionFactory(Factory):
	def __init__(self):
		self.connection = ServerConnection()

	def buildProtocol(self, addr):
		return self.connection

if __name__ == '__main__':
	reactor.listenTCP(40098, ServerConnectionFactory())
	reactor.run()
