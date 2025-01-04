(a)Configuring Hostname for MongoDB and PostGres:
Update the hostname for MongoDB in config.json file,against the following fields:
 "DB_HOST_MONGO": <replace with host name for mongoDB>,
Update the hostname,database name,username and password for Postgres in config.json file,against the following fields:
"DB_HOST_POSTGRES": <replace with host name for postgresDB>,
"DATABASE_POSTGRES": <replace with database name for postgresDB>,
"DB_USER_POSTGRES": <replace with username for postgresDB>,
"DB_PWD_POSTGRES": <replace with password for postgresDB>

(b)Installing libraries:
pip install selenium webdriver-manager tqdm pandas numpy pymongo psycopg2-binary matplotlib seaborn scikit-learn xgboost tensorflow keras

(c)Please Click RunAll for WebScraping.ipynb file:
(1)Kindly note that code cell '3' will take 15-16 min to execute and the progress of the same would be visible from the progress bar , in the third cell. Please refrain from locking the screen, until then as it might interupt the webdriver's action  intermittently. 

(d)Access the data visualisation in Streamlit App, with the url below:
https://housepriceprediction-quickerlisting.streamlit.app/
