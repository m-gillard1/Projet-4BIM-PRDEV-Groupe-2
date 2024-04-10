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

def NumpyEncoding(path_to_imToEncode):

    # Define transformations to be applied to new data samples
    transform = transforms.ToTensor() # Convert PIL Image to tensor
    image=auto.my_loader_function(path_to_imToEncode)
    image_tensor=transform(image).unsqueeze(0) #add batch dimension
    mean, logvar=autoencoder.encode(image_tensor)
    encoded_image_np=mean.detach().numpy()
    return encoded_image_np
