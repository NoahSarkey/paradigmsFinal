# Sam Mustipher and Noah Sarkey
# Import a library of functions called 'pygame'
import pygame
import sys
import os
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

class Player2(object):
    def __init__(self, gs):
        self.gs = gs

    def drawX(self, centerx, centery):
        pygame.draw.line(self.gs.screen, RED, (centerx - 50, centery - 50), (centerx + 50, centery + 50), 2)
        pygame.draw.line(self.gs.screen, RED, (centerx - 50, centery + 50), (centerx + 50, centery - 50), 2)

class Boxes(object):
    def __init__(self, gs):
        self.gs = gs
        self.boxes = []
        
        # Initializing List of Rects to be used for collision

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
        def main(self):
                # Initialize the game engine
                pygame.init()
                self.turn = 1
                
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
                 
                pygame.display.set_caption("Tic Tac Toe")
                self.myTiles = Boxes(self)
                self.player1 = Player1(self)
                self.player2 = Player2(self)

                #Loop until the user clicks the close button.
                done = False
                clock = pygame.time.Clock()
                self.board_to_check = [[0]*3 for _ in range(3)]
                self.screen.fill(WHITE)
                 
                while not done:
                 
                    # This limits the while loop to a max of 10 times per second.
                    # Leave this out and we will use all CPU we can.
                    clock.tick(10)
                     
                    for event in pygame.event.get(): # User did something
                        if event.type == pygame.QUIT: # If user clicked close
                            done=True # Flag that we are done so we exit this loop
                        elif event.type == pygame.MOUSEMOTION:
                            pos = pygame.mouse.get_pos()
                            if self.turn == 1:
                                print ("hover x")
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            for box in self.myTiles.boxes:
                                tempRect = pygame.Rect(box)
                                if tempRect.collidepoint(pos[0], pos[1]):
                                    xPosition = pos[0] / 200
                                    yPosition = pos[1] / 200
                                    xPosition = int(xPosition)
                                    yPosition = int(yPosition)
                                    # print("HERE ARE THE VALUES: ", xPosition, " ", yPosition)
                                    if self.board_to_check[xPosition][yPosition] == 0:
                                        if self.turn == 1:
                                            self.player1.drawO(tempRect.centerx, tempRect.centery)
                                            self.board_to_check[xPosition][yPosition] = 1
                                            self.turn = 2
                                        else:
                                            self.player2.drawX(tempRect.centerx, tempRect.centery)
                                            self.board_to_check[xPosition][yPosition] = 2
                                            self.turn = 1
                                        # pygame.draw.circle(self.screen, (250,250,250), (tempRect.centerx, tempRect.centery), 10)
                    
                    for box in self.myTiles.boxes:
                        pygame.draw.rect(self.screen, BLACK, box, 2)
                    
                    for box in myTiles.boxes:
                        pygame.draw.rect(screen, BLACK, box, 2)
                   
                    if checkWin() != 0:
                        print("PLAYER ", checkWin(), " WINS!")

                    # Go ahead and update the screen with what we've drawn.
                    # This MUST happen after all the other drawing commands.
                    pygame.display.flip()
                 
                # Be IDLE friendly
                pygame.quit()

        def checkWin(self):
                # Checks Column
                i = 0
                j = 0
                while j < 3:
                    kill = 0
                    sum = 0
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
                j = 0
                while i < 3:
                    kill = 0
                    sum = 0
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
                while k < 3:
                    sum = 0
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
                kill = 0
                while k >= 0:
                    sum = 0
                    if self.board_to_check[k][k] == 0:
                        kill = 1
                    sum = sum + self.board_to_check[k][k]
                    k = k - 1
                    if kill == 0 and (sum == 3 or sum == 6):
                        if sum == 3:
                            print("Player 1 WIN!")
                            return 1
                        else:
                            print("Player 2 WIN!")
                            return 2
                return 0	# nobody has won yet
                
if __name__ == '__main__':
        Game = Board()
        Game.main()
