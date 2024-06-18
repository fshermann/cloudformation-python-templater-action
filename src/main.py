import yaml


def example(template_path):
    with open(template_path) as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)
