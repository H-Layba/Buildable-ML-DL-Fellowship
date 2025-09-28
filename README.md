# ANN vs CNN for Image Classification

## Project Overview
This project explores **Artificial Neural Networks (ANNs)** and **Convolutional Neural Networks (CNNs)** for image classification tasks.  
We first test both models on the **MNIST dataset (handwritten digits)** and then extend the comparison to the **Cats vs Dogs dataset**.  

The goal is to understand:
- The limitations of ANNs for image tasks.  
- The strengths of CNNs in extracting spatial features.  
- How regularization techniques and callbacks improve training.  

---

## Datasets
1. **MNIST (built-in Keras dataset)**  
   - 60,000 training + 10,000 test images (28x28 grayscale digits).  
   - Classification into 10 classes (digits 0–9).  

2. **Cats vs Dogs**  
   - Downloaded dataset with two folders: `cats/` and `dogs/`.  
   - Used **image_dataset_from_directory** to split into training (80%) and validation (20%).  
   - Images resized to **150x150** pixels.  

---

## Models

### ANN (Fully Connected Network)
- Input flattened into 1D vector.  
- Dense(512) → Dropout(0.2)  
- Dense(256) → Dropout(0.2)  
- Output Layer (Softmax for MNIST, Sigmoid for Cats vs Dogs).  

### CNN (Convolutional Neural Network)
- Conv2D(32) → Conv2D(64) → MaxPooling → Dropout  
- Conv2D(128) → MaxPooling  
- Flatten → Dense(256) → Dropout → Output Layer.  

### Training Setup
- Optimizer: **Adam**  
- Loss: **SparseCategoricalCrossentropy** (MNIST), **BinaryCrossentropy** (Cats vs Dogs).  
- Callbacks:  
  - **EarlyStopping** → Stops training when validation loss doesn’t improve.  
  - **ModelCheckpoint** → Saves best model.  

---

## Results

### MNIST
| Model | Validation Accuracy | Validation Loss |
|-------|---------------------|-----------------|
| ANN   | ~98.2%              | ~0.06           |
| CNN   | ~99.1%              | ~0.027          |

CNN outperforms ANN, capturing spatial relationships in images.  
<img width="868" height="332" alt="image" src="https://github.com/user-attachments/assets/4e384051-3e8c-47bc-89e4-1b74a094f8dc" />

<img width="462" height="383" alt="image" src="https://github.com/user-attachments/assets/b3414bd3-6917-4781-90b0-af977693da4f" />

---

### Cats vs Dogs
| Model | Validation Accuracy | Validation Loss |
|-------|---------------------|-----------------|
| ANN   | ~99% (overfits fast) | 0.05            |
| CNN   | ~100% (too perfect)  | 1e-07           |

The CNN results suggest **possible data leakage or small validation set**.  


---

##  Conceptual Insights
- **Why CNN > ANN for Images?**  
  CNNs exploit local spatial structure via convolution filters → fewer parameters, better generalization.  
- **Pooling Layers:** Reduce spatial size, lower computation, and make model invariant to small shifts.  
- **Max vs Avg Pooling:** Max pooling captures dominant features; average pooling smooths features.  

---

## Visuals
- Training accuracy & loss curves for both models.  
- Confusion matrix for MNIST.  
- Sample predictions for Cats vs Dogs.  

---


 
