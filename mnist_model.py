from __future__ import division, print_function, absolute_import

from tefla.core.layer_arg_ops import common_layer_args, make_args, end_points
from tefla.core.layers import dropout, prelu, batch_norm_lasagne
from tefla.core.layers import input, conv2d, fully_connected, max_pool, softmax

# sizes - (width, height)
image_size = (32, 32)
crop_size = (32, 32)


def model(is_training, reuse):
    common_args = common_layer_args(is_training, reuse)
    conv_args = make_args(batch_norm=None, activation=prelu, **common_args)
    fc_args = make_args(activation=prelu, **common_args)
    logit_args = make_args(activation=None, **common_args)

    x = input((None, crop_size[1], crop_size[0], 3), **common_args)
    x = conv2d(x, 16, name='conv1_1', **conv_args)
    x = conv2d(x, 16, name='conv1_2', **conv_args)
    x = max_pool(x, name='pool1', **common_args)
    x = fully_connected(x, n_output=128, name='fc1', **fc_args)
    x = dropout(x, drop_p=0.5, name='dropout2', **common_args)
    logits = fully_connected(x, n_output=10, name="logits", **logit_args)
    predictions = softmax(logits, name='predictions', **common_args)

    return end_points(is_training)