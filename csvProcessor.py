import pandas as pd

# Read the CSV file into a DataFrame
def process_csv(file_name):
	df = pd.read_csv(file_name)
	df.dropna(inplace=True)
	# Print the first few rows to inspect

	df_list_dict = df.to_dict(orient='series')

	return df_list_dict

""" filtered_df = df[df['encounterId']]
print(filtered_df) """
