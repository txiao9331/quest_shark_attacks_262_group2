# put the functions here

def clean_columns_titles(df):
    df.columns=df.columns.str.replace(" ","").str.lower().str.strip()
    return df

def drop_null_values(df):
    # Drop the rows with null values  
    df = df.dropna(subset=['date'])
    return df

# format date, year (into int), and time column 

# in columns country ---Martino

# in columns year & date -->season Xiaobo


# filter the years after 2010 -->Nuria



# filter time and group them to  ---> Kranta
# -Morning 6-12
# -Afternoon 12-18
# -Evening 18-24
# -Night 24-6



# filter the age by group and replace --->??

# main function

# fill na in column age with mean 
# filter age and group them to 
# -Child 0-12
# -Teen 13-18
# -Adult 19-70
# -Senior 71-100+++



# specie [MAYBE]