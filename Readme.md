# Yoga tutor streamlit app

### Setting up - Docker method (Preferred)

1) Install Docker.
2) Clone this repository.
3) Open a terminal in the cloned directory.
4) Run the docker command: ```docker run -p 8501:8501 -it $(sudo docker build -q .)```
5) Open the link http://localhost:8501 in the browser.


### Setting up - Normal Python

1) Install Docker.
2) Clone this repository.
3) Open a terminal in the cloned directory.
4) Run command: ```pip install -r requirements.txt```
5) Run ```streamlit run app.py```
6) Open the link http://localhost:8501 in the browser.

#### Registering new poses

1) Perform the installation steps above
2) Run ```python pose_recorder.py --img_path <image path> --posename <pose name>```