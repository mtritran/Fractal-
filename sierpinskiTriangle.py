import turtle
import pygame
from PIL import Image, ImageOps
import io

# Function to save the image
def save_image(surface, filename):
    pygame.image.save(surface, filename)

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(points, degree, my_turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree-1, my_turtle)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree-1, my_turtle)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree-1, my_turtle)

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()

    # Pygame setup
    pygame.init()

    # Screen setup
    screen = turtle.Screen()
    screen.title("Sierpinski Triangle")
    screen.delay(10)
    
    # Set the background color to black
    my_win.bgcolor("white")
    
    my_points = [[-100, -50], [0, 100], [100, -50]]
    
    # Increase the size of the triangle by scaling the coordinates
    scaled_points = [[point[0]*2, point[1]*2] for point in my_points]
    
    sierpinski(scaled_points, 4, my_turtle)
    
    # Save the image
    image_data = screen.getcanvas().postscript(colormode='color')
    image = Image.open(io.BytesIO(image_data.encode('utf-8')))
    pygame_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
    save_image(pygame_image, "Sierpinski.png")

    my_win.exitonclick()

if __name__ == "__main__":
    main()
