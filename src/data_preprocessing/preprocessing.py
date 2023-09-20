import src.config.db_codes as db_code
import src.data_retrieval.data_retrieval as retrieve
import src.data_preprocessing.countries as country
import src.config.config as config
import pandas as pd

# performs various initial transformations on the dataset

def preprocess_database(df, removed=config.END_COUNTRIES_DATA, thresh=config.thresh):

    # remove data not related to individual countries
    df = df.iloc[:-removed]

    # drop countries with not enough data points
    df = df.dropna(thresh=thresh)

    # forward fill of missing values
    df = df.fillna(method="bfill", axis="columns")

    # backward fill of missing values
    df = df.fillna(method="ffill", axis="columns")

    # add continent column to dataset
    df['Continent'] = df['Country'].apply(country.country_to_continent)

    return df

# melt the dataframe and add education level and population label columns

def prep_melt_dataframe(df,educ_level_label,population_label ):

    df=preprocess_database(df)
    df = pd.melt(df, id_vars=['Country', 'Continent'], var_name='year', value_name='unemployment_rate')
    df['Education']=educ_level_label
    df['Population']=population_label
    return df


# Prepares the final dataset by preporcessing and concatenating all the 9 world bank datasets

def prep_dataset():


    # retrieve 9 datasets from the world bank database

    df_advanced_total = retrieve.retrieve_data(db_code.unemployment_advanced_education)
    df_advanced_female = retrieve.retrieve_data(db_code.unemployment_advanced_education_female)
    df_advanced_male = retrieve.retrieve_data(db_code.unemployment_advanced_education_male)

    df_intermediate_total = retrieve.retrieve_data(db_code.unemployment_intermediate_education)
    df_intermediate_female = retrieve.retrieve_data(db_code.unemployment_intermediate_education_female)
    df_intermediate_male = retrieve.retrieve_data(db_code.unemployment_intermediate_education_male)

    df_basic_total = retrieve.retrieve_data(db_code.unemployment_basic_education)
    df_basic_female = retrieve.retrieve_data(db_code.unemployment_basic_education_female)
    df_basic_male = retrieve.retrieve_data(db_code.unemployment_basic_education_male)

    #Preprocess and concatenate in one dataset to be used further on

    dataset=pd.concat([

        prep_melt_dataframe(df_advanced_total,'Advanced','Total'),
        prep_melt_dataframe(df_advanced_female,'Advanced','Female'),
        prep_melt_dataframe(df_advanced_male,'Advanced','Male'),
        prep_melt_dataframe(df_intermediate_total,'Intermediate','Total'),
        prep_melt_dataframe(df_intermediate_female,'Intermediate','Female'),
        prep_melt_dataframe(df_intermediate_male,'Intermediate','Male'),
        prep_melt_dataframe(df_basic_total,'Basic','Total'),
        prep_melt_dataframe(df_basic_female,'Basic','Female'),
        prep_melt_dataframe(df_basic_male,'Basic','Male')

    ])
    return dataset.reset_index().drop(columns='index')




