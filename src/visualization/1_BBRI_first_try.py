import imageio.v3 as iio
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

# Dataset paths definition
path_project = "C:/Users/Bernd/Documents/GitHub/apr24_bds_int_plant_recognition/"

path_base = path_project + "data/processed/"
#path_base = path_project + "data/processed/kaggle/input/v2-plant-seedlings-dataset/Sugar beet"
paths_to_exclude = [ path_project + "data/processed/kaggle/input/v2-plant-seedlings-dataset/nonsegmentedv2" ]

# Defining dictionary for being used to later create the dataframe
raw_data = {'plant': [], 'dir' : [], 'file' : [], 'shape_x' : [], 'shape_y' : [], 'shape_z' : [], 'pix_count' : [], 'is_square' : [] }

# Now adding all the pictures we have in our filesystem to the dictionary
for dirname, _, filenames in os.walk(path_base):

    # Replacing \ with /
    dirname = dirname.replace("\\", "/")

    # Check for our exlusion list
    proceed = True
    for to_exclude in paths_to_exclude:
         if dirname.find(to_exclude) > -1:
            proceed = False
 
    # Proceed if not excluded
    if proceed:
        plantname = dirname.split('/')[-1]
        for filename in filenames:

            with iio.imopen(os.path.join(dirname, filename), "r") as img:
                # Read metadata
                shape_x, shape_y, shape_z = img.properties().shape
                
            pix_count = shape_x * shape_y
            is_square = (shape_x == shape_y)
            
            for ind, val in zip(['plant', 'dir', 'file', 'shape_x', 'shape_y', 'shape_z', 'pix_count', 'is_square'], 
                                [plantname, dirname, filename, shape_x, shape_y, shape_z, pix_count, is_square]):
                raw_data[ind].append(val)

# Creating the dataframe
df = pd.DataFrame(data = raw_data)

print(df.info())
print(df.head())

# Plotting our first data
plt.figure(figsize = (10, 10))
plt.title('Plot 1 - Count of pictures by plant')
plt.ylabel('plant')
plt.xlabel('count')
sns.countplot(y = df.plant)
plt.show()

plt.figure(figsize = (10, 10))
plt.title('Plot 2 - Boxplot on pix_count')
plt.ylabel('pix_count')
sns.boxplot(y = df.pix_count)
plt.show()

plt.figure(figsize = (10, 10))
plt.title('Plot 3 - Are pictures in square format?')
plt.xlabel('is_square')
sns.countplot(x = df.is_square)
plt.show()
