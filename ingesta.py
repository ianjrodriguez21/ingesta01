import boto3

ficheroUpload = "data.csv"
nombreBucket = "gcr-output-01-ijr"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
print(response)

print("Ingesta completada")
