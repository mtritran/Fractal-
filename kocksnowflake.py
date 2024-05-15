import pygame
from turtle import Turtle, Screen
from PIL import Image, ImageOps
import io

# Function to save the image
def save_image(surface, filename):
    pygame.image.save(surface, filename)

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    screen = Screen()  
    screen.bgcolor("black")
    screen.title("Koch Snowflake")
    screen.delay(5)  

    # Pygame setup
    pygame.init()

    # Turtle setup
    fractal = Turtle()  
    fractal.color("blue")
    fractal.speed("fastest")

    fractal.penup()
    fractal.goto(-150, 90)
    fractal.pendown()

    for _ in range(3):
        koch_snowflake(fractal, 4, 300)
        fractal.right(120)

    # Hide the turtle cursor
    fractal.hideturtle()

    # Save the image
    image_data = screen.getcanvas().postscript(colormode='color')
    image = Image.open(io.BytesIO(image_data.encode('utf-8')))
    pygame_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
    save_image(pygame_image, "Snow.png")

    screen.mainloop()

if __name__ == "__main__":
    main()
