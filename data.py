import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import random
import statistics

df = pd.read_csv("data.csv")
data = df["Mobile Brand"].tolist()

Mb_mean = statistics.mean(data)
Mb_stdev = statistics.stdev(data)

print(f"Mb_mean: {Mb_mean}")
print(f"Mb_stdev: {Mb_stdev}")

def random_set_of_mean():
    datalist = []
    for i in range(0, 100):
        num = random.randint(0, len(data)-1)
        random_value = data[num]
        datalist.append(random_value)
    mean = statistics.mean(datalist)
    return mean

mean_list = []
for i in range(0, 1000):
    sample_mean = random_set_of_mean()
    mean_list.append(sample_mean)

fig = ff.create_distplot([mean_list], ["temp"], show_hist = False)
fig.show()

