import streamlit as st
import pandas as pd
import os
import joblib
from utils.data_processor import DataProcessor, FEATURE_COLUMNS
from utils.visualizations import Visualizer
from models.polynomial_regression import PoultryWeightPredictor
from config.settings import MODEL_SAVE_PATH

def app():
    st.title("🎯 Model Training")
    
    # Check if data exists in session state
    if 'data' not in st.session_state:
        st.error("Please upload data in the Data Upload page first!")
        st.stop()
    
    # Initialize objects
    data_processor = DataProcessor()
    visualizer = Visualizer()
    model = PoultryWeightPredictor()
    
    # Get data
    df = st.session_state['data']
    
    # Preprocess data first
    try:
        df_processed = data_processor.preprocess_data(df)
        st.success(f"Data preprocessed successfully: {df_processed.shape[0]} rows")
        
        # Save data_processor in session state for predictions
        st.session_state['data_processor'] = data_processor
        
    except Exception as e:
        st.error(f"Error preprocessing data: {str(e)}")
        st.stop()
    
    # Sidebar options
    st.sidebar.subheader("Training Options")
    
    # Calculate minimum and maximum allowed test size
    min_test_size = max(0.1, 1 / len(df_processed))  # At least 1 sample or 10%
    max_test_size = 0.4  # Maximum 40%
    
    test_size = st.sidebar.slider(
        "Test Set Size", 
        min_value=min_test_size,
        max_value=max_test_size,
        value=0.2,
        step=0.05,
        help="Proportion of dataset to include in the test split"
    )
    
    # Show data information
    st.sidebar.subheader("Data Information")
    total_samples = len(df_processed)
    train_samples = int(total_samples * (1 - test_size))
    test_samples = total_samples - train_samples
    
    st.sidebar.write("Data Split:")
    st.sidebar.write(f"- Total samples: {total_samples}")
    st.sidebar.write(f"- Training samples: {train_samples}")
    st.sidebar.write(f"- Testing samples: {test_samples}")
    
    # Main content
    st.subheader("Data Split and Model Training")
    
    # Show feature information
    st.write("Features being used:", FEATURE_COLUMNS)
    
    # Prepare features
    try:
        X_train, X_test, y_train, y_test = data_processor.prepare_features(
            df_processed, 
            test_size=test_size
        )
        st.success("Features prepared successfully")
        
        # Show shapes
        st.write(f"Training set shape: {X_train.shape}")
        st.write(f"Test set shape: {X_test.shape}")
        
    except Exception as e:
        st.error(f"Error preparing features: {str(e)}")
        st.stop()
    
    # Save test data in session state
    st.session_state['test_data'] = {
        'X_test': X_test,
        'y_test': y_test
    }
    
    # Training progress
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Initialize session state
    if 'training_results' not in st.session_state:
        st.session_state['training_results'] = None
    
    # Train model button
    if st.button("Train Model"):
        try:
            status_text.text("Training model...")
            progress_bar.progress(25)
            
            # Train the model
            model.train(X_train, y_train)
            progress_bar.progress(50)
            
            # Evaluate the model
            metrics, y_pred = model.evaluate(X_test, y_test)
            progress_bar.progress(75)
            
            # Get feature importance
            importance_dict = model.get_feature_importance(FEATURE_COLUMNS)
            progress_bar.progress(100)
            
            # Store results
            st.session_state['model'] = model
            st.session_state['training_results'] = {
                'metrics': metrics,
                'predictions': y_pred,
                'feature_importance': importance_dict,
                'test_size': test_size
            }
            
            status_text.text("Training completed!")
            
        except Exception as e:
            st.error(f"Error during training: {str(e)}")
            import traceback
            st.code(traceback.format_exc())
            progress_bar.empty()
            status_text.empty()
    
    # Display results if available
    if st.session_state.get('training_results'):
        results = st.session_state['training_results']
        metrics = results['metrics']
        y_pred = results['predictions']
        importance_dict = results['feature_importance']
        
        # Display metrics
        st.subheader("Model Performance")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Mean Squared Error", f"{metrics['mse']:.2f}")
        with col2:
            st.metric("Root MSE", f"{metrics['rmse']:.2f}")
        with col3:
            st.metric("R² Score", f"{metrics['r2']:.4f}")
        
        # Create tabs for different visualizations
        tab1, tab2 = st.tabs(["Predictions", "Feature Importance"])
        
        with tab1:
            st.subheader("Actual vs Predicted Values")
            prediction_plot = visualizer.plot_actual_vs_predicted(
                st.session_state['test_data']['y_test'],
                y_pred
            )
            st.plotly_chart(prediction_plot, use_container_width=True)
            
            if st.checkbox("Show detailed predictions"):
                n_examples = min(10, len(y_pred))
                examples = pd.DataFrame({
                    'Actual Weight': st.session_state['test_data']['y_test'][:n_examples],
                    'Predicted Weight': y_pred[:n_examples],
                    'Absolute Error': abs(
                        st.session_state['test_data']['y_test'][:n_examples] - 
                        y_pred[:n_examples]
                    ),
                    'Relative Error (%)': abs(
                        st.session_state['test_data']['y_test'][:n_examples] - 
                        y_pred[:n_examples]
                    ) / st.session_state['test_data']['y_test'][:n_examples] * 100
                })
                st.dataframe(examples)
        
        with tab2:
            st.subheader("Feature Importance")
            importance_plot = visualizer.plot_feature_importance(
                list(importance_dict.keys()),
                list(importance_dict.values())
            )
            st.plotly_chart(importance_plot, use_container_width=True)
            
            # Show feature importance table
            st.write("Feature Importance Values:")
            importance_df = pd.DataFrame({
                'Feature': importance_dict.keys(),
                'Importance': importance_dict.values()
            })
            st.dataframe(importance_df)

            # Model saving section
        st.subheader("Save Model")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            model_name = st.text_input(
                "Model Name", 
                value=f"poultry_model_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}",
                help="Enter a name for the model or use the default timestamp-based name"
            )
        
        with col2:
            if st.button("Save Model", use_container_width=True):
                try:
                    if not model_name:
                        st.error("Please enter a model name")
                        return
                    
                    # Ensure .joblib extension
                    if not model_name.endswith('.joblib'):
                        model_name += '.joblib'
                    
                    # Create full path
                    os.makedirs(MODEL_SAVE_PATH, exist_ok=True)
                    full_path = os.path.join(MODEL_SAVE_PATH, model_name)
                    
                    # Create save dictionary
                    save_dict = {
                        'model': model,
                        'data_processor': data_processor,
                        'feature_columns': FEATURE_COLUMNS,
                        'training_date': pd.Timestamp.now(),
                        'training_metrics': metrics,
                        'test_size': test_size
                    }
                    
                    # Save everything
                    joblib.dump(save_dict, full_path)
                    
                    # Success message
                    st.success(f"Model saved successfully!")
                    st.info(f"Save location: {full_path}")
                    
                    # Additional information
                    st.write("Saved contents:")
                    for key in save_dict.keys():
                        st.write(f"- {key}")
                        
                except Exception as e:
                    st.error(f"Error saving model: {str(e)}")
                    st.code(traceback.format_exc())
        


if __name__ == "__main__":
    app()