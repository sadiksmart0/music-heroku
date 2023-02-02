import subprocess
cmd = ['python', '-c', "import nltk; nltk.download('punkt')"]
subprocess.run(cmd)