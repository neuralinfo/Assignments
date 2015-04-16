
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

## What to Turn In ##

You must turn in a pull request containing the following:

 1. A copy of the output directory for the tag counter running locally (name the directory 'out').
 2. A copy of the output from S3 for the tag counter running on AWS (name the directory 'emr-out').
 3. How long did it take to run the process for each of these?
 4. How many `address` tags are there in the input?
 5. Does the local version and EMR version give the same answer?
 
Please submit the answers to 3-5 in a text file called `answers.txt`


