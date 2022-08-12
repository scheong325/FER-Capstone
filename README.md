# Real-time Emotion Detection System  
The system is designed for Rooster Teeth to capture the player's emotion in the real time with webcam. The collected data is used for market research and product development within the company. The emotion detection system is capable of differentiating 7 emotions: angry, disgust, sad, happy, netural, surprise and fear. 

# Built with 
- OpenCV
- Tensorflow 2
- Flask 
- SQLite

# Data
The data was obtained from kaggle: https://www.kaggle.com/datasets/msambare/fer2013

# Model 
The model is bult with Convolutional Neural Networks(CNN) in 4 layers. model_structure.json and model_weights.h5 files will be created after training the model. 

# Steps to install the program 
1. Clone/Download the Repo @ https://github.com/scheong325/FER-Capstone.git
2. Install miniconda for your OS: https://docs.conda.io/en/main/miniconda.html
3. After installing minicoda, launch and ensure you are in the 'base' conda environment, specified with 'base' in the terminal window.
4. Navigate to the FER-Capstone folder
5. Install required packages:
        
        Windows/ Linux/ Mac: 

        pip install -r requirements.txt

6. Navigate one folder out of FER-Capstone (ex: If your clone is in /home/FER-Capstone, navigate to /home/)
7. Set the Flask Env Variable(This has to be repeated every time the conda environment is started):

        Windows(cmd prompt): set FLASK_APP=FER-Capstone
        Linux/Mac: export FLASK_APP=FER-Capstone

8. Launch the Flask application by running: Flask run
9. A URL will be generated within the terminal window, copy/paste into your browser or "ctrl+click" to open.  

# How to use the program 
Pre-created account: fer@rooster.com:Password
1. Sign up an account on the flask webpage 
2. Log in with the your credentials 
3. Click the emotion detection tab 
4. Click the start camera button to start emtion detection 
5. Click the stop camera button to generate the prediction analytics
6. Sign out the program after clicking the log out button 

# Train model 
Run the Jupiter Notebook modeltraining.ipynb ifor model training, model_structure.json and model.h5 files will be created after training 

# How to add more data
Store 48x48 pixel grayscale images in train or test folder 


