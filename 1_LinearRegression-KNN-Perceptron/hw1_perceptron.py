from __future__ import division, print_function

from typing import List, Tuple, Callable

import numpy as np
import scipy
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self, nb_features=2, max_iteration=10, margin=1e-4):
        '''
            Args :
            nb_features : Number of features
            max_iteration : maximum iterations. You algorithm should terminate after this
            many iterations even if it is not converged
            margin is the min value, we use this instead of comparing with 0 in the algorithm
        '''

        self.nb_features = nb_features
        self.w = [0 for i in range(0,nb_features+1)]
        self.margin = margin
        self.max_iteration = max_iteration

    def train(self, features: List[List[float]], labels: List[int]) -> bool:
        '''
            Args  :
            features : List of features. First element of each feature vector is 1
            to account for bias
            labels : label of each feature [-1,1]

            Returns :
                True/ False : return True if the algorithm converges else False.
        '''
        ############################################################################
        # TODO : complete this function.
        # This should take a list of features and labels [-1,1] and should update
        # to correct weights w. Note that w[0] is the bias term. and first term is
        # expected to be 1 --- accounting for the bias
        ############################################################################

        i = 0
        while i < self.max_iteration:
            err = 0
            for sample, yn in zip(features, labels):
                x = np.array(sample)
                w_t = np.array(self.w).transpose()
                y = np.matmul(w_t, x)
                if y * yn > self.margin:
                    continue
                else:
                    x_l2 = np.linalg.norm(x)
                    self.w = self.w + yn * x / x_l2
                    err += 1
            if err == 0:
                return True
            else:
                i += 1
        return False
        raise NotImplementedError

    def reset(self):
        self.w = [0 for i in range(0,self.nb_features+1)]

    def predict(self, features: List[List[float]]) -> List[int]:
        '''
            Args  :
            features : List of features. First element of each feature vector is 1
            to account for bias

            Returns :
                labels : List of integers of [-1,1]
        '''
        ############################################################################
        # TODO : complete this function.
        # This should take a list of features and labels [-1,1] and use the learned
        # weights to predict the label
        ############################################################################

        result = []
        w = self.get_weights()
        for sample in features:
            x = np.array(sample)
            w_t = np.array(w).transpose()
            y = np.matmul(w_t, x)
            if y > self.margin:
                result.append(1)
            else:
                result.append(-1)
        return result
        raise NotImplementedError

    def get_weights(self) -> List[float]:
        return self.w
