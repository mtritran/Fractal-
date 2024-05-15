import subprocess
import tkinter as tk

root = tk.Tk()
root.title("Fractal Viewer")

label = tk.Label(root, text="Chọn hình học fractal để xem:")
label.pack()

def run_mandelbrot_program():
    subprocess.run(["python", "mandelbrot.py"])

def run_juliaset_program():
    subprocess.run(["python", "juliaset.py"])

def run_tree_program():
    subprocess.run(["python", "tree.py"])

def run_kocksnowflake_program():
    subprocess.run(["python", "kocksnowflake.py"])

def run_dragonCurve_program():
    subprocess.run(["python", "dragonCurve.py"])

def run_sierpinskiTriangle_program():
    subprocess.run(["python", "sierpinskiTriangle.py"])

def run_analyzer_program():
    subprocess.run(["python", "analyzer.py"])    

btn_mandelbrot = tk.Button(root, text="Mandelbrot", command=run_mandelbrot_program)
btn_mandelbrot.pack()

btn_julia = tk.Button(root, text="Julia", command=run_juliaset_program)
btn_julia.pack()

btn_fractaltree = tk.Button(root, text="Fractal Tree", command=run_tree_program)
btn_fractaltree.pack()

btn_kochsnowflake = tk.Button(root, text="Koch SnowFlake", command=run_kocksnowflake_program)
btn_kochsnowflake.pack()

btn_dragonCurve = tk.Button(root, text="Dragon Curve", command=run_dragonCurve_program)
btn_dragonCurve.pack()

btn_sierpinskiTriangle = tk.Button(root, text="Sierpinski Triangle", command=run_sierpinskiTriangle_program)
btn_sierpinskiTriangle.pack()

btn_analyzer = tk.Button(root, text="Analysis", command=run_analyzer_program)
btn_analyzer.pack()

root.mainloop()
