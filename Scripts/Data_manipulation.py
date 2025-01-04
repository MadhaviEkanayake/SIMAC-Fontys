import pandas as pd   

#TODO convert to a class
def get_count(data, column_name, length=0):
    '''
        In a given dataframe, get count of the number of occurances defined by the length of each data point in a specified column. 

        Parameters:
            data (Pandas.DataFrame) : Input table.
            column_name (string): Column name.
            length (int): Length of the data points to be sliced.

        Returns:
            index_list (List) : List of data points in acscending order
            counts (Pandas.Series[int]) : Count of data points in the column 
    '''
    if column_name in data.columns:
        column_data = data[column_name]
        df = pd.DataFrame(column_data)
        # Write the column data to a txt file
        df.columns = ['Name']

        # Count occurrences of each unique value in the given column
        counts = df['Name'].value_counts(sort=True)
        if length != 0:
            counts = counts.iloc[range(length)]

        index_list = counts.index 
        return index_list, counts


def filter_rows(data, keyword, column_name):
    '''
        Funtion to filter. 

        Parameters:

        Returns:

        #TODO complete the doc strings
    '''
    data_list = []
    data_df = data.reset_index()

    for index, row in data_df.iterrows():
        if keyword in row[column_name]:
            data_list.append(row)

    return pd.DataFrame(data_list)        



