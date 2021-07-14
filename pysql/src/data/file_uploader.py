import requests
from google.cloud import storage
import os
from queries import create_tables
from queries import insert_data

def authenticate():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\NikoNiinimäki\keys\python-hc-319107-d532fbbadd37.json"


def make_file():

    response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
    dataframe = response.json()
    items_data = dataframe["items"]

    with open("checkpoint.txt", "a+") as file_object:

        for i in items_data:
            file_object.seek(0)
            data = file_object.read(100)

            if len(data) > 0 :
                file_object.write("\n")

            file_object.write(f"{i['parameter']}")


def create_bucket(bucket_name):

    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print("Bucket {} created.".format(bucket.name))


def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

    return (bucket_name, source_file_name, destination_blob_name)

authenticate()
make_file()
create_tables()
create_bucket("postregtutorialism")
imginfo = upload_blob("postregtutorialism", "image.jpg", "image.jpg")
insert_data("picturedata"), picname, storagename, picurl, users)

picname = f"imginfo[2]"