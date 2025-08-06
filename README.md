# BlueberryOnMars


![](https://img.shields.io/badge/numpy-1.21.5-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/pandas-1.3.5-informational?style=plastic&logo=appveyor)


<img src="https://github.com/LynHJ/BIueberryOnMars/blob/fbb3afe79110170c4a06553668c161140c451044/Resources/spherules.jpg"  width="1200" height="400" />

## Background

**BlueberryOnMars** project led by Dr. Jones aims to target spherules on Mars. During the Curiosity Rover's more than 4,000 mission days on Mars, it has continuously supported us in studying the paleoenvironment on Mars. We will focus on Hematite spherules(blueberries), as they are iron oxides and normally precipitate from aqueous fluids, like water. It could be indirect evidence to indicate that the locations where we found hematite spherules might have been habitable in the past. Curiosity Rover has many types of cameras that serve different research purposes. Higher resolution photos taken from Mastcam-100 (Right Eye) were chosen to identify hematite spherules in the photos. 

## Time Log
<ins>29/07/25</ins>&emsp;I found that the website only allows me add 500 photos at a time to the cart for the downloading. If the number of photos taken in a day excess 500, I will not be able to download all of them. Therefore I applied more filter options(Set Filter to only *0* for colour photos; Set photo types to only *Losslessly Compressed 8 Bit Image*) to ensure that the number of daily photo is fewer than 500. <br/>
<br/>
<ins>01/08/25</ins>&emsp;Had download all the photos. <br/>
<br/>
<ins>06/08/25</ins>&emsp;Tried few ways (cv2, pillow, numpy) to convert .img file format into .png. I was failed. As a result, I changed the photo types to E(JPEG 422 Image) to ensure that I can process images easily later. <br/>


## About  

Ideally, this project will have two phases. The first phase is to categorise photos taken by Curiosity Rover's  Mastcam-100 (Right Eye) into contains Hematite spherules and not contains Hematite spherules. The second phase is to use supervised machine learning to automate our task after the catalogue contains sufficient data. 


*PHASE 1:*<br />
Prepareing:<br />
&emsp;  From [Curiosity (MSL) Analyst's Notebook](https://an.rsl.wustl.edu/msl/AN/an3.aspx)<br />
&emsp;  Set data range<br />
&emsp;  Result view : Observation groups<br />
&emsp;  Instrument: Mastcam<br />
&emsp;  Eye: Right<br />
&emsp;  Filter: 0<br />
&emsp;  Type:E(JPEG 422 Image)<br />

Recording:<br />
&emsp;  Write a log.py to note down photo details (contains/not contains, sol day, photo codes..,etc) and export as a CSV file<br />


*PHASE 2:* <br />
&emsp;  TBC

   
## Summary



## Content
```
Project  
├── README.md
└── Resources
    └── pherules.jpg 
``` 

## Installation

pip install -r requirements.txt


## Reference

1. https://science.nasa.gov/resource/martian-blueberries-2/ 
2. https://an.rsl.wustl.edu/msl/AN/an3.aspx
3. https://www.digitalocean.com/community/tutorials/
4. https://an.rsl.wustl.edu// 
5. K. Misra, A., & E. Acosta-Maeda, T. (2018). Hematite Spherules on Mars. IntechOpen. doi: 10.5772/intechopen.82583 











