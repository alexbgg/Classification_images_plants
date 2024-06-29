# Interpretability 🍃
## *target model*: our 🥇-performing fine-tuned MobileNetV2
### Why?
- Frankly, we can't believe Google makes great things for free 😉
- Furthermore, we wanna gain more insight 🧐 into what makes our fine-tuned winner model a true champ
- More specifically, we'd like to know why our champ makes a certain class prediction when served with a certain input image
- Ideally, we want to get this visual inspection performed pixel-wise
- Ultimately, we're curious to learn 🔍 which pixels/regions of the input image affected prediction the most

### Which?
- Following the logical thread pinned above, we reduce our interpretability goals down to so called *"pixel/feature attribution methods"*
- Yes, this topic is theoretically well-studied 📰, but practically poorly-implemented for custom-made models - so, we've filled this gap 💻
- Just like no one payed royalties 💰 to the Eulers for using his theorems for RSA encryption methods, we did the same & implemented (Guided) Grad-CAM
- **Grad-CAM** stands for "gradient-weighted class activation map" and represents (in our case, bilinearly interpolated) heatmaps overlayed on the input image
- **Guided Grad-CAM** results in blending of so called SM (saliency maps), which are as fine-grained as input images, with the interpolated Grad-CAM heatmaps
- Mathematical <ins>similarity</ins> of both methods is the usage of gradients of the classification score
- Mathematical <ins>dissimilarity</ins> of both methods lies in different differentiation domains (Grad-CAM - last convolutional layer output, SM - input image) 

### Grad-CAM
<details>
  <summary>some examples of well-interpreted [<span style="color:red">mis</span>]behaviour of our winner model nicknamed <i>BeLu</i></summary>
  <div align="left">
  ![Technical summary of model](web/img/grad_cam.png)
  </div>
</details>
<br>

### Guided Grad-CAM
<details>
  <summary>some examples of well-interpreted [<span style="color:red">mis</span>]behaviour of our winner model nicknamed <i>BeLu</i></summary>
  <div align="left">
  ![Technical summary of model](web/img/guided_grad_cam.png)
  </div>
</details>
<br>

### Mathematical Backbone 😱
<details>
  <summary>📢 expand at your own risk [<span style="color:red">irrelevance alert</span>]</summary>
  <object data="http://nuclear.ucdavis.edu/~tgutierr/files/sml2.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="http://nuclear.ucdavis.edu/~tgutierr/files/sml2.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="http://nuclear.ucdavis.edu/~tgutierr/files/sml2.pdf">Download PDF</a>.</p>
    </embed>
  </object>
</details>
<br>

### Conclusion
All in all, talking in the language of inferential statistics, carried out interpretability analysis gave us no evidence to vacate the champion's belt

***