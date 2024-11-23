# Quick Start Guide

## 🚀 Getting Started with Poultry Weight Predictor

### Step 1: Data Preparation
1. Prepare your CSV file with the following columns:
   - Int Temp (Internal Temperature in °C)
   - Int Humidity (Internal Humidity in %)
   - Air Temp (Air Temperature in °C)
   - Wind Speed (in m/s)
   - Feed Intake (in g)
   - Weight (in g) - for training data only

2. Ensure your data:
   - Has no missing values
   - Uses numbers only (no text)
   - Uses correct units

### Step 2: Data Upload
1. Go to the "Data Upload" page
2. Click "Upload CSV file"
3. Select your prepared CSV file
4. Review the data preview and statistics

### Step 3: Data Analysis
1. Navigate to "Data Analysis"
2. Explore:
   - Feature distributions
   - Correlations
   - Time series trends
   - Outliers

### Step 4: Model Training
1. Go to "Model Training"
2. Adjust the test set size if needed
3. Click "Train Model"
4. Review:
   - Model performance metrics
   - Feature importance
   - Prediction accuracy

### Step 5: Making Predictions
1. Navigate to "Predictions"
2. Choose:
   - Manual Input: for single predictions
   - Batch Prediction: for multiple predictions
3. Get results and download if needed

## 📊 Sample Data Format

```csv
Int Temp,Int Humidity,Air Temp,Wind Speed,Feed Intake,Weight
29.87,59,29.6,4.3,11.00,42.39
32.50,47,30.5,4.3,12.47,45.67
33.47,48,31.35,4.7,10.46,48.92
```

## 🔍 Tips for Best Results

1. **Data Quality**:
   - Clean your data before uploading
   - Remove obvious outliers
   - Ensure consistent units

2. **Model Training**:
   - Use sufficient training data (minimum 20 samples)
   - Balance your test set size
   - Review feature importance

3. **Predictions**:
   - Stay within the range of training data
   - Use consistent units
   - Validate unusual predictions

## ❗ Common Issues and Solutions

1. **Upload Errors**:
   - Check CSV format
   - Verify column names
   - Remove special characters

2. **Training Errors**:
   - Ensure sufficient data
   - Check for missing values
   - Verify data types

3. **Prediction Errors**:
   - Validate input ranges
   - Check units
   - Ensure model is trained

## 🆘 Getting Help

If you encounter issues:
1. Check the error message
2. Review data format
3. Contact support with:
   - Error description
   - Sample data (if possible)
   - Steps to reproduce

---

For more detailed information, see the full README.md