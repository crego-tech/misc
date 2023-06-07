import json
import sys
import os


def create_task_definition(json_file, container_names, images_names):
    """Add image and environment in json file

    Args:
        json_file (String): File path
        container_images (List): Containers with container_name and image_name
    """
    container_names = container_names.split(",")
    images_names = images_names.split(",")
    envs = json.loads(os.getenv('TASK_ENVS', "{}"))
    with open(json_file, "r", encoding="utf-8") as file_pointer:
        task_json = json.load(file_pointer)
    for container_def in task_json["taskDefinition"]["containerDefinitions"]:
        for index, container_name in enumerate(container_names):
            if container_name == container_def['name']:
                container_def["image"] = images_names[index]
                container_def["environment"] = envs
    with open(json_file, "w", encoding="utf-8") as file_pointer:
        json.dump(task_json, file_pointer)


if __name__ == "__main__":
    create_task_definition(sys.argv[1], sys.argv[2], sys.argv[3])