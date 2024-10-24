# Bengaluru House Price Prediction 🏠

A machine learning web application that predicts house prices in Bengaluru using XGBoost. The application features an interactive user interface built with Streamlit, making it easy for users to input house details and get price predictions instantly.

## 📌 Features

- **Interactive Web Interface**: User-friendly Streamlit dashboard
- **Real-time Predictions**: Get instant price predictions based on input parameters
- **Input Validation**: Built-in validation to ensure data quality
- **Responsive Design**: Works well on both desktop and mobile devices
- **Machine Learning Model**: Powered by XGBoost algorithm
- **Data Preprocessing**: Automated scaling and transformation of inputs

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **ML Library**: XGBoost, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Model Serialization**: Joblib

## 📋 Prerequisites

- Python 3.7+
- Git

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/assistantsir12345/house_price_prediction.git
   cd house_price_prediction
   ```

2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:8501`

## 📝 Input Parameters

The application accepts the following inputs:

| Parameter | Range | Description |
|-----------|-------|-------------|
| Area Type | 0-3 | Encoded category of the area |
| Size (BHK) | 0-19 | Number of Bedrooms, Hall, Kitchen |
| Total Square Feet | 0-2116 | Total area in square feet |
| Bathrooms | 0-19 | Number of bathrooms |
| Balconies | 0-4 | Number of balconies |

## 🧪 Sample Test Cases

Try these sample inputs to test the application:

1. **Mid-Range House**
   - Area Type: 2
   - Size: 3 BHK
   - Total Square Feet: 1200
   - Bathrooms: 2
   - Balconies: 2

2. **Budget Apartment**
   - Area Type: 1
   - Size: 2 BHK
   - Total Square Feet: 800
   - Bathrooms: 1
   - Balconies: 1

3. **Luxury Villa**
   - Area Type: 3
   - Size: 4 BHK
   - Total Square Feet: 2000
   - Bathrooms: 4
   - Balconies: 3

## 📁 Project Structure

```
house_price_prediction/
├── app.py              # Streamlit application
├── Bengaluru_House_Data# Saved ML model
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## ⚠️ Known Limitations

- The model is trained on historical data and may not reflect current market prices
- Predictions are based on limited features and may not capture all price-influencing factors
- Area types are encoded, refer to the original dataset for mapping

## 📫 Support

For support, email assistantsir12345@gmail.com or open an issue in the GitHub repository.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
