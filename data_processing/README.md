# CPSC490 - EngagementApp [Data Processing]

This folder contains all the necessary code and functions for running data processing for the EngagementApp model.

## Step One [Virtual Environment]

Make sure you create a virtual environment for this folder. 

```bash
python3 -m venv .
```

If the above command does not work, you may use the [following link](https://docs.python.org/3/library/venv.html) to assist you.

Once the virtual environment is created, activate the virtual environment by running the following command, assuming you are still in the data_processing folder.

```bash
source ./bin/activate
```

## Step Two [Packages]

Now, you will need to download the required packages with the following command:

```bash
pip3 install -r ./requirements.txt
```

If this does not work, the following packages should at least be required to run the files in this folder:
```bash
pip3 install moviepy
pip3 install pytube
pip3 install opencv-python
pip3 install tqdm
```

If that still does not work, here is an exhaustive list of packages needed:
- moviepy
- pytube
- opencv-python
- tqdm
- shutil
- os
- csv
- datetime

## Step Three [Get Clips]

In the terminal, you may run:
```bash
python3 clip_csv.py
```

to begin the clip_csv process. You may notice 6 CSV files in the folder: education[0/1].csv, sports[0/1].csv, and politics[0/1].csv. Each csv contains links to Youtube videos and timestamps of clips to snip from. What should result from running the above file is the videos folder containing all unique videos found in the 6 CSV files, as well as the processed clips in the clips folder. 

## Step Four [Get Frames]

Go to data_loader.ipynb. You may be prompted to run the kernel to begin running the jupyternotebook. Click on PythonEnvironments, then click on your virtual environment. You may be required to install the ipykernel package. After that, click on the run all option at the top to run all the cells in data_loader.ipynb. This should result in the frames folder being populated with folders of clip frames, and the scores.txt and paths.txt text files being updated.