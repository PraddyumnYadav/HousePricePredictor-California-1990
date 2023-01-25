# Importing Essentials
from model import request_prediction
from tkinter import *
import pandas as pd

# Initialize Our Root Window
root = Tk()

# Add Title of our Window
root.title("Housing Price Predictor Model")

# Creating Our Welcome Label
my_welcome_label = Label(root, text="  Welcome to HousePricePredictor  ", font=('Helvetica bold', 25))
my_welcome_label.pack()

# Create All of Our Input Fields
longitude_IF = Entry(root, width=25, font=('Helvetica bold', 13))
latitude_IF = Entry(root, width=25, font=('Helvetica bold', 13))
age_IF = Entry(root, width=25, font=('Helvetica bold', 13))
total_rooms_IF = Entry(root, width=25, font=('Helvetica bold', 13))
total_bedrooms_IF = Entry(root, width=25, font=('Helvetica bold', 13))
population_IF = Entry(root, width=25, font=('Helvetica bold', 13))
household_IF = Entry(root, width=25, font=('Helvetica bold', 13))
income_IF = Entry(root, width=25, font=('Helvetica bold', 13))
ocean_proximity_IF = Entry(root, width=25, font=('Helvetica bold', 13))

# Create All Input Field Labels
longitude_label = Label(text="Longitude:", font=('Helvetica bold', 13))
latitude_label = Label(text="Latitude:", font=('Helvetica bold', 13))
age_label = Label(text="Age:", font=('Helvetica bold', 13))
total_rooms_label = Label(text="Total Rooms:", font=('Helvetica bold', 13))
total_bedrooms_label = Label(text="Total Bedrooms:", font=('Helvetica bold', 13))
population_label = Label(text="Population:", font=('Helvetica bold', 13))
households_label = Label(text="Households:", font=('Helvetica bold', 13))
income_label = Label(text="Income:", font=('Helvetica bold', 13))
ocean_proximity_label = Label(text="Ocean Proximity:", font=('Helvetica bold', 13))

# Display All of Our Labels and Input Fields
longitude_label.pack()
longitude_IF.pack()

latitude_label.pack()
latitude_IF.pack()

age_label.pack()
age_IF.pack()

total_rooms_label.pack()
total_rooms_IF.pack()

total_bedrooms_label.pack()
total_bedrooms_IF.pack()

population_label.pack()
population_IF.pack()

households_label.pack()
household_IF.pack()

income_label.pack()
income_IF.pack()

ocean_proximity_label.pack()
ocean_proximity_IF.pack()


# Create a Function for our Predict Button
def predict_button_function():
    longitude = float(longitude_IF.get())
    latitude = float(latitude_IF.get())
    age = float(age_IF.get())
    total_rooms = float(total_rooms_IF.get())
    total_bedrooms = float(total_bedrooms_IF.get())
    population = float(population_IF.get())
    household = float(household_IF.get())
    income = float(income_IF.get())
    ocean_proximity = ocean_proximity_IF.get()

    DictData = {
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": household,
        "median_income": income,
        "ocean_proximity": ocean_proximity,
    }

    DictDataPrepared = pd.DataFrame(DictData, index=[0])
    MLPrediction = request_prediction(DictDataPrepared)

    my_final_prediction_label = Label(root, text=MLPrediction[0], font=('Helvetica bold', 15))
    my_final_prediction_label.pack()

# Create Predict Button to our GUI
spacing_label = Label()
predict_btn = Button(root, text="Predict", command=predict_button_function)
predict_btn.config(font=('Helvetica bold', 15))
spacing_label.pack()
predict_btn.pack()

# Run Tkinter GUI Mainloop
root.mainloop()
