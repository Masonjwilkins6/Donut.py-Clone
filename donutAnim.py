import pygame # used to create GUI
import os # use 
from math import cos, sin # need for rotation matrix around centeral axis

# colors (for pygame window)
WHITE =  (255,255,255)
BLACK = (0,0,0)

#center the users window, by accessing enviornment variable to change behavior of running processes
os.environ["SDL_VIDEO_CENTERED"] = "1"

# set pygame window resoltuion
RESOLUTION = WIDTH, HEIGHT = 1200, 1000

# set FPS
FPS = 60

# list of chars to represent luminace from darkest to lightest
chars = ".,-~:;=!*#$@"

# spacing in between each pixel "screen" 
pixel_width = 20
pixel_height = 20

# counters for pixel "screen" positions
x_pixel = 0
y_pixel = 0

# size of "screen" grid containg each individual pixel screen (centering it techincally becasue you are / big screen by 2) -> therfore calculates new screen area
screen_width = WIDTH // pixel_width
screen_height = HEIGHT // pixel_height
screen_size = screen_width * screen_height
















# speed of rotation around the x and z axis
A, B =  0, 0

# donut paramters
# r1 => small circle radius that is being rotated around centeral y axis
# r2  => distance from centeral axis to small circle center
R1 = 10
R2 = 20

# screen depth parameters
# k2 => distance from user eye to the screen (estimate)
# k1 => distance from user eye to center of "donut" (small circle)
K2 = 200
K1  = screen_height * K2 * 3 / (8 * (R1 + R2))

# initalize density of cross section for torus
# theta = angle of "donut" cross section ------------ (width of torus)
# phi = angle of "donut" rotation around centeral axis through the center of the torus -------- (girth of torus)
theta_spacing = 7
phi_spacing = 2














# initalize pygame
pygame.init()

# create screen || initate clock to track frame rate
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
pygame.display.set_caption("Illusion")

# set pygame window font
font = pygame.font.SysFont('Arial', 20, bold=True)

# display text in pygame window
# char = text to display
# x & y to center
def text_display(char, x, y):

    # text to render
    text = font.render(str(char), True, WHITE)

    # create retangle containg text to render
    text_rect = text.get_rect(center=(x,y))

    # draw the text using blit
    screen.blit(text, text_rect)

# initalize count variable for list of different chars to shuffle through
k = 0

running = True
while running:
    # set maximum frame rate during runtime to fps
    clock.tick(FPS)

    # fill screen
    screen.fill(BLACK)

    # place holder image
    output = [' '] * screen_size

    # z axis buffer 
    zbuffer = [0] * screen_size
   
    # creating donut (628 represents 2pi) <= cross section for torus is a circle, 2pi = 1 full rev = a cirlce ------ theta and phi spacing represent the density of points within cross section
    for theta in range(0, 628, theta_spacing): # theta goes around the cross sectional area of "donut" (torus) from 0 to 2pi = 1 revolution
        for phi in range(0, 628, phi_spacing):  # phi goes around the center of revolution of the "donut" (torus) (which creates the donut shape) from 0 to 2pi = 1 revolutuion
            
            # x and z values 
            cosA = cos(A)
            sinA = sin(A)
            cosB = cos(B)
            sinB = sin(B)

            # x and y values of theta and phi
            cosTheta = cos(theta)
            sinTheta = sin(theta)
            cosPhi = cos(phi)
            sinPhi = sin(phi)

            # calculate x and y coordinates of phi and theta before rotaion around centeral axis
            circleX = R2 + R1 * cosTheta # (point on the outer edge of circle cross section)
            circleY = R1 * sinTheta # ()

            # 3D (x,y,z) coordinates after rotation (axis are flipped in order to compensate for the rotation around the main axis) (use rotation matrix equations)
            x = circleX * (cosB * cosPhi + sinA * sinB * sinPhi) - circleY * cosA * sinB
            y = circleX * (sinB * cosPhi - sinA * cosB * sinPhi) + circleY * cosA * cosB
            z = K2 + cosA * circleX * sinPhi + circleY * sinA
            ooz = 1 / z # to track which points are closer to screen

            # x and y projection
            # simulates the effect of perspective
            xP = int(screen_width / 2 + K1 * ooz * x)
            yP = int(screen_width / 2 - K1 * ooz * y)

            # position of chars dependent on depth
            position = xP + screen_width * yP

            #luminance (ranging from -sqrt(2) to sqrt(2))
            L = cosPhi * cosTheta * sinB - cosA * cosTheta * sinPhi - sinA * sinTheta + cosB * (
                        cosA * sinTheta - cosTheta * sinA * sinPhi)

            if ooz > zbuffer[position]:
                zbuffer[position] = ooz  # larger ooz means the pixel is closer to the viewer than what's already plotted
                luminance_index = int(L * 8)  # we multiply by 8 to get luminance_index range 0..11 (8 * sqrt(2) = 11)
                output[position] = chars[luminance_index if luminance_index > 0 else 0]


    # iterate over grid of screens
    # outerloop (vertical screens)
    for i in range(screen_height):
        y_pixel += pixel_height
        # inner loop (horizontal screens)
        for j in range(screen_width):
            x_pixel += pixel_width
            # shuffle through "output" which is list of chars to display within each "screen"
            text_display(output[k], x_pixel, y_pixel)
            k += 1 
        x_pixel = 0
    y_pixel = 0
    k = 0

    A += 0.2
    B += 0.1

    pygame.display.update()

    for event in pygame.event.get():
        # quit window logic
        if event.type == pygame.QUIT:
            running = False
        # if escape pressed, quit window
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

