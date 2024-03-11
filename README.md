# Donut.py-Clone
In this repository, you will find a clone of "Donut.c" created by Andy Sloane.

This project was implemented using Python and Pygame for the GUI.

My understanding of the project (What I learned):

In this project, I was able to create a 3D illusion in a 2D space using rotation matrices and trigonometry.

From my understanding of the project, you can create any 3-dimensional shape you would like, but I wanted to implement the torus shape. 

To break this project down into simpler terms, I created a screen using pygame that was 1200x1000 res. Within this screen, I created a grid of separate screens that would each represent an ASCII character value that would be 
shuffled using an input buffer. 

I created this grid of screens by calculating the center of the main pygame window and creating an area of about 600x500. Within this grid, each "screen" would contain a 20x20 pixel rectangle that would be the container that would house a list of chars
from darkest luminance to brightest. Within each screen I calculated the center position where the character would be rendered and also passed the list of character values that would be shuffled through on each iteration.

Now comes the really tricky part that, to be honest, I am still trying to fully grasp (for I have not learned this in my linear algebra class yet). 

What needed to be done was to understand rotational matrices as well as a little bit of calculus. 

First, I needed to understand how a 3D object would be perceived by the human eye on a 2d surface. Andy Sloane provided a great diagram in his blog about how he created "Donut.c" (https://www.a1k0n.net/2011/07/20/donut-math.html), but to summarize, we need to project each x y z coordinate z units away from
the users view. This is done by first calculating the depth of the user's vision to the screen (pygame window) and then, secondly, calculating the main depth from the user's view into the center of the torus points (z1 and z2).

Once I had the depth calculated using trigonometry I had to figure out how to first draw the torus in 2D onto the screen. I did this by using 2 for loops, the outer loop iterating from 0 to 2pi representing the crossectional area of the torus if we were to take a slice out of it, which creates the circle shape, and then the inner loop iterating
from 0 to 2pi representing the angle of revolution around a y-axis which would also give the torus its girth/depth. From here, I was able to calculate the x and y values of the cross-sectional area before rotating in order to give me starting points of where the torus would begin to be drawn. Then I calculated the 3d coordinates after rotating using the
rotational matrices equation.

Once I had the torus drawn in 2D, I was able to then calculate the x and y projection by using the viewer's depth distance and the screen width.

I know this wasn't the best explanation, but I really enjoyed learning about a new topic and tried my best to understand the concepts at hand; while there are still some linear Algebra concepts I am still struggling with overall, I was able to learn more about python as a language, as well as, learning more about pygame and GUI (which I really wanted to learn).




