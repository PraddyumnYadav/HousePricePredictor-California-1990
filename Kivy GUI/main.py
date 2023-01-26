# Importing Essentials
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from model import request_prediction


# Create Our Main Widget
class MainWidget(Widget):
    def predict_button_function(self):
        longitude = float(self.ids.Longitude.text)
        latitude = float(self.ids.Latitude.text)
        age = float(self.ids.Age.text)
        total_rooms = float(self.ids.total_rooms.text)
        total_bedrooms = float(self.ids.total_bedrooms.text)
        population = float(self.ids.population.text)
        household = float(self.ids.households.text)
        income = float(self.ids.income.text)
        ocean_proximity = self.ids.ocean_proximity.text

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
        TextToDisplay = f"Prediction = {MLPrediction[0]}"

        self.ids.Prediction.text = TextToDisplay



# Create Our Main App
class HousePricePredictorApp(App):
    pass


if __name__ == "__main__":
    HousePricePredictorApp().run()
