import torch
import torch.nn as nn
import torch.optim as optim

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
