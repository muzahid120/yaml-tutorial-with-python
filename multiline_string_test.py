import yaml

with open ('multi_line_string.yml','r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as err:
        print(err)