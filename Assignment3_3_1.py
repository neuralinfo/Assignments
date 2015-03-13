#!/usr/bin/env python
#
# David Paculdo
# W205
# Assignment 3

from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os
import sys
import string

#Accessibility to Amazon AWS
AWS_KEY=os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET=os.environ.get("AWS_SECRET_KEY")
host="s3-us-west-2.amazonaws.com"

#Location of mongo databases
localdir="/usr/local/var/mongodb/"


#Function to save mongo db to S3
def save_db_to_s3(filename):
	k = Key(bucket)
	
	nsfile=localdir+filename+".ns"
	filepath=localdir+filename+"."
	filecount=0
	
	#Checks for existence of database
	if os.path.isfile(nsfile):
		while os.path.isfile(filepath+str(filecount)):
			filep=filepath+str(filecount)
			k.key=filename+"."+str(filecount)
			#print filep
			k.set_contents_from_filename(filep)
			filecount+=1

		k.key=filename+".ns"
		k.set_contents_from_filename(nsfile)
	else:
		print "database "+filename+" does not exist!"


#Function to retrieve backup mongo db from S3
def get_db_from_s3(filename):
	k = Key(bucket)
	nsfile=filename+".ns"
	filepath=localdir+filename+"."
	k.key=nsfile
	
	#Checks for existence of backup
	if k.exists():
		filecount=0
		k.get_contents_to_filename(localdir+nsfile)
		k.key=filename+"."+str(filecount)
		
		while k.exists():
			k.get_contents_to_filename(filepath+str(filecount))
			filecount+=1
			k.key=filename+"."+str(filecount)
	else:
		print "backup of " + filename + " does not exist!" 



#Function to list mongo backups in S3
def list_backup_in_s3():
	for i, key in enumerate(bucket.get_all_keys()):
		print "[%s] %s" % (i, key.name)


#Function to delete backup in S3
def delete_backup(filename):
	k=Key(bucket)
	k.key=filename+".ns"
	
	#checks for existence of backup to delete
	if k.exists():
		k.delete()
		filecount=0
		k.key=filename+"."+str(filecount)
		
		while k.exists():
			k.delete()
			filecount+=1
			k.key=filename+"."+str(filecount)
		
	else:
		print "backup of " + filename + " does not exist!" 

	for i, key in enumerate(bucket.get_all_keys()):
		print "deleting %s" % (key.name)
		key.delete()


if __name__ == '__main__':
	conn = S3Connection(AWS_KEY, AWS_SECRET)
	
	#Bucket for saving the backups. Make sure the bucket exists.
	bucket = conn.get_bucket("w205-assignment-3-dpaculdo")

	if len(sys.argv) < 3 and string.lower(sys.argv[1])!="list":
		print 'Usage: %s [backup/restore/list/delete] [database_name (optional for list)]' % (sys.argv[0])
	else:
		if string.lower(sys.argv[1]) == 'backup':
			save_db_to_s3(sys.argv[2])
		elif string.lower(sys.argv[1]) == 'restore':
			get_db_from_s3(sys.argv[2])
		elif string.lower(sys.argv[1]) == 'list':
			list_backup_in_s3()
		elif string.lower(sys.argv[1]) == 'delete':
			delete_backup(sys.argv[2])
		else:
			print 'Usage: %s <get/set/list/delete> <backup_filename>' % (sys.argv[0])
