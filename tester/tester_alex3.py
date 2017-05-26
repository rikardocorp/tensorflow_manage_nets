import time
import tensorflow as tf
import sys, os
import numpy as np
import tensorflow.examples.tutorials.mnist.input_data as input_data

switch_server = True

testdir = os.path.dirname('__file__')
srcdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

if switch_server is True:
    from tools import utils
    from nets import net_alex3 as ALEX
    from tools.dataset_image import Dataset
else:
    from tensorflow_manage_nets.tools import utils
    from tensorflow_manage_nets.nets import net_alex3 as ALEX
    from tensorflow_manage_nets.tools.dataset_image import Dataset


# GLOBAL VARIABLES

# path = '../../data/ISB2016/'
# path_dir_image_train = path + "image_train_complete/"
# path_dir_image_test = path + "image_test_complete/"
# path_data_train = path + 'ISB_Train_complete.csv'
# path_data_test = path + 'ISB_Test_complete.csv'
#
# path = '../../data/CIFAR_10/'
# path_dir_image_train = path + "train_cifar10_original/"
# path_dir_image_test = path + "test_cifar10_original/"
# path_data_train = path + 'cifar10_train_label.csv'
# path_data_test = path + 'cifar10_test_label.csv'

# VALIDATE INPUT DATA
# assert os.path.exists(path), 'No existe el directorio de datos ' + path
# assert os.path.exists(path_data_train), 'No existe el archivo con los datos de entrenamiento ' + path_data_train
# assert os.path.exists(path_data_test), 'No existe el archivo con los datos de pruebas ' + path_data_test


# Función, fase de test
def test_model(net, sess_test, objData, minibatch=50):

    total = objData.num_examples

    count_success = 0
    count_by_class = np.zeros([net.num_class, net.num_class])
    prob_predicted = []

    print('\n# PHASE: Test classification')

    for batch_i in range(total // minibatch):
        batch, label = objData.next_batch(minibatch)
        batch = np.reshape(batch, (-1, 28, 28, 1))

        prob, layer = sess_test.run([net.prob, net.pool2], feed_dict={vgg_batch: batch})

        count, count_by_class, prob_predicted = utils.print_accuracy(label, prob, matrix_confusion=count_by_class, predicted=prob_predicted)
        count_success = count_success + count

    # promediamos la precision total
    accuracy_final = count_success/total
    print('\n# STATUS: Confusion Matrix')
    print(count_by_class)
    print('    Success total: ', str(count_success))
    print('    Accuracy total: ', str(accuracy_final))

    return accuracy_final


# Funcion, fase de entrenamiento
def train_model(net, sess_train, objData, epoch, minibatch):

    total = objData.num_examples
    print('\n# PHASE: Training model')

    for ep in range(epoch):
        print('\n     Epoch:', ep)
        t0 = time.time()
        cost_i = 0
        for batch_i in range(total // minibatch):
            t_start = time.time()
            batch, label = objData.next_batch(minibatch)
            batch = np.reshape(batch, (-1, 28, 28, 1))

            label = tf.one_hot([li for li in label], on_value=1, off_value=0, depth=net.num_class)
            label = list(sess_train.run(label))

            _, cost = sess_train.run([net.train, net.cost], feed_dict={vgg_batch: batch, vgg_label: label})
            t_end = time.time()

            cost_i = cost_i + cost
            print("        > Minibatch: %d train on batch time: %7.3f seg." % (batch_i, (t_end - t_start)))

        t1 = time.time()
        print("        Cost per epoch: ", cost_i)
        print("        Time epoch: %7.3f seg." % (t1 - t0))
        print("        Time per iteration: %7.3f seg." % ((t1 - t0) / epoch))


if __name__ == '__main__':

    # LOad y save  weights
    path_load_weight = None
    path_save_weight = '../weight/save_alex.npy'
    load_weight_fc = False

    # Ultimas capas de la red
    num_class = 10
    last_layers = [100, num_class]
    epoch = 2
    mini_batch_train = 50
    learning_rate = 0.0005
    accuracy = 0

    # GENERATE DATA
    mnist = input_data.read_data_sets('../data/MNIST_data/', one_hot=False)
    data_test = mnist.test
    data_train = mnist.train

    with tf.Session() as sess:
        # DEFINE MODEL
        vgg_batch = tf.placeholder(tf.float32, [None, 28, 28, 1])
        vgg_label = tf.placeholder(tf.float32, [None, last_layers[1]])
        train_mode = tf.placeholder(tf.bool)

        # Initialize of the model VGG19
        cnn = ALEX.ALEXNET(path_load_weight, learning_rate=learning_rate, load_weight_fc=load_weight_fc)
        cnn.build(vgg_batch, vgg_label, last_layers=last_layers)
        sess.run(tf.global_variables_initializer())

        # # Execute Network
        test_model(net=cnn, sess_test=sess, objData=data_test)
        train_model(net=cnn, sess_train=sess, objData=data_train, epoch=epoch, minibatch=mini_batch_train)
        accuracy = test_model(net=cnn, sess_test=sess, objData=data_test)

        # SAVE LOG: Genera un registro en el archivo log-server.txt
        utils.write_log(total_data=data_train.total_images,
                        epoch=epoch,
                        m_batch=mini_batch_train,
                        l_rate=learning_rate,
                        accuracy=accuracy,
                        file_npy=path_load_weight,
                        extra='')

        # SAVE WEIGHTs
        cnn.save_npy(sess, path_save_weight)