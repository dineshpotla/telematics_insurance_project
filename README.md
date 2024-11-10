
# Telematics-Driven Vehicle Insurance Risk Assessment Platform

## Overview
This project is an end-to-end solution for assessing vehicle insurance risk using telematics data. It includes data processing, machine learning model training, a real-time API for predictions, and a dashboard for data visualization.

## Project Structure
- `data/`: Contains sample datasets for telematics and insurance claims.
- `models/`: Includes saved machine learning models.
- `app/`: Contains the Flask API (`main.py`) for real-time risk assessment.
- `dashboard/`: Contains the Streamlit dashboard (`dashboard.py`) for data visualization.
- `notebooks/`: Jupyter notebooks for data processing and model training.
- `README.md`: Project documentation.
- `LICENSE`: License for the project.

## Installation
To set up this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dineshpotla/telematics_insurance_project.git
   cd telematics_insurance_project
   ```

2. **Install dependencies**:
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Running the API
The Flask API allows you to make real-time predictions based on telematics data.

1. **Navigate to the `app` directory**:
   ```bash
   cd app
   ```

2. **Run the API**:
   ```bash
   python main.py
   ```
   The API will start on `http://127.0.0.1:5000`. You can send data to the `/predict` endpoint for risk predictions.

### Running the Dashboard
The Streamlit dashboard provides visual insights into telematics data and predictions.

1. **Navigate to the `dashboard` directory**:
   ```bash
   cd dashboard
   ```

2. **Run the Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```
   The dashboard will open in your default web browser.

## Contributing
If you’d like to contribute to this project, please fork the repository and make a pull request. For major changes, please open an issue first to discuss what you’d like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
