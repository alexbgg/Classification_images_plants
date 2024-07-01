# Data Analysis 🍃

## Dataset
The data used in this project has been retrieved from the following sources:
- The Plant Seedlings Dataset - Ref #1

This dataset contains images of very young plants (seedlings). It has around 5.5K images that represent 12 classes.

<div align="center">
![“Cleavers”](web/img/da_cleavers.png)

Figure 1: Representative image of the dataset [seedling of the plant species “Cleavers”]
</div>

- The PlantVillage Dataset - Ref #2

This dataset contains images of the leaves for grown-up plants. It has around 55.5K images. The dataset contains healthy plants but also plants with diseases.


<div align="center">
![“scab”](web/img/da_scab.png)

Figure 2: Representative image of the dataset [“scab”-diseased mature leaf of the plant species “Apple”]
</div>

So, the full dataset contains ~61K pictures. This consolidated dataset represents 26 different plants and shows 20 different types of diseases, in total 51 classes.
For more detailed evaluation we'd like to refer the reader to our project report 1 which contains in-depth analytics of the datasets used.

### Detailed Insights
<details>
  <summary>Plant distribution</summary>
  <div align="left">
  ![Plant distribution](../reports/figures/1.0-arif-plot-3.png)
  </div>
</details>

<details>
  <summary>Healthy pie</summary>
  <div align="left">
  ![Healthy pie](../reports/figures/1.0-arif-plot-2.png)
  </div>
</details>


## Evaluation criteria
We decided to use the F1-Score as primary evaluation criteria for any of our models. Important hereby is that this score has to be calculated on a test dataset which is to be kept separate from any of the training data for the model.
Additional criteria were that there are no obvious (or at least significantly worse than others) signs of overfitting. Also, the IT resources and time required to train the model were considered in the evaluation.