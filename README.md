# BinBot - GDSC UGM Solution Challenge 2024 Entry

Welcome to the repository for BinBot, one of two repositories submitted for the Google Solution Challenge 2024 by our team from Google Developer Student Clubs at Universitas Gadjah Mada.

## Team Members

- Muhammad Zaky Firdaus - Hacker/Programmer
- Muhammad Alfi Ramadhan - Hacker/Programmer
- Aryanta Adri Herlangga - Hustler/Project Manager
- Adila Rahma Widja - Hipster/UI/UX Designer

## About BinBot

BinBot is an innovative solution designed to classify waste materials efficiently, promoting environmental sustainability. Utilizing machine learning and computer vision, BinBot can identify different types of waste and suggest the correct bin for disposal. This project aims to tackle *Goal 12: Responsible Consumption and Production* and to streamline waste management as well as support recycling efforts. 

## Requirements

To run BinBot, the following hardware components are required:

- Orange Pi 3B
- Webcam compatible with Orange Pi
- Monitor with HDMI input

## Tutorial

### Setting Up the Hardware

1. Connect the Orange Pi to the monitor using an HDMI cable.
2. Connect the webcam to the Orange Pi via a USB port.

### Configuring the Orange Pi

Follow the detailed instructions for setting up the Orange Pi 3B [here](http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_3B#Introduction_to_the_use_of_the_development_board).

### Software Installation

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
### Software Installation
Navigate to the directory containing 'classification3_with_images.py' and run the following command:
```bash
python3 classification3_with_images.py
```
