from math import pi
from datetime import datetime
import re

width = float(input('Enter tire width (ie 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ie 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ie 15): '))

volume = (pi * width ** 2 * ratio * (width * ratio + 2540 * diameter))/10000000

print(f'The approximate volume is {volume:,.1f} cubic centimeters.')
tires_offer = input('Would you like us to contact you with an offer to buy these tires? Enter "yes" or "no".')
if tires_offer.lower() == 'yes':
    phone_number = ""
    while len(phone_number) != 10:
        phone_number = re.sub('-|(|)| ',"",input("Awesome. What's the best phone number to reach you at?"))
        if len(phone_number) != 10:
            print("Please enter your 10-digit phone number (this includes your area code).")

today = datetime.now()
today_clean = str(today.year) + "-" + str(today.month) + "-" + str(today.day)

with open('volumes.txt', mode="at") as volume_text:
    if tires_offer.lower() == 'yes':
        print(f'CUSTOMER WANTS TO BUY TIRES', file=volume_text)
    print(f"Today's date: {today_clean}", file=volume_text)
    print(f'Tire Width: {width:.0f}', file=volume_text)
    print(f'Aspect ratio: {ratio:.0f}', file=volume_text)
    print(f'Diameter: {diameter:.0f}', file=volume_text)
    print(f'Volume: {volume:.1f}', file=volume_text)
    if tires_offer.lower() == 'yes':
        print(f'Customer phone number: {phone_number}', file=volume_text)
    print('------------------------------------', file=volume_text)

import pandas as pd
import dask.dataframe as dd
import sqlalchemy as sa
from sqlalchemy import create_engine, Table, MetaData
import warnings

def dataframe_to_sql(self, eng, schema, table_name, if_exists='fail', chunksize=10000):
    """
    This function converts a Pandas or Dask DataFrame to a SQL table and inserts the data.

    :param self: The DataFrame (Pandas or Dask) to insert into the table
    :param eng: The SQLAlchemy engine to connect to the database
    :param schema: The schema for the table
    :param table_name: The name of the table
    :param if_exists: What to do if the table exists. Options: 'fail', 'replace', 'append'. Default: 'fail'.
    :param chunksize: The number of rows to process at once for Dask DataFrames. Default: 10000.
    """

    # Determine if the input is a Dask DataFrame
    is_dask_dataframe = isinstance(self, dd.DataFrame)

    # Warn the user if there are null values and indicate the columns containing null values
    null_columns = [col for col in self.columns if (self[col].isnull().any().compute() if is_dask_dataframe else self[col].isnull().any())]
    if null_columns:
        warnings.warn(f"The DataFrame contains null values in the following columns: {', '.join(null_columns)}")

    # Create a table based on the DataFrame schema
    dtypes = self.dtypes.compute() if is_dask_dataframe else self.dtypes
    meta = MetaData(schema=schema)
    table = Table(table_name, meta, *(sa.Column(col_name, sa.types.to_sqla_type(col_type), nullable=True) for col_name, col_type in dtypes.items()))

    # Create a connection to the database
    with eng.connect() as conn:
        # Check if the table exists and follow the specified behavior
        if conn.dialect.has_table(conn, table_name, schema=schema):
            if if_exists == 'fail':
                raise ValueError(f"Table '{table_name}' already exists.")
            elif if_exists == 'replace':
                table.drop(conn)
                table.create(conn)
            elif if_exists == 'append':
                pass
            else:
                raise ValueError("Invalid value for 'if_exists'. Options are 'fail', 'replace', or 'append'.")
        else:
            table.create(conn)

        # Insert the DataFrame data into the table
        if is_dask_dataframe:
            self.to_sql(table_name, conn, schema=schema, if_exists=if_exists, chunksize=chunksize)
        else:
            data = [dict(row) for _, row in self.iterrows()]
            conn.execute(table.insert(), data)

pd.DataFrame.to_sql_extended = dataframe_to_sql
dd.DataFrame.to_sql_extended = dataframe_to_sql
