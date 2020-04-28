# MSc_Project
# Deep Learning for Parkinson's Disease

Code base is in Jupyter Notebook Files, was originally run in Google Colab for the 
research purposes of completing dissertation project and has not been updated since. 
Warning: It is very messy.

# Abstract (Also in Final Report, Submitted in April 2020)
In this study, we present 3 deep learning classification models in attempt to diagnose Parkinson’s Disease (PD) using patient magnetic resonance imaging (MRI), age and gender data. Our first model is a 2D convolutional neural network (CNN) using MRI data which achieved a maximum accuracy on test set of 100% and 10-fold cross-validated score of 85.23%, so the former exceeds state of the art accuracy from a support vector machine (SVM) classifier with 97.5% accuracy from Adeli et al [1] by 2.5%. The second model is a 3D CNN in which we make an effort to validate the 100% accuracy reported by Soheil et al [2], who also used a 3D CNN. We achieve a cross-validated accuracy of 87.87% and a maximum accuracy of 93.10% on test set and therefore find it plausible. Finally, our tertiary model is an ensembled fully connected neural network (FCNN) using age and gender data, which has yet to be observed in literature and therefore is a novel contribution to achieve a cross-validated accuracy of 74.41% and a maximum accuracy of 81.67%. Thereby, it exceeds current clinical diagnostic accuracy of 73.8% by non-experts in PD [3].

References:
-  [1]: E. Adeli, G. Wu, B. Saghafi, L. An, F. Shi, and D. Shen, “Kernel-based joint feature selection and max- margin classification for early diagnosis of parkinson’s disease,” Scientific Reports (Nature Publisher Group), vol. 7, p. 41069, 01 2017. Copyright - Copyright Nature Publishing Group Jan 2017; Last updated - 2017-08-18.
-  [2]:S. Esmaeilzadeh, Y. Yang, and E. Adeli, “End-to-end parkinson disease diagnosis using brain mr-images by 3d-cnn,” ArXiv, vol. abs/1806.05233, 06 2018
-  [3]: G. Rizzo, M. Copetti, S. Arcuti, D. Martino, A. Fontana, and G. Logroscino, “Accuracy of clinical diagnosis of parkinson disease,” Neurology, vol. 86, no. 6, pp. 566–576, 2016.