#lpfeifer_x442.3_assignment9.py

'''Question 1
Using os.walk, write a script that will print the filenames of zero length files. 
It should also print the count of zero length files.'''

import os
file_location = '/Users/lpfeifer/code/files'
for root, dirs, files in os.walk(file_location):
    for f in files:
        print(f)
        file_path = os.path.join(root, f)
        size = os.path.getsize(file_path)
        if size == 0:
            print(f, file_path)
        else:
            print("I guess it's not zero")
'''Question 2
Write a script that will list and count all of the images in a given HTML web page/file. You can assume that:
Each image file is enclosed with the tag <img and ends with >
The HTML page/file is syntactically correct'''

#image example <a href="photos.html"  target="display"> ==$0    <im src="images/pete0.png" width="120">    </a>
#list images

import re
from urllib.request import urlopen #open URL Library

def get_image(url): #pass URL through function
    total = 0
    page = urlopen(url).readlines()
    for line in page:
        hit = re.findall('<img.*?>', str(line)) #Using *? matches match only with <a>
        total += len(hit)

    print('{0} Total number of images = {1}'.format(url, total))

get_image("https://ganbreeder.app/")
get_image("https://openai.com/blog/learning-dexterity/")
