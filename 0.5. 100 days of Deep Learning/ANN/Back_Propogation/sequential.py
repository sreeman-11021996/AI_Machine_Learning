import numpy as np

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
        self.params_["w"+str(self.layers_)] = wts
        self.params_["b"+str(self.layers_)] = bias


    def init_params (self,curr_layer_nodes,prev_layer_nodes):
        # Initializing wt = 1 and bias = 0
        wts = np.ones((curr_layer_nodes, prev_layer_nodes))*0.1
        bias = np.zeros((curr_layer_nodes,1))
        return wts,bias

    def compile(self,loss="mean_squared_error",learning_rate=0.01):
        # Loss Function
        self.loss = loss
        # Gradient Descent params
        self.lr = learning_rate
        self.A = {}

    def summation_ (self,wts,bias,X):
        z = np.dot(wts,X.T) + bias
        return z

    def forward_prop_ (self,X):
        A = X


    def fit(self,X,y,epochs=100):
        X = np.array(X)
        y = np.array(y)

        for epoch in range(epochs):
            for i in range(X.shape[0]):
                # Get a random number
                Xi = X[i]
                yi = y[i]

                # Predict for this value
