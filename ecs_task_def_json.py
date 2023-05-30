import json
import sys
import os


def create_task_definition(json_file, image_name):
    """Add image and environment in json file

    Args:
        json_file (String): File path
        containers (List): Containers with container_name and image
        envs (List): List of object with name and value
    """
    envs = json.loads(os.getenv('TASK_ENVS', "{}"))
    with open(json_file, "r", encoding="utf-8") as file_pointer:
        task_json = json.load(file_pointer)
    for container_def in task_json["taskDefinition"]["containerDefinitions"]:
        container_def["image"] = image_name
        container_def["environment"] = envs
    with open(json_file, "w", encoding="utf-8") as file_pointer:
        json.dump(task_json, file_pointer)


if __name__ == "__main__":
    create_task_definition(sys.argv[1], json.loads(sys.argv[2]))