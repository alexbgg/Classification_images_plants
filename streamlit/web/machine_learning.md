# Classic Machine Learning for Image Classification 🍃

### Overview

- Examines traditional machine learning techniques for image classification.
- Explores optimal feature extraction methods and algorithm selection.

### Limitations

- Findings based on limited computational resources and a subset of the dataset (only 4 classes out of 51).
- The findings are based on a predominantly heuristic approach and non-exhaustive analysis of the relevant knowledge base.
- Future work should explore more algorithms and methodologies.

### Image Processing and Feature Extraction

- We used the Support Vector Machine (SVM) algorithm to come up with a reasonably optimal image descriptor configuration.
- **Top 3 Methods and Findings**

  - **Histogram of Oriented Gradients (HOG)**

    - Captures gradient orientation.
    - Effective for edges and shapes, but sensitive to illumination and viewpoint changes.
    - Not good at capturing color distribution.
    - Accuracy: 0.68.

  - **Color Histograms + HOG**

    - Combines color distribution with gradient orientation.
    - Improved feature extraction by 10%.
    - Accuracy: 0.78.

  - **Fourier and Wavelet Transform + PCA**
    - High-dimensional feature space reduced with PCA.
    - Not as effective as HOG and Color Histograms and resource inefficient.
    - Accuracy: 0.71.

- **Optimal Feature Extraction Method**
  - **Combination of HOG and Color Histograms**
    - Selected for computational efficiency, robustness, and complementary strengths.
    - Captures both structural and color information effectively.

### Model Selection and Training

- **Top 3 Algorithms Considered**

  - **XGBClassifier (97%)**

    - Chosen for high accuracy and scalability.
    - Selected for superior performance and robustness against overfitting.
    - Significantly outperformed other algorithms.
    <details>
      <summary>Classification Report</summary>
      <div align="left">
      ![Classification Report](web/img/arif_classification.png)
      </div>
    </details>
    <br>

    <details>
      <summary>Log Loss</summary>
      <div align="left">
      ![Log Loss](web/img/arif_loglos.png)
      </div>
    </details>
    <br>
    <details>
      <summary>Confusion Matrix</summary>
      <div align="left">
      ![Confusion Matrix](web/img/arif_confusion_matrix.png)
      </div>
    </details>

  - **Support Vector Machine (SVM) (78%)**

  - **RandomForestClassifier (75%)**

### Comparison with pre-trained VGG16 Model

- **Pre-trained VGG16 Model for Feature Extraction**
  - Achieved similar accuracy (~0.97) as combination of HOG and CH.
  - Less suitable due to computational demands.

### Conclusion

- Trained a deep learning model on a subset of the dataset for bench marking.
- DL model gave an indication for being superior to the best of classic ML
- The DL model, with a custom architecture, was trained for 50 epochs and achieved a validation accuracy of 98.91%.
- Correctly predicted previously misclassified images.
