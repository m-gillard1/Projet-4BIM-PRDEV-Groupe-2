import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import Variational_Autoencoder_Training as auto

# Instantiate the autoencoder model
autoencoder = auto.VAE()

# Load the trained weights
autoencoder.load_state_dict(torch.load("./vae_model10lrBBatchB.pth"),map_location=torch.device('cpu'))

# Set the model to evaluation mode
autoencoder.eval()

def NumpyEncoding(path_to_imToEncode):
    """
    Encodes an input image into a NumPy array using a pre-trained autoencoder model.

    Args:
        path_to_imToEncode (str): The path to the image file to be encoded.

    Returns:
        numpy.ndarray: The encoded image represented as a NumPy array.

    """
    transform = transforms.ToTensor() # Convert PIL Image to tensor
    image=auto.my_loader_function(path_to_imToEncode)
    image_tensor=transform(image).unsqueeze(0) #add batch dimension
    mean, logvar=autoencoder.encode(image_tensor)
    encoded_image_np=mean.detach().numpy()
    return encoded_image_np

def NumpyDecoding(npToDecode):
    """
    Decodes an encoded image represented as a NumPy array into a PIL image using a pre-trained autoencoder model.

    Args:
        npToDecode (numpy.ndarray): The encoded image represented as a NumPy array.

    Returns:
        PIL.Image.Image: The decoded image as a PIL image.

    """
    transform2 = transforms.ToPILImage()
    encoded_image=torch.from_numpy(npToDecode.astype(np.float32))
    decoded_image=autoencoder.decoder(encoded_image)
    decoded_image_pil=transform2(decoded_image.squeeze(0))

    return decoded_image_pil
