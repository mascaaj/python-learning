# OpenCV learning via Udemy Course

## Git flow and versioning

Abject laziness reduced the want to create a new repo.
This repo will have the following structure

```
            develop
    master   |  opencv_develop
        |    |     |
        |    |    /
        |    |___/
        |    |
        |    | 
        |   /
        |  /
        |_/
        |
        |
```

All open cv relate work will branch off opencv_develop.
It will merge back to develop and eventually to master.

## Environment

Setting up this environment should have been straight forward. However due to the raspi 4 being the current dev machine, the environment could not be what was recommended by the course.

Both ```conda env list``` and ```pip freeze``` have been placed in the root folder as ```.yaml``` and ```.txt``` files respectively.

## Current source information :

Course : https://www.udemy.com/course/python-for-computer-vision-with-opencv-and-deep-learning/

``` 
    startconda #alias
    conda activate cvcourse
```
