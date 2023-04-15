import configparser

# Создание конфига с подключениями:
config = configparser.ConfigParser()
config.add_section('db_conn')
config.set('db_conn', 'database', 'postgres')
config.set('db_conn', 'user', 'postgres')
config.set('db_conn', 'password', 'postgres')
config.set('db_conn', 'host', 'postgres')
config.set('db_conn', 'port', 'postgres')

with open('connection_config', 'w') as config_file:
    config.write(config_file)
