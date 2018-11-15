import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with open("tweet.json", "r") as read_file:
    data = json.load(read_file)
