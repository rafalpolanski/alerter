import io
import configparser

# get key from config INI section
def get_value_from_config(config_file, section, key_name):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config[section][key_name]

# open file for traversing
def open_log_file(name):
    log_file = io.open(name, "rt")
    return log_file

# close file for traversing
def close_log_file(log_file):
    log_file.close()
    return True

# check the number in the string at position
def int_in_string(string, position):
    number = ""
    i = 0
    while string[position + i] != " ":
        number = number + string[position + i]
        i += 1
    return int(number)
