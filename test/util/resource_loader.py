import json
import os


class ResourceLoader:

    @staticmethod
    def get_resources(path):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        resource_path = os.path.join(base_dir, path)
        print(resource_path)
        data = None
        try:
            if os.path.exists(resource_path):
                with open(resource_path, 'r') as file:
                    data = file.read()
            else:
                raise FileNotFoundError(f"File not found at path: {resource_path}")
        except Exception as e:
            print(f"Unable to read test data {path}.\n{e}")

        return data
