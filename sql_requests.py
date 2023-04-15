from connections import Connections


# class with sql requests, subclass for Connections class
class SqlRequests(Connections):

    # if fetchone=True returning tuple with values of one row, else returning all taken rows
    # if select = true returning rows, else committing changes is database
    def execute_sql(self, body, select=True, fetchone=False):
        try:
            self.cursor.execute(body)
            if select:
                if fetchone:
                    return self.cursor.fetchone()
                else:
                    return self.cursor.fetchall()
            else:
                self.conn_db.commit()
        except:
            print(f'Ошибка выполнения sql-запроса {body}')
            raise Exception

    def close_connection(self):
        self.conn_db.close()

    # to get all primary keys values given table contains
    def get_all_names(self, table):
        body = f'''
        select {table[:-1]} from {table}
        '''
        res = self.execute_sql(body)
        return [name for tu in res for name in tu]

    # take value of given foreign key from ships by ship name
    # taken parameter main to choose witch table (randomized or not) to select from
    def get_ship_param_name(self, ship_name, ship_param, main=True):
        if not main:
            instance_option = '_instance'
        else:
            instance_option = ''

        body = f'''
        select {ship_param}
        from ships{instance_option}
        where ship = '{ship_name}' 
        '''
        res = self.execute_sql(body, fetchone=True)
        return res[0]

    # taking values from table that references to given foreign key in ships for given ship name
    # taken parameter main to choose witch table (randomized or not) to select from
    def get_ship_param_arguments_values(self, ship_name, ship_param, main=True):
        param_tables = {
            'weapons': ['weapon', 'reload_speed', 'rotational_speed', '"diameter"', 'power_volley', '"count"'],
            'hulls': ['hull', 'armor', '"type"', 'capacity'],
            'engines': ['engine', '"power"', '"type"'],
        }

        if not main:
            instance_option = '_instance'
        else:
            instance_option = ''

        body = f'''
        select p.*
        from ships{instance_option}
        join {ship_param}s{instance_option} p
        using({ship_param})
        where ship = '{ship_name}'
        '''

        # taking one row of values from table, where primary key == ship chosen foreign key
        res = self.execute_sql(body, fetchone=True)

        # create dict with format {foreign key's argument from ship: its value}
        return {param_tables[ship_param+'s'][i]: res[i] for i in range(1, len(res))}
