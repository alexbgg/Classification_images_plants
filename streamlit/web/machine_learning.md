### Classic Machine Learning for Image Classification

- **Overview**
  - Explores traditional machine learning techniques for image classification.
  - Exploring optimal feature extraction methods and algorithm selection.

### Image Processing and Feature Extraction

- we used the Support Victor Machine (SVM) algorithm to train our features, comparing which method is optimal.
- **Methods and Findings**

  - **Histogram of Oriented Gradients (HOG)**

    - Captures gradient orientation.
    - Effective for edges and shapes, but sensitive to illumination and viewpoint changes.
    - Not good at capturing color distribution.
    - Accuracy: 0.68.

  - **Color Histograms + HOG**

    - Combines color distribution with gradient orientation.
    - Improved feature extraction by 10%.
    - Accuracy: 0.78.

  - **Local Binary Patterns (LBP) + HOG**

    - Combines texture analysis with gradient orientation.
    - Improved accuracy slightly but sensitive to noise (Gaussian Noise and Speckle Noise).
    - Accuracy: 0.70.

  - **LBP + HOG + Color Histograms**

    - Adds LBP to the previous combination.
    - No significant improvement over Color Histograms + HOG.
    - Accuracy: 0.78.

  - **ORB (Oriented FAST and Rotated BRIEF)**

    - Similar to SIFT and SURF but more robust
    - Focuses on corner detection, lacks color information.
    - Not suitable due to sensitivity to lighting and texture variations.
    - Accuracy: 0.57.

  - **Bag of Visual Words (BoVW)**

    - Uses SIFT descriptors and clustering.
    - High computational overhead, inefficient.
    - taking over 9 hour

  - **Fourier and Wavelet Transform + PCA**
    - High-dimensional feature space reduced with PCA.
    - Not as effective as HOG and Color Histograms.
    - Accuracy: 0.71.

- **Optimal Feature Extraction Method**
  - **Combination of HOG and Color Histograms**
    - Selected for computational efficiency, robustness, and complementary strengths.
    - Accuracy: 0.78.
    - Captures both structural and color information effectively.

### Model Selection and Training

- **Algorithms Considered**

  - **XGBClassifier (97%)**

    - Selected for superior performance and robustness against overfitting.

  - **Support Vector Machine (SVM) (78%)**

  - **RandomForestClassifier (75%)**

  - **LogisticRegression (71%)**

- **XGBClassifier**

  - Chosen for high accuracy and scalability.
  - Significantly outperformed other algorithms.
    <details>
      <summary>Classification Report</summary>
      <div align="left">
      ![Classification Report](web/img/arif_classification.png)
      </div>
    </details>
    <br>

    <details>
      <summary>Log Los</summary>
      <div align="left">
      ![Log Los](web/img/arif_loglos.png)
      </div>
    </details>
    <br>
    <details>
      <summary>Confusion Matrix</summary>
      <div align="left">
      ![Confusion Matrix](web/img/arif_confusion_matrix.png)
      </div>
    </details>

### Comparison with Pre-trained VGG16 Model

- **Pre-trained VGG16 Model for Feature Extraction**
  - Achieved similar accuracy (~0.97) as XGBClassifier.
  - Less suitable due to computational demands and generalization issues.
  - HOG and Color Histograms method more effective for specific plant disease detection tasks.

### Disclaimer

- **Methodological Limitations**
  - Findings based on limited computational resources and a subset of the dataset.
  - The findings are based on experiments and surface review of existing documentation
  - Future work should explore more algorithms and methodologies.

### Conclusion

- Trained a deep learning model on a subset of the dataset for bench marking.
- Achieved 98.91% validation accuracy.
- Correctly predicted previously misclassified images.
- **Summary**
  - HOG and Color Histograms combination optimal for feature extraction.
  - XGBClassifier significantly improved accuracy.
  - Deep learning model proved most effective with highest accuracy.
