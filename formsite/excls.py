import pandas as pd

def read_excel_to_dataframe(excel_file_path, sheet_name=None):
    try:
        if sheet_name:
            df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(excel_file_path)
        
        return df
    except Exception as e:
        print("An error occurred:", e)
        return None

def get_row_by_cell_id(data_frame, cell_id):
    try:
        specific_row = data_frame[data_frame['Cell_ID'] == cell_id]
        return specific_row
    except Exception as e:
        print("An error occurred:", e)
        return None