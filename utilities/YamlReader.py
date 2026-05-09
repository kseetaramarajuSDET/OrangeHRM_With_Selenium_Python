import yaml


class YamlReader:

    @staticmethod
    def read_loginData_from_Yaml_File(filePath):
        with open(filePath, 'r') as file:
            yaml_data = yaml.safe_load(file)
            # We convert the dictionary into a list of tuples for Pytest @parametrize
            return [(yaml_data['user'], yaml_data['pwd'], yaml_data['expected']) for yaml_data in yaml_data]




# //p[text()='Successfully Saved']
# //p[text()='Successfully Updated']
