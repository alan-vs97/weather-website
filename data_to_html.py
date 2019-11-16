import pandas as pd

data = pd.read_csv("Resources/cities.csv")

data.to_html("data_raw.html", index = False, justify="center")