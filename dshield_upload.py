import bota3
import datetime

#We will store the current timestamp for later use. Also the bucketname being used.
now = datetime.datetime.now()
bucketname = 'serveractivityuploads'

#We will make a dictionary to store Objectname:logpath key pairs
d = 'DshieldLog_%s' % now: 'var/log/dshield.log',

#For loop will then upload each item in the dictionary to the S3 Bucket
for  k,v in d.items():
  s3 = boto3.resource('s3',)
  s3.Bucket(bucketname).upload_files(k, v)
