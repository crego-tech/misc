import json
import sys


def create_task_definition(json_file, containers, envs):
    """Add image and environment in json file

    Args:
        json_file (String): File path
        containers (List): Containers with container_name and image
        envs (List): List of object with name and value
    """
    with open(json_file, "r", encoding="utf-8") as fp:
        task_json = json.load(fp)
    for container_def in task_json["taskDefinition"]["containerDefinitions"]:
        for container in containers:
            if container["container_name"] == container_def["name"]:
                container_def["image"] = container["image"]
        container_def["environment"] = envs
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(task_json, f)


if __name__ == "__main__":
    create_task_definition(sys.argv[1], json.loads(sys.argv[2]), json.loads(sys.argv[3]))