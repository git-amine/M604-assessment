import wbgapi as wb
import src.config.config as config



# Retrieve data from world bank database using API

def retrieve_data(db_code,range=range(config.start_year, config.end_year + 1)):

    df = wb.data.DataFrame(db_code,'all',range,numericTimeKeys=True,labels=True)

    return df




