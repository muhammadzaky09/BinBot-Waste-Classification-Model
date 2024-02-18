import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from collections import deque

# Class labels mapping
class_labels = {0: "Organic", 1: "Inorganic", 2: "B3"}

def preprocess_image(image, target_size=(224, 224)):
    image = cv2.resize(image, target_size)
    if image.shape[2] != 3:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image = image.astype('float32') / 255.0
    return np.expand_dims(image, axis=0)

def update_frame():
    global frame, start_inference, predictions, root, lbl_video
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if start_inference:
            cv2.putText(frame, "Loading...", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            blob = preprocess_image(frame)
            net.setInput(blob)
            output = net.forward()
            predictions.append(np.argmax(output[0]))
            if len(predictions) > 5:
                predictions.popleft()
                most_common = max(set(predictions), key=predictions.count)
                class_label = class_labels.get(most_common, "Unknown")  # Get the label from the dictionary
                cv2.putText(frame, f"Class: {class_label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            else:
                cv2.putText(frame, "Analyzing...", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        frame_image = Image.fromarray(frame)
        frame_image = ImageTk.PhotoImage(frame_image)
        lbl_video.configure(image=frame_image)
        lbl_video.image = frame_image
    root.after(10, update_frame)

def start_stop_inference():
    global start_inference, predictions
    start_inference = not start_inference
    if start_inference:
        predictions = deque()
        btn_start['text'] = 'Stop Inference'
    else:
        btn_start['text'] = 'Start Inference'

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Initialize the webcam and model
cap = cv2.VideoCapture(0)
model_path = 'model.onnx'
if not os.path.isfile(model_path):
    raise Exception(f"Model file {model_path} not found. Please check the file path.")
net = cv2.dnn.readNetFromONNX(model_path)

# GUI setup
root = tk.Tk()
root.title("Waste Classification")
root.attributes('-fullscreen', True)  # Set full-screen

# Bind Escape key to exit full-screen
root.bind('<Escape>', toggle_fullscreen)

style = ttk.Style()
style.theme_use('clam')

frame = None
start_inference = False
predictions = deque()

lbl_video = tk.Label(root, bg='#333')
lbl_video.pack(pady=20)

btn_start = ttk.Button(root, text="Start Inference", command=start_stop_inference)
btn_start.pack(pady=10)

root.after(10, update_frame)
root.mainloop()

# Release resources
cap.release()
cv2.destroyAllWindows()
