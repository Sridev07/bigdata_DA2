# bigdata_DA2 
DATASET DESCRIPTION
Dataset Title: Digital Wallet Transaction Dataset
This dataset contains detailed logs of financial transactions performed using a digital wallet platform. It provides valuable insights into user behavior, transaction patterns, and potential anomalies, making it ideal for machine learning tasks such as fraud detection, customer segmentation, and recommendation systems.

Dataset Overview
The dataset includes transaction details across various categories and merchants, with key attributes related to the user, the merchant, the transaction status, and payment method.

Features:
idx: Unique identifier for each transaction.
transaction_id: Unique ID for each transaction.
user_id: Unique identifier of the user making the transaction.
transaction_date: Timestamp of when the transaction occurred.
product_category: Category of the product or service involved (e.g., electronics, apparel).
product_name: Specific name of the product or service being purchased.
merchant_name: Name of the merchant where the transaction occurred.
product_amount: The monetary value of the product/service purchased.
transaction_fee: Fee associated with processing the transaction.
cashback: Amount of cashback offered to the user for the transaction.
loyalty_points: Loyalty points awarded for completing the transaction.
payment_method: Payment method used (e.g., credit card, bank transfer, digital wallet).
transaction_status: Status of the transaction: successful, pending, or failed.
merchant_id: Unique identifier of the merchant.
device_type: Device used for the transaction (e.g., mobile, desktop, tablet).
location: Geographical location (city or country) from where the transaction was made.
Use Cases
This dataset can be used for various data science and machine learning applications, including but not limited to:

Fraud Detection: Identify potentially fraudulent transactions based on transaction patterns.
Customer Segmentation: Group users into segments based on purchase behavior or product preferences.
Recommendation Systems: Recommend products or services to users based on their transaction history and engagement.
Anomaly Detection: Detect unusual patterns such as failed or pending transactions that could indicate issues or risks.
Potential Applications
Clustering: Group users or merchants based on transaction patterns using algorithms like K-Means or Self-Organizing Maps (SOM).
Classification: Predict transaction outcomes (successful, pending, failed) using supervised learning techniques.
Time-Series Analysis: Analyze transaction trends over time, such as seasonality in product sales or changes in user engagement.
Visualization: Use Self-Organizing Maps (SOM) to visualize and identify transaction clusters or anomalies in the dataset.
Dataset Format
File Format: CSV
Number of Records: Varies (thousands to millions of transactions)
Number of Features: 16 columns
Example Applications
Fraud Detection: By analyzing attributes such as transaction_status, product_amount, and location, machine learning models can be developed to detect fraudulent transactions.
Movie Recommendation Systems: The dataset can be adapted for a recommendation engine by analyzing user behavior, preferences, and transactions related to entertainment services.
SOM for Visualization: Use SOM to visualize user behaviors and categorize transactions, identifying clusters of users who behave similarly.

Execution:
step1: install necessary libraries from the import statements i gave.(pip install)
Step2: python3.12 setup and minisom (self orgranising map).
Step3: run the soma.py
Step4: i have chosen to show red circle that indicates payment failed,pending and green boxes for payment successful. based on this it will show the self organising map figure with use minisom.

