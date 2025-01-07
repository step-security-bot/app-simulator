from createComposeFile import plural_to_singular, render_compose_file
from jinja2 import Environment, FileSystemLoader
import pytest

@pytest.fixture(scope="session")
def load_template():
    env = Environment(loader=FileSystemLoader('.'))
    env.filters['singularize'] = plural_to_singular
    return env.get_template('docker-compose.j2')


def test_render_compose_file_with_empty_config_and_defaults(load_template):
    result = render_compose_file(load_template, {}, {})
    expected = """
services:
  ## services
  ## databases
  ## loaders
configs:
""".strip()
    assert result == expected

def test_render_compose_file_with_simple_config_and_no_defaults(load_template):
    result = render_compose_file(load_template, {
        "global": {
            "imageNamePrefix": "test/",
            "imageNameSuffix": "test"
        },
        "services": {
            "test": {
                "type": "java"
            }
        },
        "databases": {
            "testdb": {
                "type": "mysql"
            }
        },
        "loaders": {
            "testloader": {
                "type": "curl"
            }
        }
    }, {})
    expected = """
services:
  ## services
  test:
    image: test/app-simulator-services-java:test
    configs:
      - source: services_test_config
        target: /config.json
  ## databases
  testdb:
    image: test/app-simulator-databases-mysql:test
    configs:
      - source: databases_testdb_config
        target: /config.json
  ## loaders
  testloader:
    image: test/app-simulator-loaders-curl:test
    configs:
      - source: loaders_testloader_config
        target: /config.json
configs:
  services_test_config:
    content: |
      {"type": "java"}
  databases_testdb_config:
    content: |
      {"type": "mysql"}
  loaders_testloader_config:
    content: |
      {"type": "curl"}
""".strip()
    assert result == expected

def test_render_compose_file_with_simple_config_and_defaults(load_template):
    result = render_compose_file(load_template, {
        "services": {
            "test": {
                "type": "java"
            }
        },
        "databases": {
            "testdb": {
                "type": "mysql"
            }
        },
        "loaders": {
            "testloader": {
                "type": "curl"
            }
        }
    }, {
      "imageNamePrefix": "test/",
      "imageNameSuffix": "test"
    })
    expected = """
services:
  ## services
  test:
    image: test/app-simulator-services-java:test
    configs:
      - source: services_test_config
        target: /config.json
  ## databases
  testdb:
    image: test/app-simulator-databases-mysql:test
    configs:
      - source: databases_testdb_config
        target: /config.json
  ## loaders
  testloader:
    image: test/app-simulator-loaders-curl:test
    configs:
      - source: loaders_testloader_config
        target: /config.json
configs:
  services_test_config:
    content: |
      {"type": "java"}
  databases_testdb_config:
    content: |
      {"type": "mysql"}
  loaders_testloader_config:
    content: |
      {"type": "curl"}
""".strip()
    assert result == expected

def test_render_compose_file_with_port_config(load_template):
    result = render_compose_file(load_template, {
        "global": {
            "imageNamePrefix": "test/",
            "imageNameSuffix": "test",
            "defaultPorts": {
                "services": 1024,
                "databases": 5432,
                "loaders": 1025
            },
            "_defaultDefaultPorts": {
                "services": 8080,
                "databases": 5432,
                "loaders": 6000
            }
        },
        "services": {
            "test": {
                "type": "java"
            }
        },
        "databases": {
            "testdb": {
                "type": "mysql"
            }
        },
        "loaders": {
            "testloader": {
                "type": "curl"
            }
        }
    }, {})
    expected = """
services:
  ## services
  test:
    image: test/app-simulator-services-java:test
    environment:
      - SERVICE_DEFAULT_PORT=1024
    cap_add:
      - NET_BIND_SERVICE
    configs:
      - source: services_test_config
        target: /config.json
  ## databases
  testdb:
    image: test/app-simulator-databases-mysql:test
    configs:
      - source: databases_testdb_config
        target: /config.json
  ## loaders
  testloader:
    image: test/app-simulator-loaders-curl:test
    environment:
      - LOADER_DEFAULT_PORT=1025
    configs:
      - source: loaders_testloader_config
        target: /config.json
configs:
  services_test_config:
    content: |
      {"type": "java"}
  databases_testdb_config:
    content: |
      {"type": "mysql"}
  loaders_testloader_config:
    content: |
      {"type": "curl"}
""".strip()
    assert result == expected