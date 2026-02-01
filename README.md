# Graph-Based Coronary Artery Segmentation in X-Ray Angiography
**Project Proposal COMP396**  
**Author:** Mert Cezar (261166600)

---

## Proposed Abstract
Accurate segmentation of coronary arteries (CA) is an important step in detecting abnormalities from 2D X-ray angiograms. While there are many existing deep learning methods that tackle these challenges ([Padariya et al., 2025](https://www.sciencedirect.com/science/article/pii/S0952197625022250), [Li et al., 2024](https://www.mdpi.com/2079-9292/13/18/3676), [Gao et al., 2022](https://doi.org/10.1186/s12880-022-00734-4), [Nobre Menezes et al., 2022](https://www.sciencedirect.com/science/article/pii/S0870255122001354)), this project aims at revisiting and enhancing an existing graph-based method ([M’hiri et al., 2013](https://doi.org/10.1109/ISBI.2013.6556625)) considered as "traditional image processing" as opposed to deep learning methods, which could be preferred for segmentation due to its computational efficiency and interpretability.

---

## Model
The base model that will be used is **VesselWalker** ([M’hiri et al., 2013](https://doi.org/10.1109/ISBI.2013.6556625)). Its traditional image processing approach is computationally efficient and interpretable.

---

## Dataset
The dataset used to test the model is obtained from [Popov et al., 2024](https://doi.org/10.5281/zenodo.10390295) due to its large size and public availability.

---

## Procedure
1. Implement the VesselWalker algorithm in Python.  
2. Apply preprocessing to the dataset to normalize image contrast and remove noise.  
3. Run the model on the preprocessed dataset.  
4. Compare segmentation outputs with ground truth annotations.  
5. Evaluate performance using metrics such as Dice score, sensitivity, and specificity.  
6. Compare results to the original MATLAB implementation to validate correctness.

---

## Literature Review
Five papers were read to get acclimated to the subject. Key points from each paper are summarized below:

1. **[Li et al., 2024](https://www.mdpi.com/2079-9292/13/18/3676)**: Focused on deep-learning techniques for coronary artery stenosis detection using Hessian-based Frangi vesselness (HFV) and image fusion. Training deep learning models on fusion images improved accuracy by ~5% with minimal latency loss. The $AP_{50}(\%)$ value peaked at the LCA zero angle.

2. **[Lalinia & Sahafi, 2024](https://doi.org/10.1007/s11220-024-00481-6)**: Introduced an edge-based tracking approach for coronary vessel segmentation in X-ray angiography, using preprocessing (guided filtering, edge-sharpening) to enhance image features. Reported Dice score: 81.79%, Sensitivity: 86.93%, Accuracy: 97.81%.

3. **[Gao et al., 2022](https://doi.org/10.1186/s12880-022-00734-4)**: Proposed an ensemble framework using deep learning and filter-based features with Gradient Boosting Decision Trees (GBDT) and Deep Forest classifiers. Best GBDT model: F1=0.874, AUROC=0.947, Sensitivity=0.902, Specificity=0.992. Best Deep Forest model: F1=0.867, AUROC=0.95, Sensitivity=0.867, Specificity=0.993.

4. **[Padariya et al., 2025](https://www.sciencedirect.com/science/article/pii/S0952197625022250)**: Designed an end-to-end pipeline (CASBloDaM) for coronary artery segmentation, blockage detection, and measurement. Reported segmentation metrics: Accuracy=0.985, Specificity=0.913, Sensitivity=0.847, Dice=0.989. Blockage detection: Accuracy=72.5%, Precision=66.2%, Recall=91.1%, F1=76.6%.

5. **[Nobre Menezes et al., 2022](https://www.sciencedirect.com/science/article/pii/S0870255122001354)**: Developed U-Net based AI models for CAG segmentation and introduced a Global Segmentation Score. Reported generalized Dice Score: 0.9234 (baseline), 0.9348 (enhanced AI model).

---

## References
- [Nobre Menezes et al., 2022](https://www.sciencedirect.com/science/article/pii/S0870255122001354) – Development of deep learning segmentation models for coronary X-ray angiography.
- [M’hiri et al., 2013](https://doi.org/10.1109/ISBI.2013.6556625) – VesselWalker: Coronary arteries segmentation using random walks and Hessian-based vesselness filter.
- [Padariya et al., 2025](https://www.sciencedirect.com/science/article/pii/S0952197625022250) – A novel deep learning pipeline for coronary artery analysis in X-ray angiography.
- [Popov et al., 2024](https://doi.org/10.5281/zenodo.10390295) – Dataset for Automatic Region-based Coronary Artery Disease Diagnostics.
- [Li et al., 2024](https://www.mdpi.com/2079-9292/13/18/3676) – Hessian-Based Deep Learning Preprocessing Method for Coronary Angiography.
- [Gao et al., 2022](https://doi.org/10.1186/s12880-022-00734-4) – Vessel segmentation using ensemble methods with deep learning and filter-based features.
- [Lalinia & Sahafi, 2024](https://doi.org/10.1007/s11220-024-00481-6) – Coronary Vessel Segmentation Using Edge-Based Tracking.

