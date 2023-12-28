from sklearn.model_selection import train_test_split
import pandas as pd
import env as e
import os



# acquire zillow dataset
def get_zillow():
    '''
    Acquire zillow dataset from codeup database
    returns zillow data frame with yearbuilt, bedroomcnt, bathroomcnt, 
    calculatedfinishedsquarefeet, taxvaluedollarcnt, taxamount, fips. 
    '''
    # name of cached csv
    filename = "zillow.csv"
    # if cached data exist
    if os.path.isfile(filename):
        # read the file
        df = pd.read_csv(filename)
    # else, pull from sql db if not cached
    else:
        df = pd.read_sql(
            """SELECT yearbuilt,
                       bedroomcnt,
                       bathroomcnt,
                       calculatedfinishedsquarefeet,
                       taxvaluedollarcnt,
                       taxamount,
                       fips
                FROM properties_2017
                WHERE propertylandusetypeid = 261""",
            f"mysql+pymysql://{e.user}:{e.password}@{e.host}/zillow",)
        # cache the pulled data locally
        df.to_csv(filename, index=False)
    return df






# acquire and prep function for zillow dataset
def wrangle_zillow():
    """
    This function reads the Zillow data from a cached CSV file if it exists,
    or from a SQL database if it doesn't exist. It then renames the columns
    to more descriptive names.

    Args:
    - None

    Returns:
    - pandas dataframe
    """
    # Name of cached CSV file
    filename = "zillow.csv"
    # If cached data exists, read from CSV file
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    # Otherwise, read from SQL database
    else:
        df = pd.read_sql(
            """SELECT yearbuilt,
                                   bedroomcnt,
                                   bathroomcnt,
                                   calculatedfinishedsquarefeet,
                                   taxvaluedollarcnt,
                                   taxamount,
                                   fips
                            FROM properties_2017
                            WHERE propertylandusetypeid = 261""",  # 261 is single family residential id
            f"mysql+pymysql://{e.user}:{e.password}@{e.host}/zillow",
        )
        # Cache data locally
        df.to_csv(filename, index=False)
    # Rename columns
    df = df.rename(
        columns={
            "yearbuilt": "year",
            "bedroomcnt": "bedrooms",
            "bathroomcnt": "bathrooms",
            "calculatedfinishedsquarefeet": "square_feet",
            "taxvaluedollarcnt": "property_value",
            "taxamount": "property_tax",
            "fips": "county",
        }
    )

    # Drop rows with missing values in specific columns 
    df = df.dropna()

    # Map county codes to county names
    df.county = df.county.map({6037: "LA", 6059: "Orange", 6111: "Ventura"})

    # Convert columns to int data type
    df = df.astype({"year": int, "bedrooms": int, "square_feet": int, "property_value": int})

    return df








# Split data function
def split_data(df):
    """
    This function takes in any DataFrame and a target variable as an argument 
    and returns train, validate, and test dataframes.
    It returns three DataFrames with a printout of their proportion to the original DataFrame.
    """
    train, validate_test = train_test_split(df, train_size=0.6, random_state=123)
    validate, test = train_test_split(validate_test, train_size=0.5, random_state=123)
    print(f"train: {len(train)} ({round(len(train)/len(df), 2)*100}% of {len(df)})")
    print(
        f"validate: {len(validate)} ({round(len(validate)/len(df), 2)*100}% of {len(df)})"
    )
    print(f"test: {len(test)} ({round(len(test)/len(df), 2)*100}% of {len(df)})")

    return train, validate, test





