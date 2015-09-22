This code is implemented in python with opencv. 

assignment2.py < --- driver code


Steps of the algo - 
Frames from the video is extracted. 
The first frame selects the object to be tracked. (in this case car). This value is hardcoded. 
The object tracked is compared in all frames using meanshift algorithm.
 
Rectangle is drawn at the tracked window. 


Instructions for running the code- 

1 - Download the code and ensure that the input video is in the same folder as the code 
2 - You can change the hard coded values to change the object to be tracked. 
3 - Install python-numpy and python-opencv
4 - Command to run the file - python assignment2.py  


Note - 
Opencv2 code (assignment2.py) is running completly. 
