import pandas
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(20, 10))

columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
info = pandas.read_csv('heartdisease/processed.hungarian.data', header=None, names=columns)

info_classes = info['num'].unique()
feature_name1 = 'age'
feature_name2 = 'sex'

colors=[[1,0,0],[0,1,0]]

for i, species in enumerate(info_classes):
   species_data = info[info['num'] == species]
   plt.plot(species_data.index, species_data[feature_name1], marker='o', linestyle='', color=colors[i], label=species)
   plt.plot(species_data.index, species_data[feature_name2], marker='o', linestyle='', color=colors[i], label=species)