import boto3
import datetime
import os.path
import sys

#We will store the current timestamp for later use
#We will also specify the bucket and source directory
#We will also creat a device id variable

now = datetime.datetime.now()
bucketname = 'serveractivityuploads'
sourceDir = 
deviceid = 'ipn2%s' % now

#We will make a list of the file names to be uploaded
uploadFileNames = []
for (sourceDir, dirname, filename) in os.walk(sourceDir):
    uploadFileNames.extend(filename)
    break

#For loop goes through each file and uploads it to s3
for filename in uploadFileNames:
    sourcepath = os.path.join(sourceDir + '/' + filename) 
    logname = deviceid + '_' + filename   
    s3 = boto3.resource('s3',)
    s3.Bucket(bucketname).upload_file(sourcepath, logname)
