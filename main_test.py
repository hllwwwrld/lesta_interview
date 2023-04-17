import pytest


class TestMain:

    # temporary fixtures to try few tests (один корабль - 3 параметра)
    # @pytest.mark.parametrize('ship_param', ['weapon', 'hull', 'engine'])
    # @pytest.mark.parametrize('ship_name', [f'ship-0'])

    # giving 3 argumets to test function:
    # database - for executins sql requests in database
    # ship_name, ship_param - name of shi and ship parameter (taken from mark.parametrize)
    # for every ship comparing every parameter name
    # for every parameter testing every parameter's argument (values of parameter are similar)
    @pytest.mark.parametrize('ship_param', ['weapon', 'hull', 'engine'])
    @pytest.mark.parametrize('ship_name', [f'ship-{i}' for i in range(200)])
    def test_compare_instance_ships_with_main_ships(self, database, ship_name, ship_param):
        # taking parameter name from main db
        # taking parameter name from instance
        # giving main=True as a function argument to choose main db or instance db
        main_ship_param_name = database.get_ship_param_name(ship_name, ship_param)
        instance_ship_param_name = database.get_ship_param_name(ship_name, ship_param, main=False)

        # comparing taken names from different db's
        assert main_ship_param_name == \
               instance_ship_param_name, f'Ship {ship_name} have invalid parameter {ship_param} name ' \
                                         f'from main database not similar to instance database ' \
                                         f'expected: {main_ship_param_name} ' \
                                         f'actual: {instance_ship_param_name}'

        # taking all parameter values as a dict {parameter's argument: value} for main and instance db
        main_ship_param_arguments = database.get_ship_param_arguments_values(ship_name, ship_param)
        instance_ship_param_arguments = database.get_ship_param_arguments_values(ship_name, ship_param, main=False)

        # for every parameter's argument comparing value from instance db and main db
        # choosing parameter and its value and comparing
        for argument in main_ship_param_arguments:
            assert main_ship_param_arguments[argument] == \
                   instance_ship_param_arguments[argument], f'Ship: {ship_name} argument: {argument} of {ship_param}' \
                                                            f'from main database not similar to instance database' \
                                                            f'expected: {main_ship_param_name[argument]}' \
                                                            f'actual: {instance_ship_param_arguments[argument]}'
