#importing general objects
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
# install('plotly')
install('statsmodels')
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
import plotly.figure_factory as ff

#TODO: reading in the dataset


#Some basic commands in streamlit -- you can find an amazing cheat sheet here: https://docs.streamlit.io/library/cheatsheet
st.title('Examining Factors that affect MPG')
st.write('For the past one hundred years, many bright minds have come together in effort to find ways to improve vehicles. Vehicle manufactuers spend countless hours looking for the smallest optimizations that will reduce production costs, increase vehicle efficiency, and ultimately improve the safety and reliability of their vehicles. For that reason, I will be looking at a small dataset containing under 400 unique vehicles with features such as cylinders, mpg, weight, acceleration, horsepower, and other important features. From this experiment I hope to glean what features display the strongest negative relationship to mpg.')
st.markdown("""---""")
#generate random data for my example dataframe -- howto: https://stackoverflow.com/questions/32752292/how-to-create-a-dataframe-of-random-integers-with-pandas
df = pd.read_csv('mpg_cleaned.csv')

#show off a bit of your data. 
st.header('The Data')
col1, col2 = st.columns(2) #here is how you can use columns in streamlit. 
col1.dataframe(df.head())
col2.markdown("\n") #add a line of empty space.
col2.markdown('This dataset contains exactly 392 unique cars that were released from 1970 to 1982. The features that we will be analyzing in this experiment are mpg, cylinders, and weight.') #you can add multiple items to each column.

st.markdown("""---""")

st.header("Hypothesis")
st.write('I believe that factors such as the number of cylinders and vehicle weight will have the strongest correlation to mpg. That is, the number of cylinders and the vehicle weight will display the strongest negative relationship with MPG. For my first visual I will be creating a box plot which examines the relationship between the number of cylinders and vehicle mpg. The second visual will be a scatter plot which examines the relationship between weight and mpg. The final visual will be a correlation heatmap which will serve to confirm or deny the hypothesis.')

st.header('Findings')


st.plotly_chart(px.box(df, x="cylinders", y="mpg", color="cylinders"))
st.write("Note: This dataset contains vehicles from 1970-1982. As of 2022, three cylinder vehicles have the best mpg. Also, 7 cylinder cars are extremely rare and you won't find any common manufactuer producing them.")

st.plotly_chart(px.scatter(df, x="weight", y="mpg", trendline='ols'))
st.markdown("From our visual we can clearly see a negative relationship between weight and mpg. As a car's weight increases there is a decrease in the mpg. Now, we can turn to our correlation matrix which will confirm or deny our initial hypthosesis.")

corr = df.corr()
x = list(corr.columns)
y = list(corr.index)
z = np.array(corr)
st.plotly_chart(ff.create_annotated_heatmap(
    z,
    x = x,
    y = y ,
    annotation_text = np.around(z, decimals=2),
    hoverinfo='z',
    colorscale='greys'
    ))



st.markdown("""---""")

#Always good to section out your code for readability.
st.header('Conclusions')
st.write('From our correlation heatmap we can see that weight has the highest negative correlation with mpg at -.83. Moreover, the number of cylinders was tied for third most negatively correlated feature with mpg at -.78. All-in-all if vehicle manufactuers aim to lower mpg they should focus their efforts on producing cars that are as light as possible and have the four or less cylinders.')
st.write('Created by Elian Ahmar')