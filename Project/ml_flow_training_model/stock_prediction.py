import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import urllib.request, json
import os
import sys
import numpy as np
import tensorflow as tf
import mlflow
import load_stock_data
import train_stock_prediction_model

if __name__ == "__main__":
    with mlflow.start_run():
        df = load_stock_data.get_stock_data()
        train_stock_prediction_model.train_model(df)


