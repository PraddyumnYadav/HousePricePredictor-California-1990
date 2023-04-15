# HousePricePredictor-California-1990
- A Machine Learning Model for Predicting Price of House from California Census 1990
- **This Machine Learning Model is Derived From Hands on ML Book by Aurelien Geron.**
- Your Python Version Should Be Between python3.7 or python 3.10 because kivy don't Supports python3.11
## Description about Model
- This is a Machine Learning Model that can Predict Prices of House Which are at California.
- The Price Predicted By This Model is according to Census of 1990.
- I Have Used Sciket-learn in This Project
## Description about Webiste
- I have Used Python-Django FrameWork in this Project.
- I have used Tailwind CSS as a Frontend FrameWork
- Here i Converted My Model in .pkl file With The help of joblib module in python.
- I Have Created a model.py file in which i have the pipeline and a function name request_prediction().
- if i Give The data into request_prediction() function it first executes the pipeline in which my data is transformed in many ways and then it is feeded to the machine learning model and output is returned.
- Then its Returned Information is Presented as Prediction in our next Page Using Django.
## Description about GUI's
- I have Used `Python-Tkinter` and `Python-Kivy` FrameWork in this Project.
- Here i used the same `.pkl` file in this Project.
- I have also used The same model.py file.
- I Have Taken all inputs in form of string then converted it in float then feed it to Machine Learning Model.
## How to Get This Running on Your System
- Clone the Repository Using SSH
```
git clone git@github.com:PraddyumnYadav/HousePricePredictor-California-1990.git
```
or HTTPS
```
git clone https://github.com/PraddyumnYadav/HousePricePredictor-California-1990.git
```
- cd into HousePricePredictor-California-1990.
```
cd HousePricePredictor-California-1990
```
- Intall virtualenv Module.
```
pip install virtualenv
```
- Create a Virutal Enviornment.
```
virutualenv venv
```
- Activate the Virutal Enviornment.
```
source ./venv/bin/activate
```
- Install All the Dependencies.
```
pip install -r requirements.txt
```
- Now You are Ready to run this on Your Local Machine.
# Conclusion
If You Notice any Bugs in our Code or You Think That you Can Make This Code a Little Bit Better Than Don't Hesistate You Can Do Two Things in That Case
- First Thing is That You Can Raise an Issue.
- Second Thing is That You Can Open a Pull Request I Will be Very Happy to See Your Code and if it is Good Than i Will Definetly Add it to My Main Repository.
### Thank You
