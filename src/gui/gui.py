import pandas as pd
import src.config.config as config
import src.config.db_codes as db_code
import src.data_retrieval.data_retrieval as retrieve
import src.data_preprocessing.preprocessing as prep
import src.gui.pipelines as pipline
import panel as pn
pn.extension('tabulator',sizing_mode='stretch_width')
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')
from bokeh.plotting import show




# retrieve and preprocess data - may take time until the data is loaded and preprocessed 

df=prep.prep_dataset()



# create widgets

select_continent = pn.widgets.Select(name='',options=df['Continent'].unique().tolist())

select_country = pn.widgets.Select(name='',options=df[df['Continent'] == select_continent.value]['Country'].unique().tolist())

select_educ_level_continent = pn.widgets.RadioButtonGroup(

    name = 'Education level',
    options = ['Advanced','Intermediate','Basic'],
    button_type='success'
)

select_educ_level_country = pn.widgets.RadioButtonGroup(

    name = 'Education level',
    options = ['Advanced','Intermediate','Basic'],
    button_type='success'
)



# Update the country's widget options when a new continent is selected

@pn.depends(select_continent.param.value, watch=True)
def _update_countries(slct_continent):
    countries = df[df['Continent'] == slct_continent]['Country'].unique().tolist()
    select_country.options = countries


# Combine pipelines and widgets

@pn.depends(select_continent.param.value, select_educ_level_continent.param.value, watch=True)
def continent_unemployment_plt(select_continent, select_educ_level ):
    data=pipline.continent_unemployment_by_education(df,select_continent,select_educ_level)
    return data.hvplot(x='year', y=['Female', 'Male', 'Total'], title='Unemployment rate in selected Continent (2008 - 2022)')

@pn.depends(select_country.param.value, select_educ_level_country.param.value, watch=True)
def country_unemployment_plt(select_country, select_educ_level ):
    data=pipline.country_unemployment_by_education(df,select_country,select_educ_level)
    return data.hvplot(x='year', y=['Female', 'Male', 'Total'], title='Unemployment rate in selected Country (2008 - 2022)')


# Arrange widgets and plots in a template

template=pn.template.FastListTemplate(

    title=' World bank unemployment data - interactive dashboard ',
    sidebar=['Select Continent/Education level : ', select_continent,select_educ_level_continent,'Select Country/Education level : ',
             select_country,select_educ_level_country],
    main=[continent_unemployment_plt,country_unemployment_plt],
    accent_base_color="#88d8b0",
    header_background="#88d8b0",

)

template.show()

