# Underwater Scene Prior Inspired Deep Underwater Image and Video Enhancement
This repository is for Underwater Scene Prior Inspired Deep Underwater Image and Video Enhancement (UWCNN) introduced in the following paper

# Paper
[Chongyi Li](https://li-chongyi.github.io/),  [Saeed Anwar](https://saeed-anwar.github.io/),  [Fatih Porikli](http://www.porikli.com), ["Underwater Scene Prior Inspired Deep Underwater Image and Video Enhancement"](https://www.sciencedirect.com/science/article/pii/S0031320319303401), Pattern Recognition, 2019. [[arxiv]](https://arxiv.org/pdf/1807.03528.pdf).

 ## Contents
1. [Introduction](#introduction)
2. [Network](#network)
3. [Test](#test)
4. [Datasets](#datasets)
5. [Results](#results)
6. [Citation](#citation)

## Introduction
In underwater scenes, wavelength-dependent light absorption and scattering degrade the visibility of images and videos. The degraded underwater images and videos affect the accuracy of pattern recognition, visual understanding, and key feature extraction in underwater scenes. In this paper, we propose an underwater image enhancement convolutional neural network (CNN) model based on underwater scene prior, called UWCNN. Instead of estimating the parameters of underwater imaging model, the proposed UWCNN model directly reconstructs the clear latent underwater image, which benefits from the underwater scene prior which can be used to synthesize underwater image training data. Besides, based on the light-weight network structure and effective training data, our UWCNN model can be easily extended to underwater videos for frame-by-frame enhancement. Specifically, combining an underwater imaging physical model with optical properties of underwater scenes, we first synthesize underwater image degradation datasets which cover a diverse set of water types and degradation levels. Then, a light-weight CNN model is designed for enhancing each underwater scene type, which is trained by the corresponding training data. At last, this UWCNN model is directly extended to underwater video enhancement. Experiments on real-world and synthetic underwater images and videos demonstrate that our method generalizes well to different underwater scenes. The underwater types and corresponding values are given below.

<p align="center">
  <img width="700" src="https://github.com/saeed-anwar/UWCNN/blob/master/Figs/Types.png">
</p>

<p align="center">
  <img width="700" src="https://github.com/saeed-anwar/UWCNN/blob/master/Figs/Types_table.png">
</p>

## Network
<p align="center">
  <img width="600" src="https://github.com/saeed-anwar/UWCNN/blob/master/Figs/Net.png">
</p>


## Test
### Requirements
python = 3.5 <br/>
tensorflow =1.0.0 <br/>
scipy=1.1.0 (required) <br/>
Tested with tensorflow = 1.14.0 and python 3.6 <br/>
### Quick start

1. The trained models are in 'checkpoint/coarse_230/'
2. Choose the needed model (For example, if you need the type 1 model, please put 'model_checkpoint_path: "coarse.model-type1"' on the first line of checkpoint text.If you are using existing checkpoint text then model in the last line will be loaded(coarse.model-typeII))
3. Put the test images into 'test_real'

   **Use the following to test the algorithm**

    ```
    Python main_test.py
    ```
4. Find the results in 'test_real'


## Datasets
### Synthesized
To synthesize underwater image degradation datasets, we use the attenuation coefficients described in Table 1 for the different water types of oceanic and coastal classes (i.e., I, IA, IB, II, and III for open ocean waters, and 1, 3, 5, 7, and 9 for coastal waters). Type-I is the clearest and Type-III is the most turbid open ocean water. Similarly, for coastal waters, Type-1 is the clearest and Type-9 is the most turbid. We apply Eqs (1) and (2) (please check the paper) to build ten types of underwater image datasets by using the RGB-D NYU-v2 indoor dataset which consists of 1449 images. To improve the quality of datasets, we crop the original size (480x640) of NYU-v2 to 460x620. This dataset is for non-commercial use only. The size of each dataset is **1.2GB**

Type-I:   [[Baidu]](https://pan.baidu.com/s/13k3qNGG93aFwdthjRtxi3Q)

Type-IA:  [[Baidu]](https://pan.baidu.com/s/13lRAbZYyYLyb-Z8qcpW-4Q)

Type-IB:  [[Baidu]](https://pan.baidu.com/s/12qXACo20C6ee9bViItZAFA)

Type-II:  [[Baidu]](https://pan.baidu.com/s/1iZM9md_mdeHXqw3XchvKHg)

Type-III: [[Baidu]](https://pan.baidu.com/s/1fIKVcvU6jg5Mi0Sw-k8VmA)

Type-1:   [[Baidu]](https://pan.baidu.com/s/1V10iXd9QnFbevm17Ua0jwQ)

Type-3:   [[Baidu]](https://pan.baidu.com/s/1DEI4T700jmU-cUYgAxRQAw)

Type-5:   [[Baidu]](https://pan.baidu.com/s/1jlPodNRPqySGnFxr7-qRRg)

Type-7:   [[Baidu]](https://pan.baidu.com/s/12l0gCsPYOtEx7hCvp9C-fw)

Type-9:   [[Baidu]](https://pan.baidu.com/s/1IPKimxXA1CsX3wjRE4VYNQ)

## Results

### Quantitative Results
<p align="center">
  <img width="700" src="https://github.com/saeed-anwar/UWCNN/blob/master/Figs/Test_table.png">
</p>
The performance of state-of-the-art algorithms on widely used publicly available datasets in terms of PSNR (in dB), MSE and SSIM. The best results are highlighted in bold.

### Synthetic Visual  Results
![Visual_Synthetic](/Figs/Synth.png)
(a) Raw underwater images. (b) Results of RED [21]. (c) Results of UDCP [22]. (d) Results of ODM [25]. (e) Results of UIBLA [26]. (f) Our results. (g) Ground truth. The types of underwater images in the first column from top to bottom are Type-1, Type-3, Type-5, Type-7, Type-9, Type-I, Type-II, and Type-III. Our method removes the light absorption effects and recovers the original colors without any artifacts.

### Real Visual  Results

![Visual_Real](/Figs/Real.png)

(a) Real-world underwater images. (b) Results of RED [21]. (c) Results of UDCP [22]. (d) Results of ODM [25]. (e) Results of UIBLA [26]. (f) Results of our UWCNN. (g) Results of our UWCNN+. Our method (i.e., UWCNN and UWCNN+) produces the results without any visual artifacts, color deviations, and over-saturations. It also unveils spatial motifs and details.

### Video Visual  Results
![Visual_VideoFrames](/Figs/Videoframes.png)
(a) Raw underwater video (from top to bottom are frame 1, frame 2, frame 3, frame 4, frame 29, and frame 54 in this video). (b) Results of RED [21]. (c) Results of UDCP [22]. (d) Results of ODM [25]. (e) Results of UIBLA [26]. (f) Results of our UWCNN.

## Citation
If you find the code helpful in your resarch or work, please cite the following papers.
```
@article{Anwar2019UWCNN,
  title = "Underwater scene prior inspired deep underwater image and video enhancement",
  journal = "Pattern Recognition",
  volume = "98",
  pages = "107038",
  year = "2020",
  issn = "0031-3203",
  doi = "https://doi.org/10.1016/j.patcog.2019.107038",
  url = "http://www.sciencedirect.com/science/article/pii/S0031320319303401",
  author = "Chongyi Li and Saeed Anwar and Fatih Porikli",
}

@article{anwar2019diving,
  title={Diving Deeper into Underwater Image Enhancement: A Survey},
  author={Anwar, Saeed and Li, Chongyi},
  journal={arXiv preprint arXiv:1907.07863},
  year={2019}
}
```
