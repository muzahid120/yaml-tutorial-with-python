import yaml

with open ('list.yml','r') as file:
    try:

        print(yaml.safe_load(file))


    except yaml.YAMLError as err:
        print(err)