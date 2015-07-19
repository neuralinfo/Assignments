
# coding: utf-8

# In[ ]:

get_ipython().system(u'aws configure')


# In[ ]:

get_ipython().system(u'aws --version')


# In[ ]:

get_ipython().system(u'aws help')


# In[ ]:

get_ipython().system(u'aws s3 ls')


# In[ ]:

get_ipython().system(u'aws s3 mb s3://mybuck-w205-2014')


# In[ ]:

get_ipython().system(u'aws s3 cp s3://emr-w205-outputs s3://mybuck-w205-2014 --recursive')


# In[ ]:

get_ipython().system(u'aws s3 ls s3://mybuck-w205-2014')


# In[ ]:

get_ipython().system(u'pysay "Aws CLI is Awesome"')


# In[ ]:



