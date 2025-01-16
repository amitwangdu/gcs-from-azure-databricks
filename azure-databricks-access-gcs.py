
## how to access the gcs bucket in google clude  from tne azure databricks
#steps-1
pip install google-cloud-storage

#step-2 
copy the jason file to the local directory 
here its /Workspace/Users/samit.rkl@gmail.com/Databricks-Certified-Data-Engineer-Associate/1- Databricks Lakehouse Platform/<jsonfile>.json

#step-3

from google.cloud import storage
from google.oauth2 import service_account

# Specify the path to the service account JSON key
#gcs_key_path = "/dbfs/mnt/keys/skyeyez.json"  # DBFS path to the key
gcs_key_path = "/Workspace/Users/samit.rkl@gmail.com/Databricks-Certified-Data-Engineer-Associate/1- Databricks Lakehouse Platform/<jsonfile>.json" 

# Authenticate using the service account key
credentials = service_account.Credentials.from_service_account_file(gcs_key_path)

# Create a GCS client with the provided credentials
client = storage.Client(credentials=credentials, project='skyeyez-ai-solution')

# List buckets to verify the connection
buckets = list(client.list_buckets())
print(buckets)
