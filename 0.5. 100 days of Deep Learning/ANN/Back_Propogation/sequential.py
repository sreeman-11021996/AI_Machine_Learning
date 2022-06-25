import numpy as np
import pandas as pd

WTS = "w"
BIAS = "b"
OUTPUT = "a"
X_ROW = 2
X_COL = 1

class sequential_:

    def __init__ (self):
        self.layers_ = 0
        self.params_ = {}
        self.nodes_ = []

    def add (self,nodes=5,activation = "linear",input_dim=None):
        # add one layer
        self.layers_ += 1
        # add the nodes
        self.nodes_.append(nodes)

        if input_dim:  # Input Layer
            prev_nodes = input_dim
        else:
            prev_nodes = self.nodes_[self.layers_-2]
        curr_nodes = nodes
        wts, bias = self.init_params(curr_nodes,prev_nodes)

        # add the wts and bias to self.params_
        self.params_[WTS+str(self.layers_)] = wts
        self.params_[BIAS+str(self.layers_)] = bias


    def init_params (self,curr_layer_nodes:int,prev_layer_nodes:int):
        # Initializing wt = 0.1 and bias = 0
        wts = np.ones((curr_layer_nodes, prev_layer_nodes))*0.1
        bias = np.zeros((curr_layer_nodes,1))
        return wts,bias

    def compile(self,loss="mean_squared_error",learning_rate=0.01):
        # Loss Function
        self.loss = loss
        # Gradient Descent params
        self.lr = learning_rate
        self.outputs = {}

    def summation_ (self,wts:np.ndarray,bias:np.ndarray,X:np.ndarray):
        z = np.dot(wts,X) + bias
        return z

    def forward_prop_ (self,X):
        A = X
        for l in range(1,self.layers_+1):
            wts = self.params_[WTS + str(l)]
            bias = self.params_[BIAS + str(l)]
            A = self.summation_(wts,bias,A)
            self.outputs[OUTPUT+str(l)] = A
        return A

    def fit(self,X:pd.core.frame.DataFrame,y:pd.core.frame.DataFrame,epochs=100):
        X = np.array(X)
        y = np.array(y)

        for epoch in range(epochs):
            for i in range(X.shape[0]):
                # Get a random number
                Xi = X[i].reshape(X_ROW,X_COL)
                yi = y[i]

                # Predict for this value
                y_predi = self.forward_prop_(Xi)