
# Getting Started #

This assignment will step you through the process of running a simple computation over a data set using Map/Reduce via mrjob.  The goal 
of the assignment is to have you walk through the process of using, github, python, mrjob, and AWS and ensure you are setup with
all the various tools and services.

## Recommended Readings ##

 * [Getting started with Amazon AWS video tutorials](http://aws.amazon.com/getting-started/)
 * [Introduction to AWS training](https://www.youtube.com/playlist?list=PLhr1KZpdzukcMmx04RbtWuQ0yYOp1vQi4)
 * [A Comparison of Clouds: Amazon Web Services, Windows Azure, Google Cloud Platform, VMWare and Others](http://pages.cs.wisc.edu/~akella/CS838/F12/notes/Cloud_Providers_Comparison.pdf)
 * [A Survey on Cloud Provider Security Measures](http://www.cs.ucsb.edu/~koc/ns/projects/12Reports/PucherDimopoulos.pdf)

## Tasks ##
Note: Keep track of the time necessary to run the process.  For Linux/Mac users, you can use the `time` command to compute this.

### Part 1 ###



 1. Follow the instructions for running the program [locally]( https://github.com/commoncrawl/cc-mrjob#running-locally) and measure the completion time.

### Part 2 ###

 1. Follow the process for running the program on on on [Amazon Elastic MapReduce]( https://github.com/commoncrawl/cc-mrjob#running-via-elastic-mapreduce) and measure the completion time.
 2. Download the output from S3.

# Setup for running on AWS EMR #

## AWS Setup ##
You can create users instead of using your root aws credentials
If you do not have a user/group with access to EMR, you'll need to do the following procedure.

First, you need to setup a user to run EMR:

 1. Visit http://aws.amazon.com/ and sign up for an account.
 2. Select the "Identity and Access Management" (or IAM) from your console or visit https://console.aws.amazon.com/iam/home
 3. Select "Users" from the list on the left.
 3. Click on the "Create New Users"
 4. Enter a user name for yourself and create the user.
 5. The next screen will give you an option to download the credentials for this user.  Do so and store them in a safe place.  You will not be able to retrieve them again.

Second, you need to create a group with the right roles:

 1. Select "Groups" from the list on the left.
 2. Click on "Create New Group".
 3. Enter a name and click on "Next Step".
 4. Scroll down to "Amazon Elastic MapReduce Full Access" click on "Select".
 5. Once the policy document is displayed, click on "Next Step".
 6. Click on "Create Group" to create the group.
 
Third, you need to assign your user to the group:

 1. Select the check box next to your group.
 2. Click on the "Group Actions" drop-down menu and click on "Add Users to Group".
 3. Select your user by clicking on the check box.
 4. Click on "Add Users".

## Configure mrjob with the new user credentials##

You need to configure mrjob to access your AWS account:

   1. Edit the mrjob.conf
   2. Locate the `#aws_access_key_id:` and `#aws_secret_access_key:` lines.
   3. Remove the hash (#) and add your AWS key and secret after the colon (:).  You should have these from previously creating the user.
   
## Setup an Output Bucket on S3 ##

You need to create an output bucket on S3 for the results of your computation:

   1. Go to https://aws.amazon.com/ in your browser.
   2. Click on the 'S3' service link.
   3. Click on the 'Create Bucket' button.
   4. Enter a name and hit create.
   
Keep in mind that the bucket name is unique to all of Amazon.  If you use some common name, it is likely to clash with other 
users.  One suggestion is to use a common prefix (e.g. a domain name) for all your bucket names.




## What to Turn In ##

You must turn in a pull request containing the following:

 1. A copy of the output directory for the tag counter running locally (name the directory 'out').
 2. A copy of the output from S3 for the tag counter running on AWS (name the directory 'emr-out').
 3. How long did it take to run the process for each of these?
 4. How many `address` tags are there in the input?
 5. Does the local version and EMR version give the same answer?
 
Please submit the answers to 3-5 in a text file called `answers.txt`


