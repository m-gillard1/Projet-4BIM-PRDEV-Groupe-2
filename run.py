import subprocess

def run()
  commande = "pip install -r requirements.txt"
  subprocess.run(commande, shell=True)
  import main_sprint1
  import Algo_gen
  import Autoencoder_to_use
  import Training_autoencoder
  import interface
