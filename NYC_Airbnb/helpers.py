# cross val

from sklearn.model_selection import cross_val_score

def check_accuracy_of_model(reg, X_train, y_train):
    """Prints the accuracy of the model by computing a cross val score"""
    
    results = cross_val_score(estimator = reg, X = X_train, y = y_train, cv=10)
    print('Accuracy: {:.2f} %'.format(results.mean()*100))
    