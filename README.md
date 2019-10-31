# MTHE493
Group 10, Project B2.

## Setting Up

If you want to use a python environment for the project feel free. I am trying to work on this myself so I will be using conda to manage my environment. You can download conda [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). To set up a new conda environment and add the required packages use the following commands:
```
conda create --name 493 # Or whatever you want to name it
source activate 493
pip install -r requirements.txt # Must be in the MTHE493 folder
```

Shoot me a message if you have issues with this, its not entirely necessary but can help keep things clean. If you don't want to use conda, just make sure you run the last line of the code above so you have all the required python packages.

## What we have so far

Currently the `src/` folder only contains a single helper file. [`videoToImage`](src/videoToImage.py). I modifed this from a medium article to allow us to make easy image sequences from chosen videos. The function `getVideoFrames` will take a given video file name (must be in the `videos/` directory!) and capture a frame every 0.5 seconds and save them as images in `images/filename/`.
