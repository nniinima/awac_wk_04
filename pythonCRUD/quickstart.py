def run_quickstart():
    # [START datastore_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import datastore

    # Instantiates a client
    datastore_client = datastore.Client()

    # The kind for the new entity
    kind = "taulu"
    # The name/ID for the new entity
    name = "kuppo"
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task["name"] = "Joanne"
    task["job"] = "seamstress"
    task["food"] = "lasagna"
    task["species"] = "human"

    # Saves the entity
    datastore_client.put(task)

    print(f"Saved {task.key.name}: {task['name']}")
    # [END datastore_quickstart]


if __name__ == "__main__":
    run_quickstart()