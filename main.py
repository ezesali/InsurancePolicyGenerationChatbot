import boto3


s3 = boto3.Session(
    aws_access_key_id='AKIA2JHUK4EGBAMYAYFY',
    aws_secret_access_key='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'
)

bucket_name = 'anyoneai-datasets'
prefix = 'queplan_insurance/'

s3_client = s3.client('s3')
s3_client.download_file(bucket_name, prefix + 'POL320200071.pdf', 'POL320200071.pdf')

s3_client.download_file(bucket_name, prefix + 'POL320150503.pdf', 'POL320150503.pdf')

s3_client.download_file(bucket_name, prefix + 'POL320130223.pdf', 'POL320130223.pdf')




#POL320130223.pdf

#POL320150503.pdf

#POL320200071.pdf