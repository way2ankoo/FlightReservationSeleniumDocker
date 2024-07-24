import json
from typing import Type, TypeVar

from test.util.resource_loader import ResourceLoader

T = TypeVar('T')


class JsonUtil:
    @staticmethod
    def load_json_to_dataclass(path: str, dataclass_type: Type[T]) -> T:
        json_content = ResourceLoader.get_resources(path)

        if json_content is None:
            raise ValueError(f"Failed to load JSON data from {path}")

        try:
            # parse JSON content
            data_dict = json.loads(json_content)
            # convert to dataclass instance
            return dataclass_type(**data_dict)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {path} : {e}")
            # raise
        except TypeError as e:
            print(f"Error converting JSON to {dataclass_type.__name__}: {e}")
            # raise
