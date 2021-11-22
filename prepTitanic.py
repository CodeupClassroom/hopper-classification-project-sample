from pandas import DataFrame
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def clean_titanic(df):
    '''
    This function takes in dataframe as argument, 
    create dummy variables out of sex and embarked, and concats those to original dataframe
    drops columns embarked, sex, deck, class
    drops rows where age (177 rows) or embarked_town (2 rows) are null. 
    it returns the new cleaned dataframe.
    '''
    dummies_df = pd.get_dummies(df[['sex', 'embarked']], drop_first=True)
    df_with_dummies = pd.concat([df, dummies_df], axis=1)
    df_dropped_cols_with_dummies = df_with_dummies.drop(columns=['embarked', 'sex', 'deck', 'class'])
    df_cleaned = df_dropped_cols_with_dummies[df_dropped_cols_with_dummies.age.notnull()]
    return df_cleaned


def train_validate_test_split(prepped_df, seed=123):
    '''
    This function takes in a cleaned dataframe and a random seed, 
    and splits the dataframe into 3 samples, a train, validate and test sample, 
    The test is 20% of the data, the validate is 24% of the data, and the train is 56% of the data. 
    The function returns 3 dataframes in the order of: train, validate and test. 
    '''
    train_and_validate, test = train_test_split(
        prepped_df, test_size=0.2, random_state=seed, stratify=prepped_df.survived
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.survived,
    )
    return train, validate, test

def clean_split_titanic_data(df):
    '''
    this function runs both the clean_titanic and train_validate_test_split functions, initially taking in the orginal
    acquired dataframe as an argument and returning the 3 samples in order: train, validate, test. 
    '''
    cleaned_df = clean_titanic(df)
    train, validate, test = train_validate_test_split(cleaned_df, seed=123)
    return train, validate, test