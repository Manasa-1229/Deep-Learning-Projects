# Real vs. Fake Face Image Detection

This project demonstrates the application of deep learning models for detecting whether an image of a face is real or fake. The repository includes several Jupyter notebooks that showcase different neural network architectures and their application to this task. Last worked on 4/25/2023

## Project Structure

/Real_vs_Fake_Face_Detection  
│  
├── /Test/                                  # Test dataset directory  
├── /Train/                                 # Training dataset directory  
├── /Valid/                                 # Validation dataset directory  
│  
├── Efficient_net_demo.ipynb                # Jupyter notebook demonstrating EfficientNet model  
├── Project_Big_data_Real_Fake_face_image_detection.ipynb  # Main project notebook for real vs. fake face detection  
├── Resnet_demo.ipynb                       # Jupyter notebook demonstrating ResNet model  
├── VGG16.ipynb                             # Jupyter notebook demonstrating VGG16 model  
│  
└── README.md                               # Project documentation (this file)


### Notebooks Overview

- **Efficient_net_demo.ipynb**: This notebook demonstrates how to use the EfficientNet architecture for detecting fake faces. EfficientNet is known for its balance between accuracy and computational efficiency.

- **Project_Big_data_Real_Fake_face_image_detection.ipynb**: The main notebook for this project. It includes data preprocessing, model training, evaluation, and results. It might use one or more deep learning architectures to differentiate between real and fake face images.

- **Resnet_demo.ipynb**: Demonstrates the use of the ResNet architecture. ResNet is widely used in image classification tasks due to its ability to train very deep networks without the problem of vanishing gradients.

- **VGG16.ipynb**: This notebook demonstrates the VGG16 model, which is a well-known convolutional neural network architecture used for image classification tasks.

### Datasets

- **/Train/**: Contains the  sample training dataset used to train the models.
- **/Valid/**: Contains the Sample validation dataset used to tune the models and select the best one.
- **/Test/**: Contains the sample test dataset used for final evaluation of the models.

## **NOTE:** 
The dataset uploaded here is only a sample. The actual dataset used for this project is large and couldn't be uploaded. A reference link to the full dataset will be provided.


### Getting Started

To get started with this project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Real_vs_Fake_Face_Detection.git
   cd Real_vs_Fake_Face_Detection
   ```

2.**Set Up the Environment**:

- Make sure you have Python installed along with Jupyter Notebook.
- Install the necessary dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3.**Run the Notebooks**:
- Start Jupyter Notebook:
```bash
jupyter notebook
```

- Open and run the notebook "Project_Big_data_Real_Fake_face_image_detection.ipynb" 

4. **Results and Performance**:
- Each notebook contains the results obtained from running the corresponding model on the real vs. fake face detection task.

5. **Acknowledgements**:

- Special thanks to the dataset providers.
- The authors of the models and libraries used in this project are: Manas Paul and Manasa Gonuguntla.          




