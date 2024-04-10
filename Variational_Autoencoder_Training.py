import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.autograd import Variable
from PIL import Image

class Reshape(nn.Module):
    def __init__(self, *shape):
        super(Reshape, self).__init__()
        self.shape = shape

    def forward(self, x):
        return x.view(*self.shape)

class VAE(nn.Module):
    def __init__(self, latent_dim):
        super(VAE, self).__init__()
        self.latent_dim = latent_dim

        # Encoder layers
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32,64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(64,128, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(128,256, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
        )

        # Mean and log variance layers
        self.fc_mean = nn.Conv2d(256 , 256, kernel_size=3, padding='same') #Linear(8 * 8 * 256 , latent_dim)
        self.fc_log_var = nn.Conv2d(256 , 256, kernel_size=3, padding='same') #Linear(256 * 8 * 8 , latent_dim)
        
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(256, 128, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 1, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU()
        )

        def encode(self, x):
            x = self.encoder(x)
            x = x.view(x.size(0), -1)
            mean = self.fc_mean(x)
            log_var = self.fc_log_var(x)
            return mean, log_var

        def reparameterize(self, mean, log_var):
            std = torch.exp(0.5 * log_var)
            eps = torch.randn_like(std)
            return mean + eps * std

        def decode(self, z):
            x = self.decoder(z)
            return x

        def forward(self, x):
            x = self.encoder(x)
            x = x.view(x.size(0), -1)  # Flatten the features
            mean = self.fc_mean(x)
            log_var = self.fc_log_var(x)
            z = self.reparameterize(mean, log_var)
            x_recon = self.decoder(z.view(-1, self.latent_dim))
            return x_recon, mean, log_var

def my_loader_function(path):
        return Image.open(open(path, 'r+b'))

def train_vae(dataset_path, batch_size=64, latent_dim=200, learning_rate=0.001, num_epochs=100):
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])
    
    # Load dataset
    train_dataset= datasets.ImageFolder(root=dataset_path, transform=transforms.ToTensor(), loader=my_loader_function)
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

    # Define VAE model
    vae = VAE(latent_dim)

    # Loss function
    def vae_loss(recon_x, x, mu, log_var):
        BCE = nn.BCELoss(reduction='sum')(recon_x, x) # Reconstruction loss
        KLD = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp()) # KL divergence
        #print(BCE.item(), KLD.item())
        return BCE + 0.001*KLD

    # Optimizer
    optimizer = optim.Adam(vae.parameters(), lr=learning_rate)

    # Training loop
    for epoch in range(num_epochs):
        for i, (images, _) in enumerate(train_loader):
            images = Variable(images)
            recon_images, mu, log_var = vae(images)
            loss = vae_loss(recon_images, images, mu, log_var)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i+1) % 2 == 0:
                print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, i+1, len(train_loader), loss.item()))
        if epoch % 10 == 0:
        # Save the trained VAE model
            torch.save(vae.state_dict(), 'C:/Users/thiba/Documents/INSA_2023-2024/S2/Software_dev/VAE_Models/vae_model'+str(epoch)+'.pth')

if __name__ == "__main__":
    train_vae(dataset_path="C:/Users/thiba/Documents/INSA_2023-2024/S2/Software_dev/ImagesClassées/train_data_0_23999/")
