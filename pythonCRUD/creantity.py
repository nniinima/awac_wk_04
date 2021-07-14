from google.cloud import datastore

# For help authenticating your client, visit
# https://cloud.google.com/docs/authentication/getting-started
client = datastore.Client()

with client.transaction():
    incomplete_key = client.key("taulu")

    task = datastore.Entity(key=incomplete_key)

    task.update(
        {
            "name": "Unknown",
            "species": "unknown",
            "job": "unknown",
            "color": "unknown",
        }
    )

    client.put(task)