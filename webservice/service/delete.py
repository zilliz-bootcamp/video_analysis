import logging
import time
from common.config import LOGO_TABLE
from indexer.tools import connect_mysql, delete_data, delete_table
import time


def do_delete_table(index_client, conn, cursor, table_name):
    if not table_name:
        table_name = LOGO_TABLE

    logging.info("doing delete table, table_name:", table_name)
    delete_table(conn, cursor, table_name)
    status = index_client.delete_collection(table_name)
    return status
