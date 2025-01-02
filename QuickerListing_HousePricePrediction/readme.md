(a)Configuring API Key
(i)Access the NASA api portal with the url: https://api.nasa.gov/ 
(ii)Click on Generate API Key , enter the details for sign up
<API key would be sent to email id, after sign up>
(iii) Create a file 'nasa_api.env' in the 'Input' folder
(iv) Add the API key in the file in the following format:
	Api_Key="Replace the api key over here without double quotes"
	and save the file

(b)Installing libraries
(i)Run the following command in the terminal:
	pip install requests tqdm python-dotenv numpy pandas category-encoders scikit-learn seaborn matplotlib

(c)Please Click RunAll for each of the .ipynb files in the following order:
Problem1.ipynb
Problem2.ipynb
Problem3.ipynb
Problem4.ipynb
Note: Ensure that all the cells are run in one .ipynb file, before running the next file.
(Since the output from one .ipynb file might server as input for the other .ipynb file)

####################################
(a)Configuring Hostname for MongoDB and PostGres:
Update the hostname for MongoDB in config.json file,against the following fields:
 "DB_HOST_MONGO": <replace with host name for mongoDB>,
Update the hostname,database name,username and password for Postgres in config.json file,against the following fields:
"DB_HOST_POSTGRES": <replace with host name for postgresDB>,
"DATABASE_POSTGRES": <replace with database name for postgresDB>,
"DB_USER_POSTGRES": <replace with username for postgresDB>,
"DB_PWD_POSTGRES": <replace with password for postgresDB>




