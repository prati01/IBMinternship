import ibm_boto3
from ibm_botocore.client import Config
import cgi
form = cgi.FieldStorage()
classname =  form.getvalue('classname')
uploadedfile = form.getvalue('uploaded_file')

api_key = '5fCIJmZL3zt2FOsUdQQQUhUTc-L4X2uzIFhwb4dVY7Yo'
service_instance_id = 'crn:v1:bluemix:public:cloud-object-storage:global:a/61c86e4ba3d34ff19c5d45b1d4d5c6a6:7ea63fd2-4bc5-47af-a9be-415362f996d9::'
auth_endpoint = 'https://iam.bluemix.net/oidc/token'
service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'
##
##new_bucket = 'fooditems32'
##new_cold_bucket = 'NewColdBucket'

cos = ibm_boto3.resource('s3',
                      ibm_api_key_id=api_key,
                      ibm_service_instance_id=service_instance_id,
                      ibm_auth_endpoint=auth_endpoint,
                      config=Config(signature_version='oauth'),
                      endpoint_url=service_endpoint)

##cos.create_bucket(Bucket=new_bucket)

##cos.create_bucket(Bucket=new_cold_bucket,
##                    CreateBucketConfiguration={
##                        'LocationConstraint': 'us-cold'
##                    },
##)

##for bucket in cos.buckets.all():
##        print(bucket.name)

cos.meta.client.upload_file(uploadedfile , 'fooditems32' , classname)
