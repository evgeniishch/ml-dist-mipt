import numpy as np


class ClassificationMetrics:
    @staticmethod
    def accuracy(labels, preds):
        """
        labels : numpy array of shape (`n_observations`)
        predictions : numpy array of shape (`n_observations`)

        Return : float
            single number with accuracy score
        
        Comment: Both labels and predictions contain integers 0 or 1
        """

        # YOUR CODE HERE
        return

    @staticmethod
    def precision(labels, preds):
        """
        labels : numpy array of shape (`n_observations`)
        predictions : numpy array of shape (`n_observations`)

        Return : float
            single number with precision score
        
        Comment: Both labels and predictions contain integers 0 or 1
        """

        # YOUR CODE HERE
        return

    @staticmethod
    def recall(labels, preds):
        """
        labels : numpy array of shape (`n_observations`)
        predictions : numpy array of shape (`n_observations`)

        Return : float
            single number with recall score
        
        Comment: Both labels and predictions contain integers 0 or 1
        """
        
        # YOUR CODE HERE
        return

    @staticmethod
    def f1(labels, preds):
        """
        labels : numpy array of shape (`n_observations`)
        predictions : numpy array of shape (`n_observations`)

        Return : float
            single number with f1 score
        
        Comment: Both labels and predictions contain integers 0 or 1
        """

        # YOUR CODE HERE
        return

    @staticmethod
    def f_beta(labels, preds, beta=1):
        """
        labels : numpy array of shape (`n_observations`)
        predictions : numpy array of shape (`n_observations`)
        beta : float

        Return : float
            single number with f_beta score
        
        Comment: Both labels and predictions contain integers 0 or 1
        """

        # YOUR CODE HERE
        return
    