import itertools

from src.datasets.datasets import Unity_RotOpenAI
from src.evaluation.config import ConfigEval
from src.models.WitnessComplexAE.config import ConfigGrid_WCAE
from src.models.autoencoder.autoencoders import ConvAE_Unity480320


rotopenai_1_local= ConfigGrid_WCAE(
    learning_rate=[1/100],
    batch_size=[180],
    n_epochs=[1000],
    weight_decay=[0],
    early_stopping=[120],
    rec_loss_weight=[1],
    top_loss_weight=[1],
    match_edges=['push_active'],
    k=[2],
    r_max=[10],
    model_class=[ConvAE_Unity480320],
    model_kwargs=[dict()],
    dataset=[Unity_RotOpenAI()],
    sampling_kwargs=[dict()],
    eval=[ConfigEval(
        active=True,
        evaluate_on='test',
        eval_manifold=False,
        save_eval_latent=False,
        save_train_latent=True,
        online_visualization=False,
        k_min=5,
        k_max=10,
        k_step=5,
        quant_eval=False
    )],
    uid=[''],
    toposig_kwargs=[dict()],
    method_args=dict(n_jobs=[1], normalize=[True], mu_push=[1.125], online_wc=[True],
                     dist_x_land=[True],
                     lam_t_decay=[dict([(i*100,1/2**ii) for i,ii in enumerate([-2,-1,0,1,2,4,8,10,12])])],
                     wc_offline=[dict(path_to_data='/Users/simons/PycharmProjects/MT-VAEs-TDA/src/datasets/simulated/openai_rotating')],
                     pre_trained_model = ['/Users/simons/PycharmProjects/MT-VAEs-TDA/output/WAE/openai/retrain_examples/1_/post/Unity_RotOpenAI-seed1-ConvAE_Unity480320-default-lr1_100-bs180-nep1000-rlw1-tlw1-mepush_active9_8-k3-rmax10-seed1-a31416d4']),
    experiment_dir='/Users/simons/PycharmProjects/MT-VAEs-TDA/output/WAE/openai/retrain_examples/1_',
    seed=1,
    device='cpu',
    num_threads=1,
    verbose=True,
)


rotopenai_1_local2= ConfigGrid_WCAE(
    learning_rate=[1/1000],
    batch_size=[180],
    n_epochs=[1000],
    weight_decay=[1e-6],
    early_stopping=[120],
    rec_loss_weight=[1],
    top_loss_weight=[1],
    match_edges=['push_active'],
    k=[2],
    r_max=[10],
    model_class=[ConvAE_Unity480320],
    model_kwargs=[dict()],
    dataset=[Unity_RotOpenAI()],
    sampling_kwargs=[dict()],
    eval=[ConfigEval(
        active=True,
        evaluate_on='test',
        eval_manifold=False,
        save_eval_latent=False,
        save_train_latent=True,
        online_visualization=False,
        k_min=5,
        k_max=10,
        k_step=5,
        quant_eval=False
    )],
    uid=[''],
    toposig_kwargs=[dict()],
    method_args=dict(n_jobs=[1], normalize=[True], mu_push=[1.125], online_wc=[True],
                     dist_x_land=[True],val_size = [0],
                     lam_t_decay=[dict([(i*100,1/2**ii) for i,ii in enumerate([0,1,2,4,8,10,12])])],
                     wc_offline=[dict(path_to_data='/Users/simons/PycharmProjects/MT-VAEs-TDA/src/datasets/simulated/openai_rotating')],
                     pre_trained_model = ['/Users/simons/PycharmProjects/MT-VAEs-TDA/output/WAE/openai/retrain_examples/1_/post/Unity_RotOpenAI-seed1-ConvAE_Unity480320-default-lr1_100-bs180-nep1000-rlw1-tlw1-mepush_active9_8-k3-rmax10-seed1-a31416d4']),
    experiment_dir='/Users/simons/PycharmProjects/MT-VAEs-TDA/output/WAE/openai/retrain_examples/1_',
    seed=1,
    device='cpu',
    num_threads=1,
    verbose=True,
)



rotopenai_g1_cluster= ConfigGrid_WCAE(
    learning_rate=[1/1000],
    batch_size=[180],
    n_epochs=[20000],
    weight_decay=[1e-6],
    early_stopping=[200],
    rec_loss_weight=[1],
    top_loss_weight=[1],
    match_edges=['push_active'],
    k=[2],
    r_max=[10],
    model_class=[ConvAE_Unity480320],
    model_kwargs=[dict()],
    dataset=[Unity_RotOpenAI()],
    sampling_kwargs=[dict(root_path='/cluster/home/schsimo/MT/AEs-VAEs-TDA')],
    eval=[ConfigEval(
        active=True,
        evaluate_on='test',
        eval_manifold=False,
        save_eval_latent=False,
        save_train_latent=True,
        online_visualization=False,
        k_min=5,
        k_max=10,
        k_step=5,
        quant_eval=False
    )],
    uid=[''],
    toposig_kwargs=[dict()],
    method_args=dict(n_jobs=[1], normalize=[True], mu_push=[1.125], online_wc=[True],
                     dist_x_land=[True],
                     lam_t_decay=[dict([(i*150,1/2**ii) for i,ii in enumerate([0,1,2,3,4,5])])],
                     wc_offline=[dict(
                         path_to_data='/cluster/home/schsimo/MT/AEs-VAEs-TDA/src/datasets/simulated/openai_rotating')],
                     pre_trained_model = ['/cluster/scratch/schsimo/output/rotating_decay/Unity_RotOpenAI-seed1-ConvAE_Unity480320-default-lr1_100-bs180-nep12000-rlw1-tlw1-mepush_active9_8-k2-rmax10-seed1-cc1e83ee']),
    experiment_dir='/cluster/scratch/schsimo/output/rotating_retrain',
    seed=1,
    device='cpu',
    num_threads=1,
    verbose=True,
)

