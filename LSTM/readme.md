### LSTM for Text and Speech Processing

This project explores the application of Long Short-Term Memory (LSTM) networks for two critical tasks: **speech-to-text conversion** and **story generation**. LSTMs are a type of recurrent neural network (RNN) particularly well-suited for processing and generating sequences of data, making them ideal for tasks involving text and speech.

#### Project Overview

In this project, LSTMs are used to:

1. **Speech-to-Text Conversion**: Convert spoken language into written text by processing sequential audio data and predicting the corresponding text. This task leverages LSTM’s ability to capture the temporal dependencies in audio signals.

2. **Story Generation**: Generate coherent and contextually relevant stories based on a given prompt. LSTMs process the input text and generate new text that follows the learned patterns and structures from the training data.

#### Computational Constraints

Due to computational constraints, only **0.05%** of the available data was used for model training and evaluation. While this limited the overall dataset size, the project still demonstrates the effectiveness of LSTM networks in handling sequential data and producing meaningful outputs in both speech and text domains.

## Project Structure
/Speech_to_Text_and_Story_Generation  
│  
├── /_pycache/                                              # Cached Python files  
│  
├── With_Openai.ipynb                                       # Jupyter notebook interacting with OpenAI API  
├── cleaned_merged_fairy_tales_without_eos.txt              # Dataset used for training LSTM models  
├── notebook_LSTM.ipynb                                     # Jupyter notebook demonstrating LSTM model training  
├── readme.md                                               # Project documentation (this file)  
├── speechToText.py                                         # Python script for speech-to-text conversion using LSTM  
├── storyteller_lstm.pkl                                    # Saved LSTM model for story generation  
├── storyteller_lstm_1.pkl                                  # Alternate version of the saved LSTM model  
├── storyteller_lstm_3.pkl                                  # Another version of the saved LSTM model  
├── text_to_speech.py                                       # Python script for text-to-speech conversion  



## How to Get Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Speech_to_Text_and_Story_Generation.git
   cd Speech_to_Text_and_Story_Generation
   ```
   

2. **Set Up the Environment**:

- Ensure you have Python installed.
- Install the necessary dependencies using requirements.txt (if available):
   ``` bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebooks**:

- Start Jupyter Notebook:
``` bash
jupyter notebook
```

- Open and run the notebooks (.ipynb files) in the desired order to reproduce the results.

4. **Use the Python Scripts**:

speechToText.py: Converts speech to text using a trained LSTM model.
text_to_speech.py: Converts text back into speech.



## Acknowledgements
Special thanks to the providers of the fairy tales dataset used for training the LSTM models.

