import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import QuantileTransformer

# Load the saved model
@st.cache_resource
def load_model():
    model = joblib.load("Bengaluru_House_Data")
    return model

# Load the scaler
@st.cache_resource
def create_scaler():
    scaler = QuantileTransformer()
    return scaler

def main():
    st.set_page_config(
        page_title="Bengaluru House Price Predictor",
        page_icon="🏠",
        layout="centered"
    )

    st.title("🏠 Bengaluru House Price Predictor")
    st.write("Enter the details of the house to predict its price")

    # Create columns for a better layout
    col1, col2 = st.columns(2)

    with col1:
        # Area Type (0 to 3)
        area_type = st.selectbox(
            "Area Type",
            options=[0, 1, 2, 3],
            help="Select the area type (0-3)"
        )

        # Size (0 to 19)
        size = st.number_input(
            "Size (BHK)",
            min_value=0,
            max_value=19,
            value=2,
            help="Number of bedrooms (0-19)"
        )

        # Total Square Feet (0 to 2116)
        total_sqft = st.number_input(
            "Total Square Feet",
            min_value=0,
            max_value=2116,
            value=1000,
            help="Total square feet area (0-2116)"
        )

    with col2:
        # Bath (0 to 19)
        bath = st.number_input(
            "Number of Bathrooms",
            min_value=0,
            max_value=19,
            value=2,
            help="Number of bathrooms (0-19)"
        )

        # Balcony (0 to 4)
        balcony = st.number_input(
            "Number of Balconies",
            min_value=0,
            max_value=4,
            value=1,
            help="Number of balconies (0-4)"
        )

    # Create a predict button
    if st.button("Predict Price", type="primary"):
        try:
            # Load the model
            model = load_model()
            scaler = create_scaler()

            # Prepare the input data
            input_data = np.array([[area_type, size, total_sqft, bath, balcony]])
            
            # Transform the input data
            input_scaled = scaler.fit_transform(input_data)
            
            # Make prediction
            prediction = model.predict(input_scaled)

            # Display the prediction in a nice format
            st.success("Predicted House Price:")
            st.header(f"₹ {prediction[0]:,.2f}")
            
            # Add some context
            st.info("""
            Note: This prediction is based on historical Bengaluru housing data. 
            Actual prices may vary based on current market conditions and specific location details.
            """)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.warning("Please make sure all input values are within the specified ranges.")

    # Add information about the input ranges
    with st.expander("ℹ️ Input Range Information"):
        st.markdown("""
        - **Area Type**: 0 to 3 (categorical encoding)
        - **Size**: 0 to 19 BHK (Bedroom, Hall, Kitchen)
        - **Total Square Feet**: 0 to 2116 sq.ft
        - **Bathrooms**: 0 to 19
        - **Balconies**: 0 to 4
        """)

    # Add footer
    st.markdown("---")
    st.markdown("Built with Streamlit and XGBoost")

if __name__ == "__main__":
    main()