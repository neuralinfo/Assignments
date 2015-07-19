import pandas as pd
import urllib
import csv
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection('YOUR ACCESS KEY', 'YOUR SECRET KEY')
bucket = conn.create_bucket('sub-datasets-YOUR-BUCKET-NAME')

urllib.urlretrieve("http://www.exploredata.net/ftp/WHO.csv","WHO.csv")

df = pd.read_csv("WHO.csv")

df.head()

tenforty = df[(df.CountryID >= 10) & (df.CountryID <= 40)]

tenforty.head()

tenforty.to_csv('10-40.csv',index=True,header=True)

myKey = Key(bucket)
myKey.key = '10-40.csv'
myKey.set_contents_from_filename('10-40.csv')