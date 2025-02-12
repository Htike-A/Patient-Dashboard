import pandas as pd


def process_csv(file_name ):
	df = pd.read_csv(file_name)
	df.dropna(inplace=True)


	a = df[df['referral'] == 1]


	df_list_dict = df.to_dict(orient='records')

	return df_list_dict

