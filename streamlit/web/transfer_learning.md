# Transfer Learning 🍃

### Introduction to MobileNetV2
- We leveraged this model to handle our extensive dataset, featuring over 61,000 images across 51 diverse classes.
- From the get-go, MobileNetV2 demonstrated impressive performance: achieving a F1-Score above 90% while keeping the training time under 4 hours with 20 epochs on a laptop with the following Video card:
  - Graphics co-processor:	**NVIDIA GeForce GTX 1060**
  - Graphics RAM: size	**6 GB**
  - GPU clock speed:	**1759 MHz**

For a more detailed review of MobileNetV2, check out this breakdown: "Tensorflow MobileNetV2" - Ref #5

### Streamlined Training Approach
- We quickly saw that after the initial 10 epochs, our model was performing well without the need for extensive training.
- Drawing on lessons from previous models, we set the image resolution to a consistent 180x180 pixels during the loading phase.
- We also followed established best practices by sticking to a batch size of 32, as this had proven effective in earlier models.

### Configuration
After different trials and configurations, we settled on the following setup:
- The dataset was split into 80% training, 16% validation, and 4% test partitions.
- Initially, the training commenced with 10 epochs, each taking approximately 11 minutes, culminating in a total training duration of about 2 hours.
- Additionally, the fine-tuning process spanned 10 epochs, with each epoch approximately taking 17 minutes, culminating in a total training time of around 3 hours.
- Achieved the F1-Score exceeding 97% on the test dataset, a testament to the model's robustness and efficiency.

### Detailed Insights
<details>
  <summary>Technical Overview of MobileNetV2</summary>
  <div align="left">
  ![Technical Overview of MobileNetV2 part 1](web/img/tl_model_1.png)
  <br>
  ![Technical Overview of MobileNetV2 part 2](web/img/tl_model_2.png)
  <br>
  <p>.</p>
  <p>.</p>
  <p>.</p>
  ![Technical Overview of MobileNetV2 part 3](web/img/tl_model_3.png)
  </div>
</details>
<br>

<details>
  <summary>Technical Overview of Transfer Learning model</summary>
  <div align="left">
  ![Technical Overview of MobileNetV2 part 1](web/img/tl_model_complete.png)
  </div>
</details>
<br>

### Summaries
<details>
  <summary>Training and Validation Accuracy + Loss Graphs</summary>
  <div align="left">
  ![Accuracy and Loss Over Epochs](web/img/tl_accloss.png)
  </div>
</details>
<br>

<details>
  <summary>F1-Score Distribution Across Classes for the Test Dataset</summary>
  <div align="left">
  ![F1-Score by Class](web/img/tl_f1_score.png)
  </div>
</details>
<br>

<details>
  <summary>Confusion matrix for Test Dataset</summary>
  <div align="left">
  ![Confusion Matrix](web/img/tl_conf_matrix.png)
  </div>
</details>
<br>

### Conclusion
MobileNetV2 not only met but exceeded our performance expectations with the F1-Score over 97% :smiley:.
