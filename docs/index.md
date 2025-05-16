---
layout: default
title: Computational social science final project
description: Musician community analysis in Denmark
---


# <span style="color:green"> More about the website</span>

<span style="color:green"> This part of the assignment is quite free. The main point of the website is to present your idea/analyses to the world in a way that showcases your use of what you've learned in class. It can be as simple as an old fashioned static web-page, and as complicated as you want it to be. Let your creativity run wild (but keep in mind that this is not a coding class - we care mostly about content and analysis). </span>

<span style="color:green"> The website should be self-contained and tell the story of your dataset without the need for the Explainer Notebook (the purpose of the notebook is to provide additional details for interested readers). Here are some requirements </span>

- [ ] <span style="color:green"> The page should say clearly what the dataset is and give the reader some idea of its most important properties (kind of Project Assignment A-style).</span>
- [ ] <span style="color:green"> The page should contain your network and text analysis (that's the main part).</span>
- [x] <span style="color:green"> There should be download options for data sets (so the user can play around).</span>
- [x] <span style="color:green"> You must link to the Explainer Notebook (more details below) that explains the details of your analysis (including all of the machine learning, the model selection, etc). You can achieve this with a link to a notebook displaying on the nbviewer.</span>
- [X] <span style="color:green"> For hosting, I recommend using your DTU website or Github pages.</span>

## Table of contents
- [Introduction](#introduction)
- [The dataset](#the-dataset)
- [Network and text analysis](#network-and-text-analysis)
  - [Basic characteristics of the network](#basic-characteristics-of-the-network)
  - [Attribute analysis (genre)](#attribute-analysis-genre)
  - [Community detection](#community-detection)

## Introduction

For this assignment, we investigate the structure of Denmark’s local music scene by building a network that connects musicians to the bands they play with. '
Our goal is to uncover patterns of collaboration, reveal how creative communities form, and perhaps highlight key individuals and groups that act as bridges across different scenes or genres.

To do this, we constructed a bipartite network - a special kind of network made up of two different types of nodes: musicians and bands. 
In our network, musicians are only connected to bands (and not to other musicians directly), and bands are only connected to musicians. From this, we can create two useful views: one where bands are linked if they share members, and another where musicians are linked if they’ve played in the same band.

We collected data on Danish music groups by going through all relevant categories on the Danish Wikipedia, and gathered information about group members either from Wikipedia pages or the music database Discogs when needed. 
Once this data was cleaned and merged, we used it to build the network.

Focusing on Denmark keeps the scope of the project manageable while still offering meaningful insights. 
The final outcome will be this interactive website, where you can explore how artists and bands are interconnected. 


## The Dataset
This project looks into the network of danish music groups, defined by their shared members. All danish music groups are collected from the danish Wikipedia though running thorug all wiki categories of danish groups. The members of the groups are collected from Wikipedia if possible and the music website Discogs otherwise. 
From this data a network is created, edges of the netwoek being a musician being a part of a music group. This means that musicians only connect to groups and vice versa. This create a bipartite network as shown in the figure below (number of nodes not to scale, for better visualisation). For the analysis, we have focused on the projection of the network, onto musicians and groups respectively. This results in a network where groups are connected if they have at least 1 shared member, and musicians are connected if they have been in the same group.
[![Bipartite_network_model.png](assets/images/Bipartite_network_model.png)](https://aaresh1705.github.io/CSS_project_final/network_test.html)

## Network and text analysis
To begin our analysis, we created two projections of the bipartite network: The Danish Music Groups (DMG) network and the Danish Musicians Network. 
Click the links to go to the interactive plots of the networks.

| Network                                                                                      | Average degree               | Size |
|----------------------------------------------------------------------------------------------| ---------------------------- | ---- |
| [Danish Musicians Network](assets/graphs/network.html) | 20.0                         | 4151 |
| [Danish Music Groups (DMG) network](assets/graphs/network.html)                              | 1.36                         | 814  |
| [Bipartite network](assets/graphs/bipartite.html)                                            | Musicians: 1.23  Groups: 5.84| 4931 |

**Danish Musicians Network:** \
The size is how many musicians there are in the network. The degree of a musician tells how many other musicians this musician has a shared music group with. The degree is thereby the number of links to other associated musicians.
The average degree is then the average of all degrees of musicians and tells something about how connected Danish musicians are. So, on average, one musician shares a music group or groups with 20 other musicians.

**The DMG network** \
The size is how many music groups there are in the network. The degree of a group tells how many other groups this group shares a musician with. The degree is thereby the number of links to other associated groups.
The average degree is then the average of all degrees of groups and tells something about how connected Danish musicians are. So, one music group shares one or more musicians with 1.36 other groups on average.

**Bipartite network** \
Here we have two average degrees, one for musicians and one for groups.  This should be interpreted as follows: On average a musician is a part of 1.23 music groups and on average a music group has 5.84 members.

**What is the structure of the projected networks?** \
We see in the interactive plots of the projected networks, some nodes (musicians or music groups) are connected very strongly around the middle. It seems as if the distribution degrees are not random. This is emphasized below for both projected networks, where the distributions are plotted against similar randomly generated networks. The degree distributions both seem to follow a heavy-tailed distribution, where a few nodes have very high degrees and most nodes have degrees below the average. This is a natural structure for social networks, among other things. Especially for the DMG network, we see the emergence of potential hubs in the lower right corner of the degree distribution plot. The largest potential hub group has 23 links and is the large jazz band “Kansas City Stompers”. However, the largest hub group is not guaranteed to be the most central one. Centrality is a more robust measure as it also relies on how connected the linking music groups are (and the links of the linking music groups, and so on). We found that the most central music groups of the DMG network are mostly old Danish bands popular in the 70s and 80s. The most central band is the rock group “Lone Kellermann & Rockbandet”, hence it is not the largest hub. It is a bit surprising that these groups are the most central, given our initial understanding of the music scene. However, since we use Wikipedia articles across time periods it might make sense that the network is biased towards older music groups.


[![Bipartite_network.svg](assets/images/bipartite_network.svg)](assets/graphs/bipartite.html)


### Basic characteristics of the network
### Attribute analysis genre
### Community detection

## Live Graphs

- [Local Music Community Network](assets/graphs/network.html)  
- [Rotatable 3D Plot](assets/graphs/rotatable_plot.html)  

## Downloads
### The dataset
You can download the raw CSV here:\
[⬇️ Download `musicians.csv`](/data/musicians.csv)

Or take a look at here:\
[▶️ View `musicians.csv`](https://github.com/Aaresh1705/CSS_project_final/blob/main/data/musicians.csv)

### The notebook
You can download the notebook here:\
[⬇️ Download `final_notebook.ipynb`](assets/final_notebook.ipynb)

Or take a look here:\
[▶️ View `final_notebook.ipynb`](https://github.com/Aaresh1705/CSS_project_final/blob/main/final_notebook.ipynb)
