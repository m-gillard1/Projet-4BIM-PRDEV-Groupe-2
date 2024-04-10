import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.autograd import Variable
from PIL import Image


class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()

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
            mean = self.fc_mean(x)
            log_var = self.fc_log_var(x)
            z = self.reparameterize(mean, log_var)
            x_recon = self.decoder(z)
            return x_recon, mean, log_var

def my_loader_function(path):
        return Image.open(open(path, 'r+b'))

def train_vae(dataset_path, batch_size=32, learning_rate=0.0001, num_epochs=100):
    
    # Load dataset
    train_dataset= datasets.ImageFolder(root=dataset_path, transform=transforms.ToTensor(), loader=my_loader_function)
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

    # Define VAE model
    vae = VAE()

    """
    This part was only used to train the autoencoder as it can cause some error on computer and is not actually used during the application we put it in comment
    #define the running device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print("Training on:", device)
    vae.to(device)
    """
    
    # Loss function
    def vae_loss(recon_x, x, mu, log_var, epoch):
        if epoch > 2:
            MSE = nn.MSELoss()(recon_x, x)
            KLD = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp()) # KL divergence
            print(MSE.item(), KLD.item())
            loss =  MSE + 1e-7 * KLD
        else:
            MSE = nn.MSELoss()(recon_x, x)
            print(MSE.item())
            loss = MSE
        return loss 

    # Optimizer
    optimizer = optim.Adam(vae.parameters(), lr=learning_rate)

    # Training loop
    for epoch in range(num_epochs):
        for i, (images, _) in enumerate(train_loader):
            images = Variable(images)
            #images = images.to(device)
            recon_images, mu, log_var = vae(images)
            loss = vae_loss(recon_images, images, mu, log_var)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i+1) % 2 == 0:
                print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, i+1, len(train_loader), loss.item()))
        # Save the trained VAE model
        torch.save(vae.state_dict(), './vae_model'+str(epoch)+'.pth')

if __name__ == "__main__":
    train_vae(dataset_path="C:/Users/thiba/Documents/INSA_2023-2024/S2/Software_dev/ImagesClassées/train_data_0_23999/")
