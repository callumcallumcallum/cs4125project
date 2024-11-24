from src.classifierFactory import ClassifierFactory

class ModelBuilder:
 def __init__(self):
     self.params = {}

 def set_learning_rate(self, learning_rate):
     self.params["learning_rate"] = learning_rate
     return self

 def set_max_iterations(self, max_iter):
     self.params["max_iter"] = max_iter
     return self
'''
 def build(self, strategy_class):
     # Use the strategy to configure and return the classifier
     if "learning_rate" in self.params or learning_rate:
         strategy_class.classifier.learning_rate = self.params["learning_rate"]
     if "max_iter" in self.params:
         strategy_class.classifier.max_iter = self.params["max_iter"]
     return strategy_class
     '''

def change_model_params(self, strategy_class):
    print("Configure model parameters:")
    
    # Get parameters from user input
    learning_rate = input("Enter the learning rate (leave blank to skip): ")
    max_iter = input("Enter the maximum iterations (leave blank to skip): ")

    # Set parameters if provided
    if learning_rate:
        builder.set_learning_rate(float(learning_rate))
    if max_iter:
        builder.set_max_iterations(int(max_iter))

    # Apply the parameters to the strategy (access the classifier inside the strategy)
    strategy_class = builder.build(strategy_class)
    
    # If the model supports these params, apply them to the classifier directly
    if 'learning_rate' in builder.params:
        if hasattr(strategy_class.classifier, 'learning_rate'):
            strategy_class.classifier.learning_rate = builder.params["learning_rate"]
        else:
            print("Warning: The classifier does not support 'learning_rate'.")

    if 'max_iter' in builder.params:
        if hasattr(strategy_class.classifier, 'max_iter'):
            strategy_class.classifier.max_iter = builder.params["max_iter"]
        else:
            print("Warning: The classifier does not support 'max_iter'.")
    
    print("Model parameters updated.")


