# Data Analysis 🍃

## Dataset
The data used in this project has been retrieved from the following sources:
- [The Plant Seedlings Dataset](https://vision.eng.au.dk/plant-seedlings-dataset/)

This dataset contains images of very young plants (seedlings). It has around 5.5K images that represent 12 classes.

<div align="center">
![“Cleavers”](web/img/da_cleavers.png)

Figure 1: Representative image of the dataset [seedling of the plant species “Cleavers”]
</div>

- [The PlantVillage Dataset](https://data.mendeley.com/datasets/tywbtsjrjv/1)

This dataset contains images of the leaves for grown-up plants. It has around 55.5K images. The dataset contains healthy plants but also plants with diseases.


<div align="center">
![“scab”](web/img/da_scab.png)

Figure 2: Representative image of the dataset [“scab”-diseased mature leaf of the plant species “Apple”]
</div>

So, the full dataset contains ~61K pictures. This consolidated dataset represents 26 different plants and shows 20 different types of diseases, in total 51 classes.
For more detailed evaluation we'd like to refer the reader to our project report 1 which contains in-depth analytics of the datasets used.

## Evaluation criteria
We decided to use the F1-Score as primary evaluation criteria for any of our models. Important hereby is that this score has to be calculated on a test dataset which is to be kept separate from any of the training data for the model.
Additional criteria were that there are no obvious (or at least significantly worse than others) signs of overfitting. Also, the IT resources and time required to train the model were considered in the evaluation.