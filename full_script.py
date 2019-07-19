"""
Sample ``full_script.py``
-------------------------

This script is intended to be a single-stop shop
for performing analysis on this project.

As you write code, compartmentalize logical sections
within functions and/or scripts as needed.

This module is where you'll plug all the disparate pieces
together so someone can execute the full suite in one go.


Examples
--------

    >>> # This is where you'd put some sample commands
    >>> # Line 2 of the code example
"""

from os.path import join

import postGIS.pg_io as pg_io
from alta_settings import DEFAULT_PG_CONFIG as config

from project_helpers import PG_DB, PROJECT_FILE_ROOT, LOCAL_PROJECTION


def load_shapefiles():
    """ This is a basic single-line docstring explaining what this function does"""

    # Get a list of files in the directory that have '.shp' in the name
    shp_folder = join(PROJECT_FILE_ROOT, 'shapefiles_to_import')
    shapefiles = [x for x in os.listdir(shp_folder) if '.shp' in x]

    # Import the shapefiles in our list
    for shp in shapefiles:
        pg_table_name = shp.replace('.shp', '').replace(' ', '_').lower()
        shp_path = join(shp_folder, shp)
        pg_io.shp_to_postgis(shp_path, pg_table_name, PG_DB, output_epsg=LOCAL_PROJECTION, **config)


def update_value(table_name, column_name, old_val, new_val):
    """
    This is a long-form doctring, with room for multi-line explanation.

    This function updates a column in a PgSQL table, replacing old_val with the new_val

    :param table_name: 'name_of_table'
    :param column_name: 'name_of_col'
    :param old_val: any value that matches the data type of ``column_name``
    :param new_val: any value that matches the data type of ``column_name``

    :return:
    """
    query = f"""
        UPDATE {table_name} SET {column_name} = '{new_val}' WHERE {column_name} = '{old_val}'
    """
    pg_io.execute_query(PG_DB, query, **config)

    return f'Updated {table_name}'


def main():
    load_shapefiles()
    update_value('my_table', 'column_text', 'junky value', 'awesome value')
    update_value('my_table', 'column_int', 999, 5)


if __name__ == '__main__':
    main()
