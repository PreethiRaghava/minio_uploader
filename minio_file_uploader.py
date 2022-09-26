#/usr/bin/python3

from minio import Minio
import io 
import urllib3

httpClient = urllib3.PoolManager(
                cert_reqs='CERT_REQUIRED',
                ca_certs='public.crt')

ACCESS_KEY = "izar5WoFmW5fKaKm"
SECRET_KEY = "BRGjZhbNZoEoaCJEqasd4gYzoNBE7rAj"
MINIO_API_HOST = "10.8.0.31:9000"

LOCAL_FILE_PATH = 'path of the file with file name'
image_path = 'name of the file'

client = Minio(
       MINIO_API_HOST,
       access_key=ACCESS_KEY,
       secret_key=SECRET_KEY,
       secure=True,
       http_client=httpClient
)
if client.bucket_exists("health"):
    print("health bucket exists")
else:
       print("health bucket does not exist")
client.fput_object("health", image_path, LOCAL_FILE_PATH)
print("It is successfully uploaded to bucket")