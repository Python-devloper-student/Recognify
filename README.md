# Recognify
THIS code helps you make attendence system , face recogonizers and register users for you projects
# Face Attendance System

A face recognition attendance system built using Python, OpenCV, and DeepFace.
this i may take somtime at first use as it downloads the models and once initialized it will be fast

## Features

* Register new users using a webcam
* Detect faces in camera frames
* Recognize previously registered users
* Support for multiple faces in a frame
* Local storage of registered users

## Technologies Used

* Python
* OpenCV
* DeepFace
* pyttsx3

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Import the `Recon` class and create an instance:

```python
from Recognify import Recon

system = Recon(0)
```

Register a user:

```python
system.register("Divyanshu")
```

Scan for known users:

```python
system.scan()
```

## Current Status

Prototype Version 1

## Known Limitations

* Uses Haar Cascade face detection
* Stores user information in a text file
* No graphical user interface yet
* Recognition speed decreases as more users are added

## Future Improvements

* GUI application
* SQLite database support
* Faster face matching using embeddings
* Attendance reports
* Improved face detection models

## License

This project is open for learning and experimentation.
