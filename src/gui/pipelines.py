import pandas as pd


# filters dataframe for unemployment rate data relative to the continent, education level and target population provided as arguments

def continents_pipeline_trend (df, continent, education , population):

    pipeline = (

        df[
            (df.Continent == continent) &
            (df.Education == education) &
            (df.Population == population)

        ].groupby(['year'])['unemployment_rate'].mean()
        .reset_index()

    )
    return pipeline

# filters dataframe for unemployment rate data relative to the country, education level and target population provided as arguments

def countries_pipeline_trend(df, country, education, population):

    pipeline = (

        df[
            (df.Country == country) &
            (df.Education == education) &
            (df.Population == population)

        ].reset_index()

    )
    return pipeline


# provides unemployment rate data relative to the continent and education level provided as arguments

def country_unemployment_by_education(df,country,education):

    data=pd.DataFrame()

    data['year'] = range(2008,2023)

    data['Female']=countries_pipeline_trend(df,country,education,'Female')['unemployment_rate']

    data['Male'] = countries_pipeline_trend(df, country, education, 'Male')['unemployment_rate']

    data['Total'] = countries_pipeline_trend(df, country, education, 'Total')['unemployment_rate']

    return data


# provides unemployment rate data relative to the country and education level provided as arguments

def continent_unemployment_by_education(df,continent,education):

    data=pd.DataFrame()

    data['year'] = range(2008,2023)

    data['Female']=continents_pipeline_trend(df,continent,education,'Female')['unemployment_rate']

    data['Male'] = continents_pipeline_trend(df, continent, education, 'Male')['unemployment_rate']

    data['Total'] = continents_pipeline_trend(df, continent, education, 'Total')['unemployment_rate']

    return data


