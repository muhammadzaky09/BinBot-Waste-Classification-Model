# BinBot - GDSC UGM Solution Challenge 2024 Entry

Welcome to the repository for BinBot, one of two repositories submitted for the Google Solution Challenge 2024 by our team from Google Developer Student Clubs at Universitas Gadjah Mada.

## Team Members

- Muhammad Zaky Firdaus - Hacker/Programmer
- Muhammad Alfi Ramadhan - Hacker/Programmer
- Aryanta Adri Herlangga - Hustler/Project Manager
- Adila Rahma Widja - Hipster/UI/UX Designer

## About BinBot

BinBot is an innovative solution designed to classify waste materials efficiently, promoting environmental sustainability. Utilizing machine learning and computer vision, BinBot can identify different types of waste and suggest the correct bin for disposal. This project aims to tackle *Goal 12: Responsible Consumption and Production* and to streamline waste management as well as support recycling efforts. <br>
The model is derived from pretrained DenseNet-121 model, a balanced solution between performance and accuracy. During training, the model is able to reach more than 90% in both validation and training accuracy.

## Requirements

To run BinBot, the following hardware components are required:

- Orange Pi 3B
- Webcam compatible with Orange Pi
- Monitor with HDMI input

## Dataset Obtained
### Overview
![image](https://github.com/muhammadzaky09/BinBot-Waste-Classification-Model/assets/88239996/0ca8c14b-4b13-436f-99d1-afc3e5a76687)
![image](https://github.com/muhammadzaky09/BinBot-Waste-Classification-Model/assets/88239996/2afa7253-df0f-47d7-8c78-f1689018f35a)
```bash
organic count:  13966
inorganic count:  11111
b3 count:  10822
```
### Links
- Garbage Classification - Kaggle https://www.kaggle.com/datasets/mostafaabla/garbage-classification
- TrashBox - GitHub https://github.com/nikhilvenkatkumsetty/TrashBox
- Waste Pictures (Medicine Waste) - Kaggle https://www.kaggle.com/datasets/wangziang/waste-pictures

## Tutorial

### Setting Up the Hardware

1. Connect the Orange Pi to the monitor using an HDMI cable.
2. Connect the webcam to the Orange Pi via a USB port.

### Configuring the Orange Pi

Follow the detailed instructions for setting up the Orange Pi 3B [here](http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_3B#Introduction_to_the_use_of_the_development_board).

### Installing Prerequisites

On the Orange Pi, open a terminal and execute the following commands:

```bash
# Update the package list
sudo apt-get update

# Upgrade existing packages
sudo apt-get upgrade

# Install Python3
sudo apt-get install python3

# Install pip, the Python package installer
sudo apt-get install python3-pip

# Install OpenCV for Python
pip3 install opencv-python
```
### Running the Script
Navigate to 'Classification Script' directory containing 'classification3_with_images.py' and run the following command: <br>
Make sure 'model.onnx' is located on the same directory with the script.
```bash
python3 classification3_with_images.py
```
