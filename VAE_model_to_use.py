import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import variational_Autoencoder_3 as auto

# Instantiate the autoencoder model
autoencoder = auto.VAE()

# Load the trained weights
autoencoder.load_state_dict(torch.load("./vae_model10lrBBatchB.pth"))

# Set the model to evaluation mode
autoencoder.eval()
