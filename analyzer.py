import subprocess
import tkinter as tk
from tkinter import simpledialog
from PIL import Image

class FractalAnalysis:
    def __init__(self, image_filename):
        self.fractal_image = Image.open(image_filename).convert("RGB")

    def calculate_perimeter(self):
        width, height = self.fractal_image.size
        perimeter = 0
        for x in range(width):
            for y in range(height):
                if 0 < x < width - 1 and 0 < y < height - 1:
                    if self.fractal_image.getpixel((x, y)) != (0, 0, 0):
                        neighbors = [
                            self.fractal_image.getpixel((x+1, y)),
                            self.fractal_image.getpixel((x-1, y)),
                            self.fractal_image.getpixel((x, y+1)),
                            self.fractal_image.getpixel((x, y-1))
                        ]
                        if (0, 0, 0) in neighbors:
                            perimeter += 1
        return perimeter

    def calculate_area(self):
        width, height = self.fractal_image.size
        area = 0
        for x in range(width):
            for y in range(height):
                if 0 < x < width - 1 and 0 < y < height - 1:
                    if self.fractal_image.getpixel((x, y)) != (0, 0, 0):
                        area += 1
        return area

    def calculate_self_similarity_ratio(self):
        perimeter = self.calculate_perimeter()
        area = self.calculate_area()
        if area == 0:
            return 0
        else:
            return perimeter / area

def run_analyzer_program():
    image_filename = simpledialog.askstring("Enter Image Filename", "Enter the filename of the fractal image:")
    if image_filename:
        if not image_filename.endswith(".png"):
            image_filename += ".png"
        
        fractal_analyzer = FractalAnalysis(image_filename)
        perimeter = fractal_analyzer.calculate_perimeter()
        area = fractal_analyzer.calculate_area()
        ratio = fractal_analyzer.calculate_self_similarity_ratio()
        print("Image:", image_filename)
        print("Perimeter:", perimeter)
        print("Area:", area)
        print("Self-similarity ratio:", ratio)


run_analyzer_program()

