---
Company: NileAGI
comments: The first Malty-Purpose Swahili Language Model
title:  "Rafiki Language Model"
Adress: Kigamboni, Dar es Salaam
date:   August, 2023
---

### RAFIKI LANGUAGE MODEL

> The First Ever Malty-Purpose Swahili Language Model


**Contents**
[Intruduction to Rafiki Language Model](###Intruduction-to-Rafiki-Language-Model)

[Steps Towards Rafiki Language Model](###Steps-Towards-Rafiki-Language-Model)

[Team](###Team)

**State of the Art performance.** By the way, running their method with 1600 centroids gives 77% classification accuracy. If you set the clusters to be random the accuracy becomes 70%, and if you set the clusters to be random patches from the training set, the accuracy goes up to 74%. It seems like the whole purpose of k-means is to nicely spread out the clusters around the data. I'm guessing that the 70% random clusters performance might be because many of the clusters are


### CIFAR-10

> Note, this post is from 2011 and slightly outdated in some places.

<div style="text-align:center;"><img src="/assets/cifar_preview.png"></div>

**Statistics**. CIFAR-10 consists of 50,000 training images, all of them in 1 of 10 categories (displayed left). The test set consists of 10,000 novel images from the same categories, and the task is to classify each to its category. The state of the art is currently at about 80% classification accuracy (4000 centroids), achieved by [Adam Coates et al. (PDF)](http://ai.stanford.edu/~acoates/papers/coatesleeng_aistats_2011.pdf). This paper achieved the accuracy by using whitening, k-means to learn many centroids, and then using a soft activation function as features.

**State of the Art performance.** By the way, running their method with 1600 centroids gives 77% classification accuracy. If you set the clusters to be random the accuracy becomes 70%, and if you set the clusters to be random patches from the training set, the accuracy goes up to 74%. It seems like the whole purpose of k-means is to nicely spread out the clusters around the data. I'm guessing that the 70% random clusters performance might be because many of the clusters are