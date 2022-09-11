import json
import warlock
import dataclasses

import hydra
from hydra.core.config_store import ConfigStore

from src.config import Config

#config_store = ConfigStore.instance()
#config_store.store(name="cfg", node=Config)

#@hydra.main(config_path="../config", config_name="config.yaml", version_base="1.2")
s = """{
    "fields": {
        "project":
            {
                "id": "10000"
            },
        "summary": "No REST for the Wicked.",
        "description": "Creating of an issue using ids for projects and issue types using the REST API",
        "issuetype": {
            "id": 4
        }
    }
}"""


schema = {
    'name': 'Country',
    'properties': {
        'name': {'type': 'string'},
        'abbreviation': {'type': 'string'},
        'population': {'type': 'integer'},
        'states': {
            'type': 'array',
            'items': {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                    },
                    "capital": {
                        "type": "string",
                    }
                }
            }
        }
    },
    'additionalProperties': False,
}

class Endpoint:

    url: str
    verb: str
    headers: dict[str, str]

parameter_definition = {
    'type': 'object',
    'properties': {
        "/": {}
    },
    'patternProperties': {
        "^\w*$": {'type': "string"}
    },
    'additionalProperties': False,
}


endpoints = {
    'name': 'generic_endpoint',
    'properties': {
        'url': {'type': 'string'},
        'verb': {'type': 'string'},
        'params': parameter_definition,
        'headers': {
            'type': 'object',
            'properties': {
                "/": {}
            },
            'patternProperties': {
                "^\w*$": {'type': "string"}
            },
            'additionalProperties': False,
        },

    },
    'additionalProperties': False,
}


def main():
    #loaded = json.loads(s)
    #print(loaded)

    #Fields = warlock.model_factory(schema)

    #bayern = {"name": "Bayern"}
    #hessen = {"name": "Hessen"}


    #f = Fields(name="Deutschland", abbreviation="DE", population=65456)#, states=[bayern, hessen])
    #print(f)
    #as_data_class = dataclasses.

    EndpointDefinition = warlock.model_factory(endpoints)

    headers = {
        "header1": "header1_value",
        "header2": "header2_value",
        "header3": "header3_value",
    }

    params = {
        "param1": "param1_value",
        "param2": "param2_value",
        "param3": "param3_value",
        "param4": "param4_value",
        "param5": "param5_value",
    }

    get_test = EndpointDefinition(url="/rest/api/asdfasd", verb="GET", headers=headers, params=params)
    print(get_test)

    pass



if __name__ == '__main__':
    main()


