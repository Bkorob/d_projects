import json

config_file_by_env_name = {
    "development" : "database.development.json",
    "production" : "database.production.json",
    "test" : "database.test.json"
}

config = None
env_name = "production" # текущая среда
filename = config_file_by_env_name.get(env_name)
if filename is not None:
    with open(filename, "r") as fd:
        config = json.load(fd)
else:
    raise Exception("Improperly configured")