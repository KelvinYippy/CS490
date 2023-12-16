# CPSC490 - EngagementApp [Running the Model]

This folder contains all the necessary code and functions for training the EngagementApp model.

## Step One [Virtual Environment]

Make sure you create a virtual environment for this folder. 

```bash
python3 -m venv .
```

If the above command does not work, you may use the [following link](https://docs.python.org/3/library/venv.html) to assist you.

Once the virtual environment is created, activate the virtual environment by running the following command, assuming you are still in the model folder.

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
pip3 install torch
pip3 install glob
pip3 install opencv-python
pip3 install numpy
pip3 install natsort
pip3 install tqdm
pip3 install tensorboard
pip3 install torchvision
```

If that still does not work, here is an exhaustive list of packages needed:
- torch
- glob
- opencv-python
- numpy
- natsort
- tqdm
- tensorboard
- torchvision

## Step Three [Train the Model]

Go to run_model.ipynb. You may be prompted to run the kernel to begin running the jupyternotebook. Click on PythonEnvironments, then click on your virtual environment. You may be required to install the ipykernel package. After that, click on the run all option at the top to run all the cells in run_model.ipynb. This should result in the model being trained, with the training loss, test loss, and test accuracy printed after each epoch. You will also have access to tensorboard to view the loss data in a more nicer format. A thing to note is:

```python
# You may choose to run a new model, in which case call the following line.
model = VideoClassifier(num_classes=2)  # Assuming 10 classes, just need 1 as is binary classification

# You might also want to load an existing model, in which case use the following line, and replace inside torch.load() the path of where you store the model.
# model = torch.load("/content/drive/MyDrive/Colab Notebooks/CPSC 490/models/model_0028.pt")
```

You have the choice to either use a new VideoClassifier or load an existing one.