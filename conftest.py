from sql_requests import SqlRequests
import pytest
import configparser
import random


@pytest.fixture(scope='session')
def database():
    # opening config and reading it
    config = configparser.ConfigParser()
    config.read('connection_config')
    database = SqlRequests(config)  # initializing class SqlRequests with given config to be able to access database
    yield database
    database.close_connection()  # in the end of the session closing database connection


# fixture for create instance of tables: ships, weapons, hulls, engines with randomized one of tables column
# taking database for create instance as a parameter
@pytest.fixture(scope='session', autouse=True)
def create_database_instance(database):
    # dict of possible tables and list of its possible columns
    main_tables = {
        'weapons': ['weapon', 'reload_speed', 'rotational_speed', '"diameter"', 'power_volley', '"count"'],
        'hulls': ['hull', 'armor', '"type"', 'capacity'],
        'engines': ['engine', '"power"', '"type"'],
        'ships': ['ship', 'weapon', 'hull', 'engine']
    }

    # for every table creating its instance by selecting all from target table
    # every instance table calls "<target table name>_instance"
    for name in main_tables:  # for each table
        body_instance = f'''
        create temp table {name}_instance as (
        select * from {name}
        );
        '''
        database.execute_sql(body_instance, select=False)  # executing body for creating table instance

        # taking all primary_keys from chosen table to randomize each row
        table_primary_keys = database.get_all_names(name)
        for key in table_primary_keys:  # for each row
            # if it's not ships table then changing one of possible columns of table to its possible value
            if name != 'ships':
                body = f'''
                update {name}_instance
                set {random.choice(main_tables[name][1:])} = {random.randint(1, 20)}
                where {name[:-1]} = '{key}'
                '''
            else:  # if its ships table choosing random foreign key value and random possible to its possible values
                column_to_update = random.choice(main_tables[name][1:])  # choosing random foreign key to update
                # getting all possible primary key values for random foreign key from ships
                possible_values = database.get_all_names(column_to_update+'s')
                body = f'''
                update ships_instance
                set {column_to_update} = '{random.choice(possible_values)}'
                where {name[:-1]} = '{key}'
                '''
            database.execute_sql(body, select=False)   # executing sql body to randomize chosen column of chosen table
