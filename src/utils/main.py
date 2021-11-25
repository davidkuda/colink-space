from configparser import ConfigParser


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


if __name__ == "__main__":
    config = parse_config_file()
    print(config)
