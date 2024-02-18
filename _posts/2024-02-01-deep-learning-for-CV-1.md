---
title: Deep Learning for Computer Vision (1)
date: 2024-02-01 01:04:09
img_path: /_posts/
math: true
mermaid: true
tags: CS444
image:
  path: ../upload/img/2024-02-01-deep-learning-for-CV-1-image.png
categories:
- Course Notes
- Deep Learning for CV
---

# CS 444: Deep Learning for Computer Vision Course Notes

### A Taxonomy of Learning Problems

- Learning problems are categorized by the type of output:
  - classification
  - regression
  - structured prediction
  - dense prediction
  - multi-modal prediction
- the type of supervision:
  - fully supervised
  - unsupervised
  - self-supervised
- and the training regime:
  - batch offline learning
  - online/continual learning
  - active learning
  - reinforcement learning

### Topics to be Covered
w
- ML basics, linear classifiers, multilayer neural networks, backpropagation.
- Convolutional networks for classification, networks for detection, dense prediction.
- Self-supervised learning, generative models (GANs, image-to-image translation, diffusion models).
- Deep reinforcement learning, models for sequence data, transformers, large language models, transformers for vision.

## Detailed Topics

### Taxonomy of Learning Problems

- **Type of Output:** Different tasks require different outputs, ranging from simple classifications to complex structured predictions.
- **Type of Supervision:** Covers the spectrum from fully supervised learning, where every piece of training data is labeled, to unsupervised learning, where no labels are provided.
- **Training Regime:** Discusses the methodologies for training models, including batch and online learning, and introduces concepts like active and reinforcement learning.

### Learning Approaches

- **Unsupervised Learning:** Explores clustering, dimensionality reduction, and learning the data distribution through methods like GANs and denoising diffusion probabilistic models (DDPMs).
- **Self-supervised Learning:** Utilizes part of the data to predict other parts, with applications in image colorization, future prediction, and grasp prediction.

### Modern Trends

- **Data Engines:** Describes the evolution of data processing models, highlighting the transition from manual to semi-automatic and fully automatic stages, exemplified by tasks like promptable segmentation.
- **Reinforcement Learning:** Focuses on agents learning to interact with the world through actions, with examples including DeepMind’s AlphaGo and sensorimotor learning for locomotion in challenging terrains.
