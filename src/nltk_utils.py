import subprocess

def utils():
    cmd = ['python', '-c', "import nltk; nltk.download('punkt')"]
    subprocess.run(cmd)