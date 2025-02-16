# Brain Tumor MRI Classification using EfficientNet

This project focuses on classifying brain tumors from MRI scans using the **EfficientNet** deep learning model. The dataset consists of labeled MRI images, and various preprocessing techniques, including **data augmentation**, have been applied to improve model performance.

## Dataset
The dataset is sourced from **Kaggle**:  
[Brain Tumor MRI Scans](https://www.kaggle.com/datasets/rm1000/brain-tumor-mri-scans)  

### Classes:
- **Healthy** : 0  
- **Pituitary** : 1  
- **Meningioma** : 2  
- **Glioma** : 3  

Each image is labeled according to one of the above categories.

## Model
The **EfficientNet** model has been used for classification due to its high efficiency and accuracy in image recognition tasks. The model is trained with **data augmentation** techniques to enhance generalization and improve performance.

## Accuracy
The final model achieves an **accuracy of 87%** in classifying brain tumors.

## Requirements
- Python 3.x  
- TensorFlow, Keras  
- NumPy, Pandas  
- Matplotlib, Scikit-learn  

## Conclusion
This project demonstrates the effectiveness of EfficientNet in brain tumor classification, achieving 87% accuracy. The use of data augmentation helped improve model generalization. Future improvements could include:

- Fine-tuning the model with more labeled MRI images.
- Exploring transfer learning with pre-trained medical image models.
- Implementing attention mechanisms for better feature extraction.
