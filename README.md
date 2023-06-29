# Face Recognition Project

This project is a simple face recognition application implemented in Python using OpenCV library.

## Requirements

- OpenCV (cv2)
- Python pickle module

## Project Description

The application uses the Local Binary Patterns Histogram (LBPH) face recognizer in OpenCV for face recognition. It first opens the webcam and starts capturing video frames. Then, it uses Haar cascade to detect faces in the frames. The Haar cascade is pre-trained on face data. For each detected face, it recognizes the face using the LBPH face recognizer and prints the label of the recognized face.

## How to run the project

1. Install the necessary Python modules using pip:
    ```
    pip install opencv-python
    ```

2. Clone this repository:
    ```
    git clone https://github.com/your-github-username/face-recognition
    
    ```

3. Navigate to the project directory:

4. Run the code.py file:
    ```
    python code.py
    ```

## Important Note

This project requires the following files:

- The trained LBPH face recognizer model: 'trainer.yml'
- The pickle file containing the face labels: 'labels.pickle'
- Haarcascades XML file: 'haarcascade_frontalface_alt2.xml'

These files should be placed in the same directory as the Python script.

## Usage

Start the application. It will open a new window with the video feed from your webcam. When the application recognizes a face, it will draw a rectangle around the face and print the name of the person (if recognized) at the top left of the rectangle. Press 'q' to quit the application.

## Contributions

Feel free to submit pull requests, create issues or share this repository.

