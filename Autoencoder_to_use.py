import Training_autoencoder as autoE
import torch
from torchvision import transforms
from PIL import Image
import numpy as np

def NumpyEncoding(imToEncode):
    """
    Encodes an image using a pre-trained autoencoder model and returns the encoded image as a NumPy array.

    Args:
        imToEncode (str): The path to the image file to encode.

    Returns:
        numpy.ndarray: The encoded image as a NumPy array.
    """
    

    # Instantiate the autoencoder model
    autoencoder = autoE.Autoencoder()

    # Load the trained weights
    autoencoder.load_state_dict(torch.load("conv_autoencoder.pth"))

    # Set the model to evaluation mode
    autoencoder.eval()

    # Define transformations to be applied to new data samples
    transform = transforms.ToTensor() # Convert PIL Image to tensor

    #Open the image
    image=autoE.OpenImage(imToEncode)

    #Tranform to a tensor adding batch dimension
    image_tensor=transform(image).unsqueeze(0)

    #Encode the image 
    encoded_image=autoencoder.encoder(image_tensor)

    #Tranform it to a Numpy Array
    encoded_image_np=encoded_image.detach().numpy()

    return encoded_image_np

def NumpyDecoding(npToDecode):
    """
    Decodes a NumPy array using a pre-trained autoencoder model and returns the decoded image.

    Args:
        npToDecode (numpy.ndarray): The NumPy array to decode.

    Returns:
        PIL.Image.Image: The decoded image as a PIL Image object.
    """

    # Instantiate the autoencoder model
    autoencoder = auto.Autoencoder()

    # Load the trained weights
    autoencoder.load_state_dict(torch.load("conv_autoencoder.pth"))

    # Set the model to evaluation mode
    autoencoder.eval()

    #Define the tranform
    transform2 = transforms.ToPILImage()

    #Tranform the np array back into a torch 
    encoded_image=torch.from_numpy(npToDecode.astype(np.float32))

    #Decode it 
    decoded_image=autoencoder.decoder(encoded_image)

    #Tranform it as an image (removing batch dimension)
    decoded_image_pil=transform2(decoded_image.squeeze(0))

    return decoded_image_pil
