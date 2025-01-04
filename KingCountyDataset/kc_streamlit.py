import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import *
from xgboost import XGBRegressor

script_dir = os.path.dirname(os.path.abspath(__file__))


file_path = os.path.join(script_dir, "transformed_data.xls")


df = pd.read_csv(file_path)

bedrooms = st.sidebar.selectbox("Bedrooms:",sorted(df['bedrooms'].unique().tolist()))
bathrooms = st.sidebar.selectbox("Bathrooms:",sorted(df['bathrooms'].unique().tolist()))
sqft_living=st.sidebar.slider("Sqft_living",int(df['sqft_living'].min()),int(df['sqft_living'].max()))
sqft_lot=st.sidebar.slider("Sqft_lot",int(df['sqft_lot'].min()),int(df['sqft_lot'].max()))
floors=st.sidebar.selectbox("Floors",sorted(df['floors'].unique().tolist()))
waterfront=st.sidebar.selectbox("Waterfront",sorted(df['waterfront'].unique().tolist()))
view=st.sidebar.selectbox("View",sorted(df['view'].unique().tolist()))
condition=st.sidebar.selectbox("Condition",sorted(df['condition'].unique().tolist()))
grade=st.sidebar.selectbox("Grade",sorted(df['grade'].unique().tolist()))
sqft_above=st.sidebar.slider("Sqft_Above",int(df['sqft_above'].min()),int(df['sqft_above'].max()))
sqft_basement=st.sidebar.slider("Sqft_Basement",int(df['sqft_basement'].min()),int(df['sqft_basement'].max()))
yr_built=st.sidebar.slider("Year Built",int(df['yr_built'].min()),int(df['yr_built'].max()))
zipcode=st.sidebar.selectbox("ZipCode",sorted(df['zipcode'].unique().tolist()))
sqft_living15=st.sidebar.slider("Sqft_Living15",int(df['sqft_living15'].min()),int(df['sqft_living15'].max()))
sqft_lot15=st.sidebar.slider("Sqft_Lot15",int(df['sqft_lot15'].min()),int(df['sqft_lot15'].max()))
Month=st.sidebar.slider("Month",int(df['yr_built'].min()),int(df['yr_built'].max()))
Year=st.sidebar.slider("Year",int(df['Year'].min()),int(df['Year'].max()))
house_age=st.sidebar.slider("House Age",int(df['house_age'].min()),int(df['house_age'].max()))
renovated=st.sidebar.selectbox("Renovated",sorted(df['renovated'].unique().tolist()))
roomhasbathroom=st.sidebar.selectbox("Room has bathroom",sorted(df['room_has_bathroom'].unique().tolist()))

Y=df['price']
df=df.drop(columns=['lat','long','price'])
X=df

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

# Initialize the model
model = XGBRegressor(
    n_estimators=100,
    eval_metric='rmse',
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

 
# Train the model
model.fit(X_train, Y_train)

# Make predictions
y_pred = model.predict(X_test)


user_input = np.array([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,
sqft_basement,yr_built,zipcode,sqft_living15,sqft_lot15,Month,Year,house_age,renovated,roomhasbathroom]])
prediction = model.predict(user_input)

predicted_target=prediction[0]


st.markdown(
    "<h3 style='text-align: left; color: black;'>House Price Prediction with XGBoost Regressor</h3>", 
    unsafe_allow_html=True
)
st.markdown(
    f"<p style='text-align: left; font-size: 20px; color: green;'>The Predicted House Price is <strong>{predicted_target}</strong></p>", 
    unsafe_allow_html=True
)
