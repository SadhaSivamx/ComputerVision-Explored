import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to find the corners of the largest contour
def find_corners(contour):
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4:
        return approx.reshape(-1, 2)
    return None

def choose_image():
    global image, img_path, src_points, NewOne, original_img_label, transformed_img

    img_path = filedialog.askopenfilename()
    if img_path:
        image = cv2.imread(img_path)
        image = cv2.resize(image, (500, 500))
        NewOne = image.copy()
        display_image(image, original_img_label)
        transformed_img = None

def perform_transformation():
    global image, src_points, NewOne, transformed_img, transformed_img_label

    if image is None:
        messagebox.showerror("Error", "No image selected!")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    cv2.drawContours(NewOne, [largest_contour], -1, (0, 255, 0), 2)
    Corners = find_corners(largest_contour)
    if Corners is None:
        messagebox.showerror("Error", "No quadrilateral found.")
        return

    src_points = np.float32(Corners.tolist())
    [cv2.circle(NewOne, tuple(map(int, _)), 5, (0, 0, 255), -1) for _ in src_points]
    maxx = max(src_points[:,0])
    maxy = max(src_points[:,1])
    dest_points = np.float32([[0, 0], [0, maxy], [maxx, maxy], [maxx, 0]])
    M = cv2.getPerspectiveTransform(src_points, dest_points)
    transformed_img = cv2.warpPerspective(image, M, (int(maxx), int(maxy)))
    display_image(transformed_img, transformed_img_label)

def display_image(img, label):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)
    label.config(image=img_tk)
    label.image = img_tk

def save_image():
    if transformed_img is None:
        messagebox.showerror("Error", "No transformed image to save!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    if save_path:
        cv2.imwrite(save_path, transformed_img)

def rotate_image():
    global transformed_img, transformed_img_label

    if transformed_img is None:
        messagebox.showerror("Error", "No transformed image to rotate!")
        return

    transformed_img = cv2.rotate(transformed_img, cv2.ROTATE_90_CLOCKWISE)
    display_image(transformed_img, transformed_img_label)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Perspective Transformation App")

# Initialize global variables
image = None
img_path = ""
src_points = None
NewOne = None
transformed_img = None

# Create buttons and image display panels
btn_choose_image = tk.Button(root, text="Choose Image", command=choose_image)
btn_choose_image.pack(side="top", fill="both", expand="yes", padx=10, pady=10)

btn_transform = tk.Button(root, text="Perform Transformation", command=perform_transformation)
btn_transform.pack(side="top", fill="both", expand="yes", padx=10, pady=10)

frame = tk.Frame(root)
frame.pack(side="bottom", fill="both", expand="yes", padx=10, pady=10)

original_img_label = tk.Label(frame)
original_img_label.pack(side="left", padx=10, pady=10)

transformed_img_label = tk.Label(frame)
transformed_img_label.pack(side="right", padx=10, pady=10)

# Create a frame for additional buttons on the right
right_frame = tk.Frame(frame)
right_frame.pack(side="right", padx=10, pady=10)

btn_save_image = tk.Button(right_frame, text="Save Image", command=save_image)
btn_save_image.pack(side="top", fill="both", expand="yes", padx=10, pady=5)

btn_rotate_image = tk.Button(right_frame, text="Rotate Image", command=rotate_image)
btn_rotate_image.pack(side="top", fill="both", expand="yes", padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
