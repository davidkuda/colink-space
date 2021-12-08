from configparser import ConfigParser
import uuid


def parse_config_file(config_file_path: str = "config/dwh.cfg") -> dict:
    config = ConfigParser()
    config.read_file(open(config_file_path))
    sections = config.sections()
    configs = {}
    for section in sections:
        section_config = {section: {}}
        for item in config[section].items():
            k = item[0].upper()
            v = item[1]
            section_config[section].update({k: v})
        configs.update(section_config)
    return configs


def create_random_uuid() -> str:
    return str(uuid.uuid4())


def read_users_from_csv():
    PATH_USERS_CSV = "data/users.csv"
    users = []
    with open(PATH_USERS_CSV, "r") as file:
        headers = file.readline()
        for line in file:
            name, email = line.strip().split(",")
            users.append({"name": name, "email": email})
    return users


if __name__ == "__main__":
    config = parse_config_file()
    print(config)
