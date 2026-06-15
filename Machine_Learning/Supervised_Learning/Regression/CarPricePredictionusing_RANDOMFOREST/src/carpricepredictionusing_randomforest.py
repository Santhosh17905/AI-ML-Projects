# Car Price Prediction using Random Forest
# This code implements a machine learning model to predict car prices based on various features. It includes data loading, preprocessing, model training, evaluation, and user input for prediction.

# Import necessary libraries
import pandas as pd

# Upload the dataset file (dataset.csv) from your local machine to the Colab environment
# This will allow you to load the dataset into a pandas DataFrame for further processing.

from google.colab import files
uploaded = files.upload()

# Load the dataset into a pandas DataFrame and drop the 'car_ID' column as it is not relevant for prediction.

dataset = pd.read_csv('dataset.csv')
dataset = dataset.drop(['car_ID'],axis=1)

# Display the shape of the dataset 

print(dataset.shape)
print(dataset.head(5))

# Separate the independent variables (features) and the dependent variable (target) from the dataset. The target variable is 'price', and the features are all other columns.

Xdata = dataset.drop('price',axis=1)

# Convert categorical columns into numbers
X = pd.get_dummies(Xdata)

Y = dataset['price']

# Scale the features using StandardScaler to ensure that all features contribute equally to the model training. This step is important for algorithms like Random Forest to perform well.

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
cols = X.columns
X = pd.DataFrame(scaler.fit_transform(X))
X.columns = cols
X

# Split the dataset into training and testing sets using an 80-20 split. This allows us to train the model on a portion of the data and evaluate its performance on unseen data.

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.20,random_state=0)

# Hyperparameter tuning for the Random Forest model using GridSearchCV to find the best combination of parameters for optimal performance.

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

param_grid = {
    'n_estimators': [100,200],
    'max_depth': [5,10,15],
    'min_samples_split': [2,5]
}

rf = RandomForestRegressor(random_state=0)

grid = GridSearchCV(rf, param_grid, cv=5)

grid.fit(x_train, y_train)

model = grid.best_estimator_

# Train the Random Forest model using the best parameters found from GridSearchCV on the training data.

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=0
)
model.fit(x_train, y_train)

# Make predictions on the test set using the trained model and evaluate its performance using the R2 score.

ypred = model.predict(x_test)

from sklearn.metrics import r2_score
r2score = r2_score(y_test,ypred)
print("R2Score",r2score*100)
print("Model Accuracy:", round(r2score*100,2), "%")

"""# user input *prediction*

## Extract Original Feature Names and Types

### Subtask:
Identify and list all original feature names (numerical and categorical) that were present in `Xdata` before one-hot encoding. This will serve as a guide for collecting comprehensive user input.

**Reasoning**:
I need to identify numerical and categorical features from the `Xdata` DataFrame to understand the original features before one-hot encoding. I will then print these lists as requested.
"""

numerical_features = Xdata.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = Xdata.select_dtypes(include=['object']).columns.tolist()

print("Numerical Features:", numerical_features)
print("Categorical Features:", categorical_features)

"""## Refactor Preprocessing and Save Scaler

### Subtask:
Modify the code to save the `StandardScaler` object used for feature scaling and the exact column names of `X` after one-hot encoding but before scaling. This is crucial for consistently preprocessing new user input.

## Collect Comprehensive User Input

### Subtask:
Prompt the user to provide values for all identified original features (both numerical and categorical). For categorical features, explain that string values are needed. This step ensures that the raw input covers all dimensions expected by the model.

**Reasoning**:
I will generate a code block to prompt the user for each numerical and categorical feature, store the inputs in a dictionary, and then print the dictionary as instructed.
"""

user_input_data = {}

print("Please provide values for the car features:")

# Prompt for numerical features
for feature in numerical_features:
    while True:
        try:
            value = float(input(f"Enter value for {feature}: "))
            user_input_data[feature] = value
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# Prompt for categorical features
# Providing example values for guidance for some common categorical features
example_values = {
    'CarName': 'audi 100ls',
    'fueltype': 'gas',
    'aspiration': 'std',
    'doornumber': 'four',
    'carbody': 'sedan',
    'drivewheel': 'fwd',
    'enginelocation': 'front',
    'enginetype': 'ohc',
    'cylindernumber': 'four',
    'fuelsystem': 'mpfi'
}

for feature in categorical_features:
    example = example_values.get(feature, 'string value')
    value = input(f"Enter value for {feature} (e.g., {example}): ")
    user_input_data[feature] = value

print("\nCollected User Input:")
print(user_input_data)

"""## Preprocess User Input for Prediction

### Subtask:
Construct a pandas DataFrame from the collected user input. Apply `pd.get_dummies()` to this new input, ensuring the resulting columns are aligned with the columns of the training data (`x_train.columns`) by reindexing. Finally, use the saved `StandardScaler` to transform this prepared input data, making it ready for prediction.

**Reasoning**:
I need to construct a pandas DataFrame from the user input, apply one-hot encoding, align its columns with the training data, and then scale it using the previously fitted scaler. This will prepare the user input for prediction.
"""

import pandas as pd

# 1. Create a pandas DataFrame named input_df from the user_input_data dictionary.
input_df = pd.DataFrame([user_input_data])

# 2. Apply one-hot encoding to input_df
# Note: pd.get_dummies needs to be applied to the combined training data first to capture all possible categories for consistent encoding.

# Apply get_dummies to input_df
input_df_encoded = pd.get_dummies(input_df)

# 3. Reindex input_df_encoded to align its columns with x_train.columns.
# Fill any missing columns with zeros. This step is critical to ensure the user input
# has the same features and order as the training data.
input_df_aligned = input_df_encoded.reindex(columns=x_train.columns, fill_value=0)

# 4. Apply the previously fitted scaler to transform input_df_aligned.
input_df_scaled = pd.DataFrame(scaler.transform(input_df_aligned), columns=x_train.columns)

print("Prepared Input Data for Prediction:")
print(input_df_scaled)

"""## Make Prediction with Preprocessed Input

### Subtask:
Use the trained `model` (RandomForestRegressor) to make a prediction on the `input_df_scaled` DataFrame. Print the estimated car price clearly to the user.

**Reasoning**:
I need to use the trained `model` to make a prediction on the `input_df_scaled` and then print the estimated car price.
"""

predicted_price = model.predict(input_df_scaled)
print(f"Estimated Car Price: ${predicted_price[0]:.2f}")

"""# Task
Generate a box plot for the 'price' column of the `dataset` DataFrame to visualize the distribution of car prices, showing the median, quartiles, and outliers, and then summarize the insights from the plot.

## Generate Box Plot

### Subtask:
Create a box plot to visualize the distribution of car prices from the 'price' column of the `dataset` DataFrame. The plot should clearly show the median, quartiles, and any outliers.

**Reasoning**:
I need to generate a box plot of the 'price' column from the `dataset` DataFrame. This involves importing matplotlib, creating the box plot, adding appropriate labels and a title, and then displaying it.
"""

import matplotlib.pyplot as plt

# Create a box plot using the 'price' column of the dataset DataFrame
plt.figure(figsize=(8, 6))
plt.boxplot(dataset['price'])

# Add a title to the plot
plt.title("Distribution of Car Prices")

# Add a label to the y-axis
plt.ylabel("Car Price")

# Display the plot
plt.show()