import sys
import configparser


def main():
    config = configparser.ConfigParser(strict=False)

    try:
        section = sys.argv[1]
        config_key = sys.argv[2]
        config_value = sys.argv[3]
    except IndexError:
        print("Usage: cat test.ini | python parse.py <section> <option> <value>")
        sys.exit(1)

    try:
        config.read_string(''.join(sys.stdin))

        """Try to update or remove a config option from a section, or add the option to a new section."""
        if section in config:
            if config_key in config[section]:
                if config_value == 'delete':
                    config.remove_option(section, config_key)
                else:
                    config[section][config_key] = config_value
            else:
                config.set(section, config_key, config_value)
        else:
            config.add_section(section)
            config.set(section, config_key, config_value)

        config.write(sys.stdout)
    except:
        print("There was an error parsing the config.")


if __name__ == "__main__":
    main()
