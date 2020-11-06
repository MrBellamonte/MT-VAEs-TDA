from scripts.ssc.TopoAE_ext.config_libraries.colab_configs.mnist import mnist_test512_cuda
from scripts.ssc.TopoAE_ext.config_libraries.euler_configs.mnist import mnist_s838_1024_cuda_test
from scripts.ssc.TopoAE_ext.config_libraries.local_configs.mnist import (
    mnist_test2, mnist_test3,
    mnist_test256_1024_leonhard, mnist_test256)
from scripts.ssc.TopoAE_ext.config_libraries.swissroll import debug
from src.models.WitnessComplexAE.train_engine import simulator_TopoAE_ext

if __name__ == "__main__":
    configs2 = mnist_s838_1024_cuda_test.configs_from_grid()
    configs = mnist_test256_1024_leonhard.configs_from_grid()
    for config in configs:
        simulator_TopoAE_ext(config)
