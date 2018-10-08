import bota3
import datetime

now = datetime.datetime.now()
objectname = 'DshieldLog_%s' % now
logpath = 'var/log/dshield.log'
bucketname = 'serveractivityuploads'

s3 = boto3.resource('s3',)
s3.Bucket(bucketname).upload_files(logpath, objectname)
