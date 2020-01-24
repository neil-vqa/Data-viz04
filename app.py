import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import numpy as np


x_label = ['Ranked 1st', 'Ranked 2nd', 'Ranked 3rd', 'Ranked 4th', 'Ranked 5th', 'Ranked 6th']
y_label = ['They have similar interests to me','They have/make a decent amount of money','They are intelligent','They have a sense of humour I like','They have a personality I like','They are good looking']

@st.cache
def data_load():
	return pd.read_excel('Looks vs Personality.xlsx')
	
def main():
	data = data_load()

	st.title('What do you look for in a romantic partner?')
	st.write('Survey results of what Men & Women generally prefer for a possible partner.')
	st.write('*Columns show the percentage of men/women ranking a particular characteristic from 1st to 6th.*')

	option1 = st.selectbox('Select nationality', data['Nationality'].unique())
	option2 = st.selectbox('Select gender', data['Gender'].unique())

	st.title(option1 + ' ' + option2)

	cut_data = data.drop(columns=['Unweighted_Sample','Weighted_Sample'])
	man = cut_data.loc[(data['Nationality']==option1) & (data['Gender']==option2)]

	row_put = []
	row_label = []
	
	for i in y_label:
		row = man.loc[man['Question']==i]['Percentage']*100
		row = np.round(row, decimals=1)
		rowl = list(row)
		rowx = [str(i) + ' %' for i in rowl]
		row_label.append(rowx)
		row_put.append(rowl)
	
	z = row_put
	x = x_label
	y = y_label


	plot = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=row_label, colorscale='Reds')
	plot.update_layout(width=900,height=800)

	st.plotly_chart(plot)
	
	st.markdown('Data Source: YouGov, 2017')
	st.markdown('Viz by: nvqa')
	
if __name__ == '__main__':
	main()

