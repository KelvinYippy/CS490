# CPSC490 - EngagementApp [Data]

This folder contains all data relevant to the EngagementApp.

The videos folder contains all the videos in which we are getting the clips from.

The clips folder contains all the three-to-five-second clips that we have collected timestamps of from the videos. They are divided into categories of education, politics, and sports. Each category is further divided into a folder of 0 or 1.

The frames folder contains all of the frames we have subsampled from the clips. They are divided into a folder of 0 or 1.

The files folder contains the paths.txt and scores.txt text files, a logs folder logging all the errors, as well as a model folder containing all our saved models and optimizers used. paths.txt contains a list of folder paths, where each folder path points to the folder of frames for a particular clip. scores.txt contains the corresponding label for such folder. Logs folder will contain logs of any errors that have occurred while downloading. Model folder contains all past optimizers and models that have been trained.