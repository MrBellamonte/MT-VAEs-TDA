import os

import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from torchvision.transforms import transforms

from src.models.WitnessComplexAE.wc_ae import WitnessComplexAutoencoder
from src.models.autoencoder.autoencoders import ConvAE_Unity480320


if __name__ == "__main__":
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    # get model
    root_path2 = '/Users/simons/MT_data/sync/euler_sync_scratch/schsimo/output/rotating_decay'
    exp1 = 'Unity_RotOpenAI-seed1-ConvAE_Unity480320-default-lr1_100-bs180-nep1000-rlw1-tlw1-mepush_active9_8-k3-rmax10-seed1-a31416d4'
    exp2 = 'Unity_RotOpenAI-seed1-ConvAE_Unity480320-default-lr1_100-bs180-nep1000-rlw1-tlw1-mepush_active1-k2-rmax10-seed1-4725d9e2'

    root_path = '/Users/simons/MT_data/sync/selection/unity_box/no_topoloss'
    exp = 'Unity_RotOpenAI-seed1-ConvAE_Unity480320-default-lr1_1000-bs180-nep12000-rlw1-tlw0-mepush_active1-k1-rmax10-seed1-a893ecf4'

    root_path = '/Users/simons/MT_data/sync/selection/unity_box/other'
    exp = 'Unity_RotOpenAI-seed1-ConvAE_Unity480320-default-lr1_100-bs180-nep12000-rlw1-tlw1-mepush_active9_8-k2-rmax10-seed1-cc1e83ee'

    path_source = os.path.join(root_path,exp)


    autoencoder = ConvAE_Unity480320()
    device = torch.device('cpu')
    model = WitnessComplexAutoencoder(autoencoder)
    state_dict = torch.load(os.path.join(path_source, 'model_state.pth'),map_location=device)
    state_dict2 = torch.load(os.path.join(os.path.join(root_path2,exp2), 'model_state.pth'), map_location=device)
    if 'latent' not in state_dict:
        state_dict['latent_norm'] = state_dict2['latent_norm']
    model.load_state_dict(state_dict)

    model.eval()


    # get latents
    latents = pd.read_csv(os.path.join(path_source, 'train_latents.csv'))

    latents_temp = latents[0:1]
    # get reconstructed images
    labels = latents['labels']
    latents_tensor = torch.tensor(latents[['0','1']].values)
    print(latents_tensor.shape)

    x_hat = model.decode(latents_tensor.float())


    #x_hat = model.decode(torch.tensor(latents_temp[:][['0', '1']].values).float())
    trans = transforms.ToPILImage()


    for i in range(12):
        ii = 20*i
        plt.imshow(trans(x_hat[ii][:][:][:]))
        plt.savefig(os.path.join(path_source,'{}deg.pdf'.format(ii)))
        plt.show()
