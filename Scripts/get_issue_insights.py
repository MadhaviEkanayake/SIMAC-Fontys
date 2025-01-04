import pandas as pd   
from pathlib import Path
from Data_manipulation import get_count, filter_rows 

def main():
    
    # defining file path        
    file_path = Path('G:\\Fontys\\Data_Set\\Python_scripts\\files\\data_file.csv')
    df = pd.read_csv(file_path, encoding='latin-1' )

    column_name = "Description"
  
    issue_list, issue_counts = get_count(df, column_name, length=18)
    
    agenda_list = {"Issue Name":issue_list }
    dframe_issues = pd.DataFrame(agenda_list)

    issue_count_list = []
    issue_store_list = []

    for issue in issue_list:
        date_count_list = []
        dummy_store_list = []
        dates_list = []
        dummy_store_count_list = []

        # dataframe of filtered data by issue
        stores = filter_rows(df, issue, column_name)

        # store list = list of stores with count , store count = dataframe of the stores and count of the incidents 
        store_list, store_count = get_count(stores, column_name= "Vestiging", length=10)
        i = 0
        for store in store_list:
            dates = filter_rows(stores, store, column_name= "Vestiging")
            date_list, date_count = get_count(dates, column_name= "Date created")

            dummy_store_list.append(store)
            dummy_store_count_list.append(store_count.iloc[i])
            i += 1
            # postprocess to be written as a excel table
            for n in range((len(date_list)-1)):
                dummy_store_list.append(" ") # add spaces to compensate for the length difference
                dummy_store_count_list.append(" ")
            date_count_list.extend(date_count)
            dates_list.extend(date_list)

        dict = {"Store":dummy_store_list, "Date":dates_list, "Count":date_count_list, "Total":dummy_store_count_list }
        dframe = pd.DataFrame(dict)

        issue_store_list.append(dframe)

    with pd.ExcelWriter(Path(file_path.parent,"issue_list.xlsx")) as writer:
        i = 0 
        dframe_issues.to_excel(writer, sheet_name=("Agenda"))
        for dataframe in issue_store_list:
            
            dataframe.to_excel(writer,index = False, sheet_name=("issue "+str(i)))  
            i = i + 1
        
if __name__ == '__main__': 
    main()