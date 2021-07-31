import mlflow
logged_model = 'runs:/647811899b9f4fbcb1fb785e6c0d7f58/RandomForestRegressor'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
loaded_model.predict(pd.DataFrame(data))