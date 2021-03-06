import sys, os
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

switch_server = True
testdir = os.path.dirname('__file__')
srcdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))


if switch_server is True:
    from tools import utils
    from nets import net_aencoder as AE
    from tools.dataset_csv import Dataset_csv
else:
    from tensorflow_manage_nets.tools import utils
    from tensorflow_manage_nets.nets import net_aencoder as AE
    from tensorflow_manage_nets.tools.dataset_csv import Dataset_csv


def get_data_plot(opc):
    data = {}

    if opc == 0:
        # MNIST
        data['mnist'] = {}
        # data['mnist']['ae'] = {}
        # data['mnist']['ae']['dim'] = [4,6,9,13,19,28,42,63,94,141,211]
        # data['mnist']['ae']['fractal'] = [3.1633,4.5932,6.2643,7.8174,0.1364,0.2681,0.4716,1.0265,1.8659,1.9534,25.5753]

        data['mnist']['ae'] = {}
        data['mnist']['ae']['dim'] = [4, 28, 42, 63, 94, 141, 211]
        data['mnist']['ae']['fractal'] = [3,5.9068, 9.2893, 9.6357, 10.7876, 12.7876, 12.7876]

        data['mnist']['dct'] = {}
        data['mnist']['dct']['dim'] = [4,6,9,13,19,28,42,63,94,141,211]
        data['mnist']['dct']['fractal'] = [3.5165,4.4513,4.7163,4.981,5.4558,5.2292,3.4751,19.0054,22.5753,25.5753,25.5753]

        # data['mnist']['ipla'] = {}
        # data['mnist']['ipla']['dim'] = [4,6,9,13,19,28,42,63,94,141,211]
        # data['mnist']['ipla']['fractal'] = [2.0956,3.4231,3.613,4.5425,4.2206,4.4101,4.0596,16.7204,19.8748,23.2534,25.5753]

        # data['mnist']['sax'] = {}
        # data['mnist']['sax']['dim'] = [4,6,9,13,19,28,42,63,94,141,211,316,474]
        # data['mnist']['sax']['fractal'] = [2.5403,3.5612,4.7923,6.0755,6.1693,6.6266,13.7531,17.0834,21.3274,25.5753,25.5753,25.5753,25.5753]

        data['mnist']['pca'] = {}
        data['mnist']['pca']['dim'] = [4,6,9,13,19,28,42,63,94,141,211]
        data['mnist']['pca']['fractal'] = [3.7764,3.633,4.3696,4.7597,4.1067,4.5098,18.7939,1.7925,25.5753,25.5753,25.5753]

        data['mnist']['svd'] = {}
        data['mnist']['svd']['dim'] = [4,6,9,13,19,28,42,63,94,141,211]
        data['mnist']['svd']['fractal'] = [3.5072,2.9827,3.6737,4.8881,4.3186,4.8956,3.033,22.5753,25.5753,25.5753,25.5753]

        # data['mnist']['paa'] = {}
        # data['mnist']['paa']['dim'] = [4,6,9,13,19,28,42,63,94,141,211]
        # data['mnist']['paa']['fractal'] = [3.7688,4.2507,3.8278,3.8522,5.2186,4.6841,4.8219,5.1059,4.2068,19.2354,23.5753]

        data['mnist']['dwt'] = {}
        data['mnist']['dwt']['dim'] = [4,6,9,13,19,28,42,63,94,141,211]
        data['mnist']['dwt']['fractal'] = [3.4016,4.5113,4.7749,4.4473,4.4599,4.5201,3.9403,4.6369,19.598,22.5753,25.5753]

        # data['mnist']['cp'] = {}
        # data['mnist']['cp']['dim'] = [4,6,9,13,19,28,42,63,94,141,211,316,474]
        # data['mnist']['cp']['fractal'] = [3.4246,4.0078,4.4739,4.8383,4.3009,5.4709,15.1808,17.9606,2.0437,24.5753,25.5753,25.5753,25.5753]

        dx = data['mnist']
        name = 'mnist'
        original_dim = 800

    elif opc == 1:

        # CIFAR10 - 1.6494
        data['cifar10'] = {}
        # data['cifar10']['ae'] = {}
        # data['cifar10']['ae']['dim'] = [4,6,9,13,19,28,42,63,94,141,211,316]
        # data['cifar10']['ae']['fractal'] = [2.2365,2.6026,3.48,0.1136,0.119,0.1171,0.1697,0.2356,0.1557,0.2513,23.9903,25.5753]

        data['cifar10']['ae'] = {}
        data['cifar10']['ae']['dim'] = [4, 28, 42, 63, 94, 141, 211]
        data['cifar10']['ae']['fractal'] = [0.5, 0.1678, 0.1551, 10.3003, 11.401, 11.4032, 11.2067]

        data['cifar10']['dct'] = {}
        data['cifar10']['dct']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211]
        data['cifar10']['dct']['fractal'] = [3.9918,5.0943,6.243,2.8814,3.2774,4.645,6.1401,15.0665,3.3972,23.5753,25.5753]

        # data['cifar10']['ipla'] = {}
        # data['cifar10']['ipla']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211]
        # data['cifar10']['ipla']['fractal'] = [1.9384,2.9256,3.8386,5.0608,5.8173,6.1881,8.9843,8.9674,9.8928,11.6136,12.7876]

        # data['cifar10']['sax'] = {}
        # data['cifar10']['sax']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211, 316, 474, 711, 1066, 1599, 2398, 3597]
        # data['cifar10']['sax']['fractal'] = [0.4879,0.546,0.6239,0.7161,0.8361,0.9713,1.2115,1.5869,2.1696,2.9898,4.2449,6.7758,10.2027,16.8038,25.5753,25.5753,25.5753,25.5753]

        data['cifar10']['pca'] = {}
        data['cifar10']['pca']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211]
        data['cifar10']['pca']['fractal'] = [3.3653,4.0906,3.9554,1.5782,3.9994,6.2009,5.3791,6.9906,18.8888,25.5753,25.5753]

        data['cifar10']['svd'] = {}
        data['cifar10']['svd']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211]
        data['cifar10']['svd']['fractal'] = [3.634,2.7057,4.6587,2.6081,5.9719,2.5707,6.5027,6.2395,21.8748,25.5753,25.5753]

        # data['cifar10']['paa'] = {}
        # data['cifar10']['paa']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211]
        # data['cifar10']['paa']['fractal'] = [3.5931,4.3796,5.6623,8.6333,0.3525,10.1474,9.4041,0.1516,0.2149,10.5511,9.9956]

        data['cifar10']['dwt'] = {}
        data['cifar10']['dwt']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211]
        data['cifar10']['dwt']['fractal'] = [3.4213,4.8521,5.6459,2.9588,3.3272,5.485,6.7866,12.7766,14.5139,20.3658,23.5753]

        # data['cifar10']['cp'] = {}
        # data['cifar10']['cp']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211, 316, 474, 711, 1066, 1599, 2398, 3597]
        # data['cifar10']['cp']['fractal'] = [3.5199,4.6375,1.0774,6.3398,8.323,4.7599,8.2534,10.9358,14.926,20.9903,25.5753,25.5753,25.5753,25.5753,25.5753,25.5753,25.5753,25.5753]

        dx = data['cifar10']
        name = 'cifar10'
        original_dim = 4096

    elif opc == 2:

        # SVHN = 28.3359
        data['svhn'] = {}
        data['svhn']['pca'] = {}
        data['svhn']['pca']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 160]
        data['svhn']['pca']['fractal'] = [3.6906, 5.1793, 6.4785, 7.2137, 12.435, 5.422, 2.4771, 28.3359, 28.3359,28.3359, 28.3359]

        data['svhn']['ae'] = {}
        data['svhn']['ae']['dim'] = [4, 28, 42, 63, 94, 141, 160]
        data['svhn']['ae']['fractal'] = [3, 11.9392, 4.0172, 9.1322, 11.4848, 14.168, 14.168]

        # data['svhn']['paa'] = {}
        # data['svhn']['paa']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 160]
        # data['svhn']['paa']['fractal'] = [3.6458, 5.5113, 4.277, 5.9883, 11.0742, 8.8174, 9.3821, 10.8159, 11.9396,14.168, 14.168]

        data['svhn']['dwt'] = {}
        data['svhn']['dwt']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 160]
        data['svhn']['dwt']['fractal'] = [2.9093, 4.6779, 5.5817, 7.5835, 8.0256, 14.9638, 3.4771, 25.751, 28.3359,28.3359, 28.3359]

        data['svhn']['dct'] = {}
        data['svhn']['dct']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 160]
        data['svhn']['dct']['fractal'] = [3.8896, 5.515, 6.5078, 7.5054, 15.8202, 21.736, 27.3359, 28.3359, 28.3359,28.3359, 28.3359]

        data['svhn']['svd'] = {}
        data['svhn']['svd']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 160]
        data['svhn']['svd']['fractal'] = [3.8101, 5.0242, 6.5251, 7.9185, 12.2805, 5.5287, 22.7814, 28.3359, 28.3359,28.3359, 28.3359]

        # data['svhn']['ipla'] = {}
        # data['svhn']['ipla']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 160]
        # data['svhn']['ipla']['fractal'] = [1.8991, 2.8153, 3.7822, 5.4587, 7.7079, 13.4563, 24.751, 28.3359, 28.3359,28.3359, 28.3359]

        dx = data['svhn']
        name = 'svhn'
        original_dim = 1152

    elif opc == 3:

        # AgNews - 30.4943
        data['agnews'] = {}
        data['agnews']['dwt'] = {}
        data['agnews']['dwt']['dim'] = [4,6,9,13,19,28,42,63,94,141,211,316]
        data['agnews']['dwt']['fractal'] = [0.9801,0.9747,1.7576,1.758,2.6681,2.5881,4.0368,4.0368,2.132,2.2803,3.9624,7.6197]

        data['agnews']['ae'] = {}
        data['agnews']['ae']['dim'] = [28, 42, 63, 94, 141, 211, 316]
        data['agnews']['ae']['fractal'] = [0.6975, 0.7732, 9.4179, 11.7506, 0.7732, 11.6815, 11.4215]

        # data['agnews']['ipla'] = {}
        # data['agnews']['ipla']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211, 316]
        # data['agnews']['ipla']['fractal'] = [0.8858,0.8713,0.7968,1.5267,1.8855,1.94,2.6152,3.2711,2.5011,2.5171,3.1752,3.8608]

        # data['agnews']['paa'] = {}
        # data['agnews']['paa']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211, 316]
        # data['agnews']['paa']['fractal'] = [0.8103,1.3728,1.7259,1.8405,2.7076,1.6259,3.195,5.4737,6.2383,6.8174,8.5794,9.333]

        data['agnews']['svd'] = {}
        data['agnews']['svd']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211, 316]
        data['agnews']['svd']['fractal'] = [2.448,2.7537,2.9912,3.3966,3.6956,4.8341,4.5793,4.6637,17.3139,22.4432,24.7651,24.7651]

        data['agnews']['pca'] = {}
        data['agnews']['pca']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211, 316]
        data['agnews']['pca']['fractal'] = [2.5685,2.3968,2.8437,2.2094,3.805,4.4401,5.4467,5.8244,4.3857,24.7651,24.7651,24.7651]

        data['agnews']['dct'] = {}
        data['agnews']['dct']['dim'] = [4, 6, 9, 13, 19, 28, 42, 63, 94, 141, 211, 316]
        data['agnews']['dct']['fractal'] = [1.9761,2.43,2.5922,2.9844,3.9418,4.3012,4.111,2.1457,3.7315,4.676,5.0242,16.3515]

        dx = data['agnews']
        name = 'AgNews'
        original_dim = 8704

    return dx, name, original_dim


colors = cycle(['navy', 'turquoise', 'darkorange', 'cornflowerblue', 'teal','red', 'yellow', 'magenta', 'gray'])

for i in range(1,2):
    data, name, originalD = get_data_plot(i)
    plt.figure(1)
    for met, color in zip(data, colors):
        dset = data
        plt.plot(dset[met]['dim'], dset[met]['fractal'], color=color, lw=1,
                 label='Method - {0}'.format(met))

    plt.xlabel('Reduced Dimension')
    plt.ylabel('Fractal Dimension')
    plt.title('Dim-Fractal - Dataset ' + name + '-' + str(originalD))
    plt.legend(loc="lower right")
    plt.show()
