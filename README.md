# auto tests project for interview, which contains files:


 - main_test.py - target file with tests, 600 test in total (2 parametrize marks)
 - conftest.py - file with fixtures, contains 2 fixtures to open and close db connection and to create db instance
 - sql_request.py - file with methods, which nteract with database
 - connections.py - file with base class to connect
 - fill_database.py - file to fill tables ships (200 rows), weapons (20 rows), hulls (5 rows), engines (6 rows)
 - create_config.py - file to create config with database connection parameters
 - requremets.txt - installed for project libraries 
# realized on python 3.11 and PostgresSQL