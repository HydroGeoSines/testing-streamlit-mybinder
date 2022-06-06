from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    #Popen(["streamlit", "hello", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
    Popen(["streamlit", "run", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False", "st_test.py"])
