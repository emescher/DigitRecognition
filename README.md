# DigitRecognition
## Goal of the Project
The goal of this project is to take a hand-drawn digit, preprocess it, and use a trained neural network to recognize which digit (0–9) the user drew. The project demonstrates image preprocessing, neural network training, and how a user-generated sketch can be converted into a format compatible with MNIST-style digit classifiers.

## How to Run the Code
1. Open the Final Code folder in this Github Repository.
2. Open google colab and create a new notebook.
3. Paste all the code from the FinalMainCode file into a cell.
4. Download the handwritten.keras file, and add it to the files int the new notebook.
5. Create a new folder called "digits" in the new notebook.
6. Run the code.
7. The output will be the UI, or there will be a link to open a new tab with just that UI.
8. Draw a digit on the sketchpad.
9. Press the "Save Digit" button to store the drawing. The saved image is automatically processed (grayscale → binarized → cropped → resized → padded).
10. You can press "Clear Canvas" to clear the canvas and you can save as many digits as you want.
11. Once done click the "Predict All Saved Digits" button.
13. The processed 28×28 images are fed into the trained neural network.
14. The predicted digit and confidence score are displayed on the right.
15. The "Clear Saved Digits" button clears all the saved digits. 

## Requirements / Dependencies
- Python 3  
- NumPy (manipulates arrays)
- TensorFlow/Keras (creates/runs the trained nerual network)
- PIL (image processing)
- ImageOps (padding and centering image) 
- Matplotlib (for visualizing processed images in the model creation code)
- os (file detection)
- cv2 (loads PNG)
- Gradio (Creates user interface)
Dependencies os, numpy, gradio, PIL, and tensorflow must be installed before running the main program.

## Approach / Methodology

### **Image Preprocessing**
The user’s drawing is first converted from the sketchpad into a NumPy array.  
The image then goes through the following steps:
1. Converted to grayscale  
2. Binarized (digit becomes dark, background becomes light)  
3. Cropped using a bounding box to isolate the digit  
4. Resized so the longest side is 20 pixels  
5. Padded to 28×28 pixels to match MNIST format  
6. Normalized and reshaped for use in the neural network  

### **Neural Network Model Creation**
The neural network model was built using TensorFlow/Keras and trained on the MNIST dataset.  
The model includes:
- A flatten layer that converts the 28×28 image into a 784-element vector  
- Two hidden layers with 128 nuerons each (Dense) with ReLU activation to introduce non-linearity  
- An output layer with 10 neurons (one per digit) and softmax activation  

The model was compiled with:
- **Loss:** Categorical cross-entropy  
- **Optimizer:** Adam  
- **Metrics:** Accuracy  

The network was trained for multiple epochs with mini-batches, allowing the weights to gradually adjust using gradient descent and backpropagation. After training, the model was saved and loaded during prediction.

## Results / Outputs / Demo
The program outputs:
- The predicted digits (0–9)  
- The confidence scores of the predictions

Example:
<img width="3194" height="1718" alt="Screenshot 2025-12-04 234828" src="https://github.com/user-attachments/assets/175faa75-b713-4722-820a-fb79c3559065" />
