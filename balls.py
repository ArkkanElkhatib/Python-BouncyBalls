import pygame
import random
import math

class Ball():

    def __init__(self, x_loc, y_loc): # Constructor class for the "Ball" object
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.direction = random.randrange(0, 360)
        self.color = [random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)]
        self.size = 20

    def move(self):
        path = math.radians(self.direction) # Converts the degrees path we have to an equivalent in radians
        self.x_loc += math.cos(path) # Math
        self.y_loc -= math.sin(path) # Math

    def draw(self, screen):
        # pygrame draws a circle to (screem we made, color list we defined, [x coordinate of ball, y coordinate of ball], radius equal to the size of the ball)
        pygame.draw.circle(screen, self.color, [int(self.x_loc), int(self.y_loc)], self.size)

    def changeColor(self, r, g, b): # Change color method takes in 3 values to change color of ball
        self.color = [r, g, b] # Sets the color list of the ball to be a list equal to the inputted rgb values

def main():
    ball_main = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # The original ball
    ball_list = [] # Constructing the array of all the balls
    ball_list.append(ball_main) # Adding the original ball to the list of balls

    exitFlag = False
    while not exitFlag:
        event = pygame.event.poll() # Checks if an even was performed
        if event.type == pygame.QUIT: # If the event performed was "clicking the red x to exit"
            exitFlag = True # Exit the program
        if event.type == pygame.MOUSEBUTTONDOWN: # If the event performed was "clicking the mouse"
            ball_list.append(Ball(event.pos[0], event.pos[1])) # Add a ball to the list with the mouse coordinates as the x_loc and y_loc
        # THE GAME
        for ball in ball_list: # Iterates through the list of ball
            ball.move() # Use the ball objects move function to move the ball slightly
            ball.draw(screen) # Draws the ball to the scren
        pygame.display.flip() # Update the display
        screen.fill((0, 0, 0)) # Covers all previous actions of the display

        # Loops through the list of ball, if a ball meets the condiiton of hitting an edge, reflects it
        for ball in ball_list:
            if (ball.x_loc < 0 + ball.size or ball.x_loc > SCREEN_WIDTH - ball.size): # If ball hits left or right
                if (ball.x_loc < 0 + ball.size): # If ball hits left
                    ball.changeColor(0, 0, 255)  # Change the color to blue
                else:                            # If ball hits right
                    ball.changeColor(255, 0, 0)  # Change the color to red
                ball.direction = 180 - ball.direction # Direction change for left and right
            elif (ball.y_loc < 0 + ball.size or ball.y_loc > SCREEN_HEIGHT - ball.size): # If ball hits top or bot
                if (ball.y_loc < 0 + ball.size): # If ball hits top
                    ball.changeColor(0, 255, 0)  # Change the color to green
                else:                            # If ball hits bot
                    ball.changeColor(255, 0, 255)# Change the color to purple

                ball.direction = 360 - ball.direction # Direction change for top and bottom

SCREEN_WIDTH = 800 # The intended width of the screen
SCREEN_HEIGHT = 600 # The intended height of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # Creates the screen using the pre-set width and height we have defined
main()
