# put the functions here

def clean_columns_titles(df):
    df.columns=df.columns.str.replace(" ","").str.lower().str.strip()
    return df

def drop_null_values(df):
    # Drop the rows with null values  
    df = df.dropna(subset=['date'])
    return df

# In column "year" (into int) -- > Nuria
def format_year(df):
    df[df['year'].isnull()]  # display all rows with null values
    df.loc[797] = df.loc[797].fillna(value=2017)  # Replace NaN in the specified row with value
    df[['year']]=df[['year']].fillna(0).astype(int)
    return df
def filter_year(df):
    # .copy() to create a new DataFrame
    filtered_df=df.copy()
    # filter years before 2010
    filtered_df = filtered_df.loc[filtered_df['year'] > 2009]
    return filtered_df

# In column "date"  -- > Xiaobo
def format_date(filtered_df):
    filtered_df['date']=filtered_df['date'].str.replace(" ","-").str.replace("-","")
    # drop all rows where date contains string "Reported"
    filtered_df = filtered_df[~filtered_df['date'].str.contains("Reported")]
    return filtered_df

# create a new column named "season"
# extract only the months
def create_month(df):
    def extract_month(date):
        # import re
        # Use regex to extract only the letters
        letters_only = re.findall("[a-zA-Z]+", date)
        # Join the extracted letters into a single string
        month = ''.join(letters_only)
        return month
    df['month']=df['date'].apply(extract_month)
    return df

def create_season(df): 
    def check_season(month): 
        q1=['Jan','Feb','Mar']
        q2=['Apr','May','Jun']
        q3=['Jul','Aug','Sep']
        q4=['Oct','Nov','Dec']
        if month in q1:
            season='q1'
        elif month in q2:
            season='q2'
        elif month in q3:
            season='q3'
        elif month in q4:
            season='q4'
        else:
            season="not sure"
        return season 
    df['season']=df['month'].apply(check_season)
    return df

# format column sex
def fix_sex(df):
    df[['sex']]=df[['sex']].fillna("N")
    df['sex']=df['sex'].str.replace(" ","")
    return df

# In column "age" --> Stéphanie
# Define the function to categorize age groups
def set_age_group(x):
    if x == 0:
        return 'Unknown'
    elif x <= 12:
        return 'Child'
    elif x <= 18:
        return 'Teen'
    elif x <= 60:
        return 'Adult'
    elif x > 60:
        return 'Senior'
    else:
        return 'Unknown'
def fix_age(df):
    df['age_0'] = df['age'].apply(lambda x:int(x) if str(x).strip().replace(".","").isdecimal() else 0)
    str(df['age'][0]).strip().replace(".","").isdecimal()
    # df[df['age_0']==0]['age'].value_counts().values.sum()
    #Seulement 132 valeurs "funky" donc NS =>change it to median 
    # Format column age
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    # Calculate the median age
    median_age = df['age'].median()
    print("Median age:", median_age)
    # Replace '0' values with the median age
    df['age_0'] = df['age_0'].replace(0, median_age, inplace=False)
    # Apply the age group function to create the 'agegroup' column
    df['age_group'] = df['age_0'].apply(set_age_group)
    return df

# In column "time" --> Kranta
def set_time_group(x):
    if x <=6:
# == [7,8,9,10,11,12]
        return 'Night'
    elif x <=12:
# ==[13,14,15,16,17,18]
        return 'Morning'
    elif x <= 18:
#  [19,20,21,22,23,00]
        return 'Afternoon'
    elif x <=23 :
# [1,2,3,4,5,6]
        return 'Evening'
    else:
        return "Unknown"
    
def fix_time(df):
    df["time"].value_counts().sort_values(ascending=False)
    df["time"] = df["time"].str.strip()

    df["time"] = df["time"].str.replace('[^a-zA-Z0-9 ]', '', regex=True)

    df['time']= df['time'].fillna("Unknown")

    df["time_split"] = df["time"].str.split('h')

    df["time_split_h"] = df['time_split'].apply(lambda x:x[0])

    df['time_split_h'] = df['time_split_h'].replace('1600',"16")
    df['time_split_h'] = df['time_split_h'].replace('0500',"5")
    df['time_split_h'] = df['time_split_h'].replace('0830',"8")
    df['time_split_h'] = df['time_split_h'].replace('0830',"8")
    df['time_split_h'] = df['time_split_h'].replace('0830',"8")
    df['time_split_h'] = df['time_split_h'].replace('Early Morning',"8")
    df['time_split_h'] = df['time_split_h'].replace('Morning',"8")
    df['time_split_h'] = df['time_split_h'].replace('Afternoon',"14")
    df['time_split_h'] = df['time_split_h'].replace('Late afternoon',"14")
    df['time_split_h'] = df['time_split_h'].replace('Midday',"12")
    df['time_split_h'] = df['time_split_h'].replace('Early afternoon',"14")
    df['time_split_h'] = df['time_split_h'].replace('Sunset',"18")
    df['time_split_h'] = df['time_split_h'].replace('AM',"10")
    df['time_split_h'] = df['time_split_h'].replace('After noon',"14")
    df['time_split_h'] = df['time_split_h'].replace('Sometime between 06h00  08hoo',"06")
    df['time_split_h'] = df['time_split_h'].replace('Shortly before 12h00',"11")
    df['time_split_h'] = df['time_split_h'].replace('Midnight',"01")
    df['time_split_h'] = df['time_split_h'].replace('10j30',"10")
    df['time_split_h'] = df['time_split_h'].replace('Just before noon',"11")
    df['time_split_h'] = df['time_split_h'].replace('10jh45',"11")
    df['time_split_h'] = df['time_split_h'].replace('Just before noon',"11")
    df['time_split_h'] = df['time_split_h'].replace('Early  morning',"11")
    df['time_split_h'] = df['time_split_h'].replace('Dusk',"04")
    df['time_split_h'] = df['time_split_h'].replace('Dawn',"19")
    df['time_split_h'] = df['time_split_h'].replace('Before 10h00',"09")
    df['time_split_h'] = df['time_split_h'].replace('Early morning',"6")
    df['time_split_h'] = df['time_split_h'].replace('Nig',"20")
    df['time_split_h'] = df['time_split_h'].replace('Evening',"17")

    df['time_split_h_int'] = df['time_split_h'].apply(lambda x:int(x) if str(x).isdigit() else 26)
    df

    df['time_group'] = df['time_split_h_int'].apply(set_time_group)
    return df

# In column "country"  -- > Martino
def fix_countries(df):
    #pip install dataprep ##NEED INSTALL
    from dataprep.clean import clean_country
    df_cleaned = clean_country(df,"Country") ##it add a new column called "Country_clean" is has some Nan values that we will drop
    df_cleaned = df_cleaned.dropna(subset=["Country_clean"]) # we drop the NAN
    df_cleaned["Country_clean"] = df_cleaned["Country_clean"].str.lower() #Set the elements to lower case
    ##The list coountries I found online and I use it to match what we have in the Country_clean column
    ##after some playing around the lists match except for one value netherlands antilles
    countries = ['afghanistan', 'aland islands', 'albania', 'algeria', 'american samoa', 'andorra', 'angola', 'anguilla', 'antarctica', 'antigua and barbuda', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bermuda', 'bhutan', 'bolivia (plurinational state of)', 'bonaire, sint eustatius and saba', 'bosnia and herzegovina', 'botswana', 'bouvet island', 'brazil', 'british indian ocean territory (the)', 'brunei darussalam', 'bulgaria', 'burkina faso', 'burundi', 'cabo verde', 'cambodia', 'cameroon', 'canada', 'cayman islands', 'central african republic (the)', 'chad', 'chile', 'china', 'christmas island', 'cocos (keeling) islands (the)', 'colombia', 'comoros', 'congo (the democratic republic of the)', 'congo (the)', 'cook islands', 'costa rica', "cote d'ivoire", 'croatia', 'cuba', 'curacao', 'cyprus', 'czechia', 'denmark', 'djibouti', 'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'ethiopia', 'falkland islands', 'faroe islands (the)', 'fiji', 'finland', 'france', 'french guiana', 'french polynesia', 'french southern territories (the)', 'gabon', 'gambia (the)', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'grenada', 'guadeloupe', 'guam', 'guatemala', 'guernsey', 'guinea', 'guinea-bissau', 'guyana', 'haiti', 'heard island and mcdonald islands', 'holy see (the)', 'honduras', 'hong kong', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'isle of man', 'israel', 'italy', 'jamaica', 'japan', 'jersey', 'jordan', 'kazakhstan', 'kenya', 'kiribati', "korea (the democratic people's republic of)", 'south korea', 'kuwait', 'kyrgyzstan', "lao people's democratic republic (the)", 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'macao', 'macedonia (the former yugoslav republic of)', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'martinique', 'mauritania', 'mauritius', 'mayotte', 'mexico', 'micronesia, fed. sts.', 'moldova (the republic of)', 'monaco', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique', 'myanmar', 'namibia', 'nauru', 'nepal', 'netherlands (the)', 'new caledonia', 'new zealand', 'nicaragua', 'niger (the)', 'nigeria', 'niue', 'norfolk island', 'northern mariana islands', 'norway', 'oman', 'pakistan', 'palau', 'palestine, state of', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'pitcairn', 'poland', 'portugal', 'puerto rico', 'qatar', 'reunion', 'romania', 'russia', 'rwanda', 'saint barthelemy', 'palestine', 'st. helena', 'ascension and tristan da cunha', 'st. kitts and nevis', 'saint lucia', 'saint-martin', 'saint pierre and miquelon', 'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'sint maarten (dutch part)', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south georgia and the south sandwich islands', 'south sudan', 'spain', 'sri lanka', 'sudan', 'suriname', 'svalbard and jan mayen', 'swaziland', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'tokelau', 'tonga', 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'turks and caicos islands', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states minor outlying islands (the)', 'united states', 'uruguay', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam', 'british virgin islands', 'virgin islands (u.s.)', 'wallis and futuna', 'western sahara*', 'yemen', 'zambia', 'zimbabwe']
    not_country = []
    for element in df_cleaned["Country_clean"]:
        if element not in countries:
            if element not in not_country:
                not_country.append(element)
    print(not_country)
    df_cleaned = df_cleaned.dropna(subset=["Country_clean"])
    df_cleaned["Country_clean"].nunique()
    #there are still 225 unique values in the column
    return df_cleaned


# def main():
#     # This code will only run if the script is executed directly
#     # import pandas as pd
#     # import numpy as np
#     # import re
#     # Download the dataset and import it into Python
#     import xlrd
#     import pandas as pd
#     import numpy as np
#     import re

#     # pd.set_option('display.max_rows', None)
#     shark_attacks_df = pd.read_excel('GSAF5.xls')
#     # shark_attacks_df.rename(columns='Species':'species')
#     country_df = pd.read_excel('country_clean.xls')
#     df=pd.concat([shark_attacks_df, country_df], axis=1)
#     # Cleaning DataFrame
#     #Chose the columns we will be working with
#     df = df[['Date', 'Year', 'Type', 'Country', 'State', 'Location','Activity','Sex', 'Age', 'Injury','Time','Species ','Country_clean']] 
#     # clean columns titles --> remove spaces & lower cases
#     df=clean_columns_titles(df)
#     # drop the null value rows
#     df=drop_null_values(df)
#     # format column year
#     df=format_year(df)
#     # filtered df
#     filtered_df=filter_year(df)
#     filtered_df=format_date(filtered_df)
#     filtered_df=create_month(filtered_df)
#     filtered_df=create_season(filtered_df)
#     filtered_df=fix_sex(filtered_df)
#     filtered_df=fix_age(filtered_df)
#     df=fix_time(filtered_df)

#     return df

# if __name__ == "__main__":
#     result_df = main()
#     print(result_df)