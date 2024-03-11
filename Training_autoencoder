import torch
import torch.nn as nn
from PIL import Image
import torch.optim as optim
import torchvision.datasets as datasets
import torchvision.transforms as transforms

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),
            nn.ReLU()
            #MaxPool ?
        )
        # Define decoder layers
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(256, 128, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 1, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.encoder(x) 
        x = self.decoder(x) 
        return x 

def my_loader_function(path):
    """
    Custom loader function to open an image file from the given path.

    Args:
        path (str): The path to the image file.

    Returns:
        PIL.Image.Image: The opened image object.
    """
    return Image.open(open(path, 'r+b'))

def train_autoencoder(model, train_loader, criterion, optimizer, num_epochs=50):
    """
    Trains the autoencoder model.

    Args:
        model (nn.Module): Autoencoder model.
        train_loader (torch.utils.data.DataLoader): DataLoader for training data.
        criterion (torch.nn.modules.loss._Loss): Loss function.
        optimizer (torch.optim.Optimizer): Optimizer for model parameters.
        num_epochs (int): Number of epochs to train the model.

    Returns:
        None
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print("Training on:", device)
    model.to(device)

    for epoch in range(num_epochs):
        for data in train_loader:
            img, _ = data
            img = img.to(device)
            optimizer.zero_grad()
            output = model(img)
            loss = criterion(output, img)
            loss.backward()
            optimizer.step()

        if epoch % 5 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

def main():
    """
    Main function to train and save the autoencoder model.
    """
    # Initialize the autoencoder
    model = Autoencoder()

    # Define transform
    transform = transforms.ToTensor()

    # Load dataset
    train_dataset = datasets.ImageFolder(root="C:/Users/thiba/Documents/INSA_2023-2024/S2/Software_dev/ImagesClassées/train_data_0_23999", transform=transform, loader=my_loader_function)
    #the autoencoder has been trained on local due to the size of the dataset not supported by git hence the 
    # Define the dataloader
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

    # Define the loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Train the autoencoder
    train_autoencoder(model, train_loader, criterion, optimizer)

    # Save the model
    torch.save(model.state_dict(), 'conv_autoencoder.pth')

if __name__ == "__main__":
    main()
