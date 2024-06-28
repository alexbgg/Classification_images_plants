# LeNet 🍃
### About LeNet
- LeNet was introduced in DataScientest modules _151.2 - Convolutional Neural Networks with Keras (EN)_ and _155 - Tensorflow (EN)_
- First model with which we successfully scaled up to full dataset of 51 classes with ~61K images
- Very acceptable result and fitting time already at initial attempt: F1-Score > 80%, < 60 minutes for model training on standard laptop 
- Brief overview and comparison of LeNet - Ref #3

### Trials to further improve F1-Score and to address overfitting
- Converting to alternative image sizes at loading (between 32 x 32 and 256 x 256)
- Modified batch sizes for training (between 32 and 256)
- Adding more dropout layers
- Adusting dropout rates (between 0.2 and 0.5)
- Applying L2 weight regularization
- Adjusting class-weights for classes with low representation
- Using augmentation layers to generate additional images: this didn't improve the F1-Score but indeed reduced overfitting

Also see "Overfit and underfit" - Ref #4

### Setup after tuning
Final setup after finishing trials:
- Splitting dataset into training (80%), validation (16%) and test (4%)
- Model trained using datasets for training and validation. Testing dataset kept separately and only used for evaluation
- Images were converted to 64 x 64 x 3 at loading
- Batch size of 32
- Callbacks for adjusting the learning rate when reaching a plateau and early stopping
- Model finalized training after 73 epochs (33s per epoch, 40 min in total)
- F1-Score on the test dataset > 92%

### Technical summary of model
<details>
  <summary>Technical summary of model</summary>
  <div align="left">
  ![Technical summary of model](web/img/lenet_model.png)
  </div>
</details>
<br>

### Results
<details>
  <summary>Training and validation accuracy + loss</summary>
  <div align="left">
  ![Training and validation accuracy + loss](web/img/lenet_history.png)
  </div>
</details>
<br>
<details>
  <summary>F1-Score in relation to observations by class for test dataset</summary>
  <div align="left">
  ![F1-Score in relation to observations by class for test dataset](web/img/lenet_f1-score.png)
  </div>
</details>
<br>
<details>
  <summary>Confusion matrix for test dataset</summary>
  <div align="left">
  ![Confusion matrix for test dataset](web/img/lenet_cm.png)
  </div>
</details>
<br>

### Conclusion
Our LeNet performed really well with reaching an F1-Score > 92% with reasonable fitting time!

**However it wasn't selected as final model as we were able to still do better...**