#UserInput.py
# Parker Mullins

# Import the libraries
import numpy as np
import joblib

# Load the saved model
model = joblib.load('model.joblib')

# Get input from the user
Year = float(input('Enter the student year: '))
University = float(input('Enter the university attended: '))
Major = float(input("Enter the student's major: "))
Time = float(input('Enter the time: '))

# Prepare the input for model prediction
input_list = [Year, University, Major, Time]
input_data = np.array(input_list).reshape(1, -1)

# Make prediction with saved model
prediction = model.predict(input_data)

# Display the prediction for the user
print(f'\nThe predicted order is: {prediction[0]}')