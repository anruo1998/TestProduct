import yaml

def get_yaml_data(yaml_file):
    with open(yaml_file, encoding='utf-8') as file:
        return yaml.safe_load(file.read())


if __name__ == '__main__':
    from utils.handle_path import PollyPath
    print(get_yaml_data(PollyPath.configs_path / 'all_elements.yaml'))