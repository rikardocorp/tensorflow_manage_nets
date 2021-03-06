import time
import tensorflow as tf
import sys, os
import numpy as np
import matplotlib.pyplot as plt

switch_server = True

testdir = os.path.dirname('__file__')
srcdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

if switch_server is True:
    from tools import utils
    from nets import net_conv_aencoder as CAE
    from tools.dataset_csv import Dataset_csv
else:
    from tensorflow_manage_nets.tools import utils
    from tensorflow_manage_nets.nets import net_conv_aencoder as CAE
    from tensorflow_manage_nets.tools.dataset_csv import Dataset_csv

# ..................................................................


# GLOBAL VARIABLES
path = '../data/features/'
path_data_train = [path+'SKINfeaturesA_Test.csv']
path_data_test = [path+'SKINfeaturesA_Train.csv']

# ..................................................................


# Función, fase de test
def test_model(net, sess_test, objData):

    total = objData.total_inputs
    mbach = objData.minibatch

    cost_total = 0

    for i in range(objData.total_batchs_complete):
        x_, label = objData.generate_batch()
        cost, layer = sess_test.run([net.cost, net.net['encodeConv_1']], feed_dict={x_batch: x_})

        # save output of a layer
        # utils.save_layer_output(layer, label, name='Train_AE1_fc1')

        cost_total = cost_total + cost
        objData.next_batch_test()

    return cost_total


# Funcion, fase de entrenamiento
def train_model(net, sess_train, objData, objDatatest, epoch):

    print('\n# PHASE: Training model')
    for ep in range(epoch):
        t0 = time.time()
        for i in range(objData.total_batchs):

            batch, _ = objData.generate_batch()
            sess_train.run(net.train, feed_dict={x_batch: batch})
            objData.next_batch()

        cost_prom = test_model(net, sess_train, objDatatest)
        t1 = time.time()
        print('     Epoch', ep, ': ', cost_prom, '  t: ', str(t1 - t0))


# Plot example reconstructions
def plot_result(net, sess, batch, n_examples=5, dim=(1, 1)):
    print('Plotting')
    recon = sess.run(net.y, feed_dict={x_batch: batch})
    fig, axs = plt.subplots(2, n_examples, figsize=(n_examples, 2))
    for example_i in range(n_examples):
        axs[0][example_i].imshow(np.reshape(batch[example_i, :], dim))
        axs[1][example_i].imshow(np.reshape(recon[example_i, :], dim))

    fig.show()
    plt.draw()
    plt.waitforbuttonpress()
# ..................................................................

if __name__ == '__main__':

    path_load_weight = None
    path_save_weight = '../weight/saveCAE_1.npy'

    mini_batch_train = 34
    mini_batch_test = 30
    epoch = 10
    learning_rate = 0.0001

    # Datos de media y valor maximo
    data_normal = Dataset_csv(path_data=[path_data_train[0], path_data_test[0]], random=False)
    Damax = data_normal.amax
    # Load data train
    data_train = Dataset_csv(path_data=path_data_train, minibatch=mini_batch_train, max_value=Damax)
    # Load data test
    # data_test = Dataset_csv(path_data=path_data_test, minibatch=mini_batch_test, max_value=Damax, random=False)
    data_test = Dataset_csv(path_data=path_data_train, minibatch=mini_batch_train, max_value=Damax, random=False)

    with tf.Session() as sess:

        x_batch = tf.placeholder(tf.float32, [None, 4096])

        CAEncode = CAE.ConvAEncoder(path_load_weight, learning_rate=learning_rate)
        CAEncode.build(input_batch=x_batch, n_filters=[1, 10, 10], corruption=False)
        sess.run(tf.global_variables_initializer())

        print('Original Cost: ', test_model(CAEncode, sess, data_test))
        train_model(CAEncode, sess, data_train, objDatatest=data_test, epoch=epoch)

        # SAVE WEIGHTs
        CAEncode.save_npy(sess, path_save_weight)

        # Plot example reconstructions
        plot_result(CAEncode, sess, data_train.generate_batch()[0], dim=(64, 64))
