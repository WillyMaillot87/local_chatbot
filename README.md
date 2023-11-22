
Simple Local Chatbot
==============================

This is a simple app using a conversational bot that you can run locally.

- Pre-trained model used : facebook/blenderbot-400M-distill

- The GUI is built with Streamlit.

- The app is fully dockerized.

How to use it ?
------------
After cloning the repository to your machine, run the following command:

`docker image pull willymaillot87/local_chatbot:latest`


`docker container run willymaillot87/local_chatbot:latest`

In your browser, you will have access to the service:
- **streamlit app** at the address **localhost:8501**

It may take a long time to run it for the first time because the app needs to download the pre-trained model.

------------

Project organization
------------

    ├── local_chatbot
        ├── app.py
        ├── check-device.py
        ├── Dockerfile
        ├── LICENSE
        ├── README.md
        ├── requirements.txt

------------