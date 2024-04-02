import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets

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
            nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16,32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32,64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(64,128, kernel_size=3, stride=2, padding=1),
            nn.ReLU()
        )

        # Mean and log variance layers
        self.fc_mean = nn.Linear(128 * 32 * 32, latent_dim)
        self.fc_log_var = nn.Linear(128 * 32 * 32 , latent_dim)

        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 128 * 32 * 32 ),
            nn.ReLU()
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 1, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.Sigmoid()
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

def train_vae():
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])
    
    # Load dataset
    train_dataset= datasets.ImageFolder(root=dataset_path, transform=transforms.ToTensor(), loader=my_loader_function)
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
