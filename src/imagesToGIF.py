import imageio
import os
import re
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]

"""
Put the directory in line 13, output directory on line 21
"""

filenames = os.listdir("Transitions")
filenames.remove(".DS_Store")
filenames.sort(key=natural_keys)
images = []
for file in filenames:
    if ".png" in file:
        print(file)
        images.append(imageio.imread("Transitions/{}".format(file)))
imageio.mimsave('Transitions/movie.gif', images, duration=0.25)
