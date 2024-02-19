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
    """
    Preprocesses an image by resizing it to the target size and converting it to a float32 array.

    Args:
        image (numpy.ndarray): The input image.
        target_size (tuple): The desired size of the image after resizing. Default is (224, 224).

    Returns:
        numpy.ndarray: The preprocessed image as a float32 array.
    """
    image = cv2.resize(image, target_size)
    if image.shape[2] != 3:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image = image.astype('float32') / 255.0
    return np.expand_dims(image, axis=0)

def update_frame():
    """
    Function to update the frame in the video stream and perform inference on the frame.

    This function reads a frame from the video stream, converts it to RGB format, and performs inference on the frame
    using a pre-trained neural network. The predicted class label is displayed on the frame. The updated frame is then
    displayed in a GUI window.

    Args:
        None

    Returns:
        None
    """
    global frame, start_inference, predictions, root, lbl_video, arrow_images
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
                class_label = class_labels.get(most_common, "Unknown")
                cv2.putText(frame, f"Class: {class_label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                # Display the arrow image in a label below the video frame
                arrow_label_image = arrow_images[class_label]
                lbl_arrow.config(image=arrow_label_image)
                lbl_arrow.image = arrow_label_image

                # Adjust the position of the arrow label based on the class
                if class_label == "Organic":
                    lbl_arrow.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
                elif class_label == "Inorganic":
                    lbl_arrow.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
                elif class_label == "B3":
                    lbl_arrow.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
            else:
                lbl_arrow.place_forget()  # Hide the arrow if there's no prediction yet
                cv2.putText(frame, "Analyzing...", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        frame_image = Image.fromarray(frame)
        frame_image = ImageTk.PhotoImage(frame_image)
        lbl_video.configure(image=frame_image)
        lbl_video.image = frame_image
    root.after(10, update_frame)

def start_stop_inference():
    """
    Toggles the start_inference flag and updates the button text accordingly.
    
    This function is responsible for toggling the start_inference flag, which controls whether the inference process should start or stop. 
    When the flag is toggled, the button text is updated accordingly to reflect the current state of the inference process.
    """
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
model_path = '/home/orangepi/Desktop/update4/model.onnx'
if not os.path.isfile(model_path):
    raise Exception(f"Model file {model_path} not found. Please check the file path.")
net = cv2.dnn.readNetFromONNX(model_path)

# GUI setup
'''
GUI Setup
Describe the overall setup of the graphical user interface.
Discuss each component of the GUI, including the video label, arrow label, and the start/stop button.
Note/Section: Loading Arrow Images
Explain how the arrow images are loaded and potentially resized for display.
Note/Section: Creating Labels for Arrow Images
Discuss the creation of labels for displaying the arrow images on the GUI.
Note/Section: Releasing Resources
Describe the cleanup process, including releasing the webcam and closing the GUI windows.
'''
root = tk.Tk()
root.title("Waste Classification")
root.configure(bg='#1E1E1E')  # Set the background color

# Bind Escape key to exit full-screen
root.bind('<Escape>', toggle_fullscreen)

style = ttk.Style()
style.theme_use('clam')

frame = None
start_inference = False
predictions = deque()

lbl_video = tk.Label(root, bg='#1E1E1E')  # Set the video label background color
lbl_video.pack(pady=20)

# Load arrow images for each class label
arrow_images = {
    "Organic": ImageTk.PhotoImage(Image.open('organic_arrow.png').resize((150, 150))),
    "Inorganic": ImageTk.PhotoImage(Image.open('inorganic_arrow.png').resize((150, 150))),
    "B3": ImageTk.PhotoImage(Image.open('b3_arrow.png').resize((140 ,140)))
}

# Create a label for displaying arrow images
lbl_arrow = tk.Label(root, bg='#1E1E1E')  # Set the arrow label background color

btn_start = ttk.Button(root, text="Start Inference", command=start_stop_inference)
btn_start.pack(pady=10)

root.after(10, update_frame)
root.mainloop()

# Release resources
cap.release()
cv2.destroyAllWindows()
