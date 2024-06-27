# Transfer Learning 🍃

### Introduction to MobileNetV2
- We leveraged this model to handle our extensive dataset, featuring over 61,000 images across 51 diverse classes.
- From the get-go, MobileNetV2 demonstrated impressive performance: achieving an F1-Score above 90% while keeping the training time under 45 minutes on a standard laptop.

For a more detailed review of MobileNetV2, check out this breakdown: https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2?hl=en

### No effort to Optimize Performance
- Following the suggested practices from previous models, we standardized the image resolution to 180x180 during the loading phase.
- I adhered to the suggested logic based on the previous model and consistently used a batch size of 32.

### Configuration
After different trials and configurations, we settled on the following setup:
- The dataset was split into 70% training, 20% validation, and 10% test partitions.
- Initially, the training commenced with 10 epochs, each taking approximately 11 minutes, culminating in a total training duration of about 2 hours.
- Additionally, the fine-tuning process spanned 10 epochs, with each epoch approximately taking 17 minutes, culminating in a total training time of around 3 hours.
- Achieved an F1-Score exceeding 94% on the test dataset, a testament to the model's robustness and efficiency.

### Detailed Insights and Visual Summaries
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
  <summary>Training and Validation Accuracy + Loss Graphs</summary>
  <div align="left">
  ![Accuracy and Loss Over Epochs](web/img/tl_accloss.png)
  </div>
</details>
<br>

<details>
  <summary>F1-Score Distribution Across Classes for the Test Dataset</summary>
  <div align="left">
  ![F1-Score by Class](web/img/mobilenetv2_f1-score.png)
  </div>
</details>
<br>

### Conclusion
MobileNetV2 not only met but exceeded our performance expectations with an F1-Score over 97%.
