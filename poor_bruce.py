# put the functions here

def clean_columns_titles(df):
    df.columns=df.columns.str.replace(" ","").str.lower().str.strip()
    return df

def drop_null_values(df):
    # Drop the rows with null values  
    df = df.dropna(subset=['date'])
    return df

# format column year (into int)
def format_year(df):
    df[df['year'].isnull()]  # display all rows with null values
    df.loc[797] = df.loc[797].fillna(value=2017)  # Replace NaN in the specified row with value
    df[['year']]=df[['year']].fillna(0).astype(int)
    return df

# filter_df
def filter_year(df):
    # .copy() to create a new DataFrame
    filtered_df=df.copy()
    # filter years before 2010
    filtered_df = filtered_df.loc[filtered_df['year'] > 2009]
    return filtered_df

# format column date
def format_date(filtered_df):
    filtered_df['date']=filtered_df['date'].str.replace(" ","-").str.replace("-","")
    # drop all rows where date contains string "Reported"
    filtered_df = filtered_df[~filtered_df['date'].str.contains("Reported")]
    return filtered_df


# in columns country ---Martino

# in columns year & date -->season Xiaobo


#filter all years before 2010  -->Nuria
# #Use strip to remove the uncentered data (observations 325,324,84 are uncentered, leaving a blank space)
# year_filtered_df = df.loc[df['year'] > '2009'].strip()
# #drop the observation 799, blank space
# year_filtered_df = year_filtered_df.drop(index[799])


# filter time and group them to  ---> Kranta
# -Morning 6-12
# -Afternoon 12-18
# -Evening 18-24
# -Night 24-6



# filter the age by group and replace --->Stéphanie

# main function

# fill na in column age with mean 
# filter age and group them to 
# -Child 0-12
# -Teen 13-18
# -Adult 19-70
# -Senior 71-100+++



# specie [MAYBE]


# def main():
#     print("Main function")
#     function1()
#     function2()

# if __name__ == "__main__":
#     main()