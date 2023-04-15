from sql_requests import SqlRequests
import configparser
import random


# открываю и читаю конфиг, на основе полученного конфига инициализирую
config = configparser.ConfigParser()
config.read('connection_config')
database = SqlRequests(config)


def fill_weapons_20():
    for weapon in range(20):
        body = f'''
        insert into weapons (
        weapon,
        reload_speed,
        rotational_speed,
        "diameter",
        power_volley,
        "count"
        )
        
        values (
        'weapon-{str(weapon)}',
        {random.randint(1, 20)},
        {random.randint(1, 20)},
        {random.randint(1, 20)},
        {random.randint(1, 20)},
        {random.randint(1, 20)}
        )
        '''
        database.execute_sql(body, select=False)
    print('Filling table weapons success, 20 new weapons added')


def fill_hulls_5():
    for hull in range(5):
        body = f'''
        insert into hulls (
        hull,
        armor,
        "type",
        capacity
        )
        
        values (
        'hull-{str(hull)}',
        {random.randint(1, 20)},
        {random.randint(1, 20)},
        {random.randint(1, 20)}
        )
        '''
        database.execute_sql(body, select=False)
    print('Filling hulls table success, 5 new hulls added')


def fill_engines_6():
    for engine in range(6):
        body = f'''
        insert into engines (
        engine,
        "power",
        "type"
        )
        
        values (
        'engine-{str(engine)}',
        {random.randint(1, 20)},
        {random.randint(1, 20)}
        )
        '''
        database.execute_sql(body, select=False)
    print('Filling engines table success, 6 new engines added')


def fill_ships_200():
    for i in range(200):
        body_to_fill_weapon = '''
        select weapon
        from weapons
        order by random()
        limit 1
        '''
        weapon_name = database.execute_sql(body_to_fill_weapon, fetchone=True)[0]

        body_to_fill_hull = '''
        select hull
        from hulls
        order by random()
        limit 1
        '''
        hull_name = database.execute_sql(body_to_fill_hull, fetchone=True)[0]

        body_to_fill_engine = '''
        select engine
        from engines
        order by random()
        limit 1
        '''
        enngine_name = database.execute_sql(body_to_fill_engine, fetchone=True)[0]

        body_main = f'''
        insert into ships (
        ship,
        weapon,
        hull,
        engine
        )
        
        values (
        'ship-{str(i)}',
        '{weapon_name}',
        '{hull_name}',
        '{enngine_name}'
        )
        '''
        database.execute_sql(body_main, select=False)
    database.close_connection()
    print('Filling ships table success, 200 new ships added')


fill_weapons_20()
fill_hulls_5()
fill_engines_6()
fill_ships_200()
