# Emotion Detection Project

This repository contains the files and scripts for the Emotion Detection project. The goal of this project is to develop a machine learning model capable of detecting emotions from facial images using deep learning techniques.

## Project Structure
/ Emotion_Detection_Project
│
├── Project_Big_data_Emotion_detection.ipynb # Main Jupyter notebook for the emotion detection project
├── Readme.md # Project documentation (this file)
├── get_link_list.py # Python script to generate or process list of image links
└── list_patition_label.txt # Text file containing partition and label information for the dataset

## Description of Files

- **Project_Big_data_Emotion_detection.ipynb**:  
  This Jupyter notebook contains the code and analysis for developing the emotion detection model. It includes data preprocessing, feature extraction, model training, and evaluation steps.

- **Readme.md**:  
  This file provides an overview of the project, the contents of the repository, and instructions on how to use the files.

- **get_link_list.py**:  
  This Python script is used to generate or process a list of image links. It might be used for downloading images or managing datasets.

- **list_patition_label.txt**:  
  This text file contains information on the partitioning of the dataset and the corresponding labels. It is likely used to guide the model training process by providing labels for the images in the dataset.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Emotion_Detection_Project.git
   cd Emotion_Detection_Project
   ```
2. **Set Up the Enviroment**:
   - Make sure you have Python and Jupyter Notebook installed.
   - Install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```

3. **Run the Jupyter Notebook**:
   - Start Jupyter Notebook:
```bash
jupyter notebook
```
  - Open and execute Project_Big_data_Emotion_detection.ipynb to see the full workflow of the emotion detection model.

## Dataset Information
This project utilizes the Real-world Affective Faces (RAF) Database for training and evaluating the emotion detection model. The dataset includes a diverse collection of facial images labeled with various emotions. The images are organized into different partitions, with corresponding labels specified in the list_patition_label.txt file.

**Data Resource**: http://whdeng.cn/RAF/model1.html

## Acknowledgements
Special thanks to Li Shan for facilitating access to the RAF Face Database. I extend my gratitude to the dataset provider. 
