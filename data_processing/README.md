THINGS TO DO:

- Under constants.py, you may see something like this:

```python
MAIN_PATH = "/Users/kelvinyip7/Desktop/Code/CS490/data"
```

Replace the beginning section, "/Users/kelvinyip7/Desktop/Code/CS490", with wherever you are storing this repository. This acts as the main path for where you are going to store your data.

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
pip3 install movie.py
pip3 install pytube
pip3 install 
```


Go to clip_csv.py. 