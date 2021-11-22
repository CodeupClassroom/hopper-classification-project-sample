from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def handle_missing_values(df):
    return df.assign(
        embark_town=df.embark_town.fillna('Other'),
        embarked=df.embarked.fillna('O'),
    )

def remove_columns(df):
    return df.drop(columns=['deck', 'age'])

def encode_embarked(df):
    encoder = LabelEncoder()
    encoder.fit(df.embarked)
    return df.assign(embarked_encode = encoder.transform(df.embarked))

def prep_titanic_data(df):
    prepped_df = df\
        .pipe(handle_missing_values)\
        .pipe(remove_columns)\
        .pipe(encode_embarked)
    return prepped_df

def train_validate_test_split(prepped_df, seed=123):
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

def prep_split_titanic_data(df):
    prepped_df = prep_titanic_data(df)
    train, validate, test = train_validate_test_split(prepped_df)
    return train, validate, test