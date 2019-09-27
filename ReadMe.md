# Underwater Scene Prior Inspired Deep Underwater Image and Video Enhancement
This repository is for Underwater Scene Prior Inspired Deep Underwater Image and Video Enhancement (UWCNN) introduced in the following paper

# Paper
[Chongyi Li](https://li-chongyi.github.io/),[Saeed Anwar](https://saeed-anwar.github.io/),  [Fatih Porikli](porikli.com), ["Underwater Scene Prior Inspired Deep Underwater Image and Video Enhancement"](https://www.sciencedirect.com/science/article/pii/S0031320319303401), Pattern Recognition, 2019. [[arxiv]](https://arxiv.org/pdf/1807.03528.pdf).

 ## Contents
1. [Introduction](#introduction)
2. [Network](#network)
2. [Train](#train)
3. [Test](#test)
4. [Datasets](#datasets)
5. [Results](#results)
6. [Citation](#citation)
7. [Acknowledgements](#acknowledgements)

## Introduction
In underwater scenes, wavelength-dependent light absorption and scattering degrade the visibility of images and videos. The degraded underwater images and videos affect the accuracy of pattern recognition, visual understanding, and key feature extraction in underwater scenes. In this paper, we propose an underwater image enhancement convolutional neural network (CNN) model based on underwater scene prior, called UWCNN. Instead of estimating the parameters of underwater imaging model, the proposed UWCNN model directly reconstructs the clear latent underwater image, which benefits from the underwater scene prior which can be used to synthesize underwater image training data. Besides, based on the light-weight network structure and effective training data, our UWCNN model can be easily extended to underwater videos for frame-by-frame enhancement. Specifically, combining an underwater imaging physical model with optical properties of underwater scenes, we first synthesize underwater image degradation datasets which cover a diverse set of water types and degradation levels. Then, a light-weight CNN model is designed for enhancing each underwater scene type, which is trained by the corresponding training data. At last, this UWCNN model is directly extended to underwater video enhancement. Experiments on real-world and synthetic underwater images and videos demonstrate that our method generalizes well to different underwater scenes

## Datasets
### Synthesized
To synthesize underwater image degradation datasets, we use the attenuation coefficients described in Table 1 for the different water types of oceanic and coastal classes (i.e., I, IA, IB, II, and III for open ocean waters, and 1, 3, 5, 7, and 9 for coastal waters). Type-I is the clearest and Type-III is the most turbid open ocean water. Similarly, for coastal waters, Type-1 is the clearest and Type-9 is the most turbid. We apply Eqs (1) and (2) (please check the paper) to build ten types of underwater image datasets by using the RGB-D NYU-v2 indoor dataset which consists of 1449 images. To improve the quality of datasets, we crop the original size (480*640) of NYU-v2 to 460*620.
This dataset is for non-commercial use only.

