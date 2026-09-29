# 🫁 Pneumonia Detection from Chest X-Ray Images

A deep learning-based **Pneumonia Detection System** that uses a Convolutional Neural Network (CNN) to classify chest X-ray images into **Pneumonia** and **Normal** categories.

The project demonstrates the application of **Computer Vision and Deep Learning** for automated medical image classification.

---

## 📌 Project Overview

Pneumonia is a serious respiratory infection that can cause abnormalities in lung X-ray images. This project uses a **Convolutional Neural Network (CNN)** to learn visual patterns from chest X-ray images and predict whether an image indicates pneumonia.

The model takes a chest X-ray image as input, processes it through multiple convolutional and pooling layers, and produces a binary prediction:

* 🟢 **Normal**
* 🔴 **Pneumonia**

> **Note:** This project is intended for educational and research purposes and should not be used as a substitute for professional medical diagnosis.

---

## 🚀 Features

* 🩻 Chest X-ray image classification
* 🧠 CNN-based deep learning model
* 🔍 Automatic feature extraction
* 🔄 Image resizing and preprocessing
* 🎯 Binary classification: Normal vs Pneumonia
* 🛡️ Dropout regularization to reduce overfitting
* ⚡ Lightweight CNN architecture suitable for experimentation
* 📊 Model evaluation using classification metrics

---

## 🏗️ CNN Architecture

The model uses a sequential CNN architecture:

```text
Input Image
150 × 150 × 3
       │
       ▼
Conv2D (32 filters, ReLU)
       │
       ▼
MaxPooling2D (2 × 2)
       │
       ▼
Conv2D (64 filters, ReLU)
       │
       ▼
MaxPooling2D (2 × 2)
       │
       ▼
Conv2D (128 filters, ReLU)
       │
       ▼
MaxPooling2D (2 × 2)
       │
       ▼
Flatten
       │
       ▼
Dense (128, ReLU)
       │
       ▼
Dropout (0.5)
       │
       ▼
Dense (1, Sigmoid)
       │
       ▼
Normal / Pneumonia
```

### Why CNN?

CNNs are particularly effective for image classification because convolutional layers can automatically learn spatial features such as:

1. Edges and basic patterns
2. Textures and shapes
3. Complex visual patterns
4. Higher-level abnormalities

This eliminates the need to manually engineer image features.

---

## 🔬 Data Preprocessing

Before training, chest X-ray images are preprocessed to provide consistent input to the CNN.

### Processing steps

* Images are resized to **150 × 150 pixels**
* Images are represented using **3 RGB channels**
* Pixel values are normalized before training
* Images are divided into training and evaluation datasets
* Labels are assigned to the corresponding classes

### Classes

| Class     | Description                   |
| --------- | ----------------------------- |
| Normal    | Chest X-ray without pneumonia |
| Pneumonia | Chest X-ray showing pneumonia |

---

## 🧠 Model Details

### Convolutional Layers

Three convolutional blocks are used:

```text
32 filters → 64 filters → 128 filters
```

The increasing number of filters allows the network to learn increasingly complex visual representations.

### Activation Function

**ReLU (Rectified Linear Unit)** is used in the hidden layers.

```text
ReLU(x) = max(0, x)
```

It introduces non-linearity and helps the network learn complex patterns.

### Pooling

**MaxPooling2D (2×2)** reduces the spatial dimensions of feature maps while retaining important features.

### Dropout

A dropout rate of **0.5** is applied before the final classification layer.

This randomly deactivates neurons during training and helps reduce overfitting.

### Output Layer

The final layer contains one neuron with a **Sigmoid activation function**.

```text
Sigmoid(x) = 1 / (1 + e⁻ˣ)
```

The output represents the probability of the image belonging to the positive class.

---

## 📊 Prediction Logic

The model produces a probability between 0 and 1.

```python
if prediction > 0.5:
    result = "Pneumonia"
else:
    result = "Normal"
```

---

## 🛠️ Technologies Used

* **Python**
* **TensorFlow / Keras**
* **NumPy**
* **Matplotlib**
* **OpenCV / PIL**
* **Jupyter Notebook / Google Colab**

---

## 📂 Project Structure

```text
Pneumonia-Detection/
│
├── dataset/
│   ├── train/
│   │   ├── NORMAL/
│   │   └── PNEUMONIA/
│   │
│   └── test/
│       ├── NORMAL/
│       └── PNEUMONIA/
│
├── notebooks/
│   └── pneumonia_detection.ipynb
│
├── models/
│   └── pneumonia_cnn.h5
│
├── images/
│   └── sample_predictions/
│
├── requirements.txt
├── README.md
└── .gitignore
```

> Dataset files are not included in this repository if they exceed GitHub's storage limits.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Pneumonia-Detection.git
```

Navigate to the project:

```bash
cd Pneumonia-Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1. Open the notebook

```bash
jupyter notebook
```

or open the notebook using **Google Colab**.

### 2. Prepare the dataset

Place the dataset according to the expected directory structure.

### 3. Train the model

Run the notebook cells sequentially to:

* Load the dataset
* Preprocess images
* Create the CNN
* Train the model
* Evaluate performance
* Generate predictions

### 4. Make a prediction

Provide a chest X-ray image to the trained model.

The model returns:

```text
Prediction: Pneumonia
```

or

```text
Prediction: Normal
```

---

## 📈 Model Evaluation

The model can be evaluated using metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Example evaluation:

```python
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))
```

For medical image classification, **recall/sensitivity is particularly important**, because incorrectly classifying a pneumonia case as normal can be more consequential than a false positive.

---

## 📉 Training Visualization

Training and validation performance can be visualized using accuracy and loss curves.

```python
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Training', 'Validation'])
plt.show()
```

Similarly, loss can be plotted to identify potential overfitting.

---

## 🔍 Key Learning Outcomes

Through this project, I worked with:

* Convolutional Neural Networks
* Image preprocessing
* Computer vision
* Binary image classification
* Feature extraction using CNNs
* ReLU and Sigmoid activation functions
* Max pooling
* Dropout regularization
* Model evaluation
* Training and validation analysis

---

## 🔮 Future Improvements

Potential improvements include:

* Transfer learning using **ResNet, VGG16, EfficientNet or MobileNet**
* Data augmentation
* Hyperparameter optimization
* Class imbalance handling
* Explainable AI using **Grad-CAM**
* Web deployment using **Flask or Streamlit**
* Confidence score visualization
* Comparison of multiple CNN architectures

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes only**.

It is not intended to provide medical diagnosis, treatment recommendations, or clinical decisions. A qualified healthcare professional should always interpret medical imaging.

---

## 👨‍💻 Author

**Arunabha Dey**

Computer Science & Engineering

Interested in:

* Machine Learning
* Deep Learning
* Generative AI
* Data Analytics
* Computer Vision

---

## ⭐ If you found this project useful

Consider giving the repository a ⭐ and exploring the implementation.
