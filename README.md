# Poultry Weight Predictor 🐔

A machine learning application built with Streamlit for predicting poultry weight based on environmental and feeding data. This tool helps poultry farmers and researchers make data-driven decisions for optimal poultry growth management.

## Features

### 1. Data Management
- **Data Upload**: Support for CSV file uploads with automated validation
- **Data Preprocessing**: Automatic handling of missing values and data type conversions
- **Data Visualization**: Interactive charts and statistics for uploaded data
- **Data Validation**: Comprehensive checks for data quality and completeness

### 2. Analysis Tools
- **Data Analysis**: 
  - Time series analysis of weight progression
  - Feature relationship visualization
  - Correlation analysis
  - Outlier detection
- **Statistical Insights**: 
  - Basic statistics for all features
  - Distribution analysis
  - Data quality metrics

### 3. Model Training
- **Polynomial Regression Model**:
  - Configurable test/train split
  - Feature importance analysis
  - Model performance metrics
- **Model Evaluation**:
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R-squared (R²) score
- **Model Management**:
  - Save trained models
  - Load existing models
  - Model performance comparison

### 4. Prediction Capabilities
- **Manual Input Prediction**:
  - Individual predictions with instant results
  - Input validation
  - Prediction history tracking
- **Batch Prediction**:
  - CSV file upload for multiple predictions
  - Bulk processing capabilities
  - Downloadable results

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/poultry-weight-predictor.git
cd poultry-weight-predictor
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure
```
poultry_weight_predictor/
│
├── app/
│   ├── main.py                  # Main application entry point
│   │
│   ├── pages/
│   │   ├── 1_Data_Upload.py       # Data upload and validation
│   │   ├── 2_Data_Analysis.py     # Data analysis and visualization
│   │   ├── 3_Model_Training.py    # Model training and evaluation
│   │   ├── 4_Predictions.py       # Making predictions
│   │   └── 5_About.py            # About page
│   │
│   ├── models/
│   │   ├── polynomial_regression.py  # Model implementation
│   │   └── model_utils.py           # Model utilities
│   │
│   ├── utils/
│   │   ├── data_processor.py      # Data processing utilities
│   │   ├── visualizations.py      # Visualization functions
│   │   └── validation.py          # Data validation
│   │
│   └── config/
│       └── settings.py            # Application settings
│
├── models/                      # Saved models directory
├── data/                       # Sample data directory
├── tests/                      # Unit tests
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Usage

1. Start the application:
```bash
streamlit run app/main.py
```

2. Navigate through the pages:
   - **Data Upload**: Upload your CSV file
   - **Data Analysis**: Explore your data
   - **Model Training**: Train and evaluate the model
   - **Predictions**: Make predictions

### Required Data Format

Your CSV file should include these columns:
- `Int Temp`: Internal Temperature (°C)
- `Int Humidity`: Internal Humidity (%)
- `Air Temp`: Air Temperature (°C)
- `Wind Speed`: Wind Speed (m/s)
- `Feed Intake`: Feed Intake (g)
- `Weight`: Weight (g) - required for training data only

## Making Predictions

### Manual Input
1. Navigate to the Predictions page
2. Select "Manual Input"
3. Enter values for all required features
4. Click "Predict" to get results

### Batch Predictions
1. Prepare a CSV file with required features
2. Upload the file in the Predictions page
3. Download the results with predictions

## Model Details

### Feature Engineering
- Polynomial features (degree 2)
- Standard scaling of features
- Automated feature importance analysis

### Model Performance Metrics
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²) score
- Feature importance ranking

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- Your Name
- Contact Information

## Acknowledgments

- Built with Streamlit
- Uses scikit-learn for machine learning
- Plotly for visualizations
- Pandas for data manipulation

## Support

For support or feature requests, please:
1. Check existing issues
2. Create a new issue with detailed description
3. Contact the maintainers

---

Made with ❤️ for poultry farmers and researchers