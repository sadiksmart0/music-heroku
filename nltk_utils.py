import subprocess
import nltk
def utils():
    cmd = ['python', '-m', "import nltk; nltk.download('punkt')"]
    subprocess.run(cmd)