import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler




# Function to preprocess your data by scaling it while ensuring that the scaling parameters are 
# learned from the training data and applied consistently to all splits (training, validation, and test).
def scale_data(train, 
               validate, 
               test, 
               to_scale = ['bedrooms','bathrooms','square_feet','property_tax'],
               return_scaler=False):
    '''
    Scales the 3 data splits. 
    Takes in train, validate, and test data splits and returns their scaled counterparts using MinMaxScaler.
    If return_scalar is True, the scaler object will be returned as well
    '''
    # make copies of our original data
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    #     make the thing
    scaler = MinMaxScaler()
    #     fit the thing
    scaler.fit(train[to_scale])
    # applying the scaler:
    train_scaled[to_scale] = pd.DataFrame(scaler.transform(train[to_scale]),
                                                  columns=train[to_scale].columns.values).set_index([train.index.values])
                                                  
    validate_scaled[to_scale] = pd.DataFrame(scaler.transform(validate[to_scale]),
                                                  columns=validate[to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[to_scale] = pd.DataFrame(scaler.transform(test[to_scale]),
                                                 columns=test[to_scale].columns.values).set_index([test.index.values])
    
    if return_scaler:
        return scaler, train_scaled, validate_scaled, test_scaled
    else:
        return train_scaled, validate_scaled, test_scaled









# Create a function to isolate the target variable from a split dataframe
def X_y_split(train, validate, test, target):
    '''
    This function takes in train, validate, and test dataframes and the target variable.
    Then it returns the X_train, y_train, X_validate, y_validate, X_test, y_test.
    '''  

    X_train = train.drop(columns= target)
    y_train = train[target]

    X_validate = validate.drop(columns= target)
    y_validate = validate[target]

    X_test = test.drop(columns= target)
    y_test = test[target]
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test
# use the function on zillow for example
# X_train, y_train, X_validate, y_validate, X_test, y_test = X_y_split(train, validate, test, 'property_value')






