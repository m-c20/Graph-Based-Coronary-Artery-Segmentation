Coronary Artery Segmentation Using a Graph-Based Method
Overview

This repository contains a Python implementation of VesselWalker, a traditional graph-based algorithm for coronary artery segmentation in 2D X-ray angiograms. The project revisits a non–deep learning approach to vessel segmentation, emphasizing computational efficiency, interpretability, and reproducibility.

The implementation is evaluated on a large, publicly available coronary angiography dataset and compared against ground-truth annotations as well as the original MATLAB implementation.

Method

The core segmentation method is based on the VesselWalker algorithm, which models vessel extraction as a graph traversal problem. Unlike deep learning approaches, this method does not require training data and provides transparent decision-making at each step of the segmentation process.

Dataset

Experiments are conducted using a publicly available coronary angiography dataset. The dataset is chosen for its size, annotation quality, and accessibility. Ground-truth vessel annotations are used for quantitative evaluation.
