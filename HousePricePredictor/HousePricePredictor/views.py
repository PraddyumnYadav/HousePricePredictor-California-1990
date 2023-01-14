from django.shortcuts import render
from .model import request_prediction
import pandas as pd


def home(request):
    return render(request, "home.html")


def result(request):
    DictData = {
        "longitude": [request.GET["longitude"]],
        "latitude": [request.GET["latitude"]],
        "housing_median_age": [request.GET["housing_median_age"]],
        "total_rooms": [request.GET["total_rooms"]],
        "total_bedrooms": [request.GET["total_bedrooms"]],
        "population": [request.GET["population"]],
        "households": [request.GET["households"]],
        "median_income": [request.GET["median_income"]],
        "ocean_proximity": [request.GET["ocean_proximity"]],
    }

    DictDataPrepared = pd.DataFrame(DictData)
    MLPrediction = request_prediction(DictDataPrepared)
    return render(request, "result.html", {"prediction": MLPrediction})
