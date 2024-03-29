import logging
import time
from common.config import LOGO_TABLE
from indexer.tools import count_table


def do_count_table(index_client, conn, cursor, table_name):
    if not table_name:
        table_name = LOGO_TABLE

    logging.info("doing count, table_name:" + table_name)
    num_milvus = index_client.count(table_name)
    num_mysql = count_table(conn, cursor, table_name)
    return num_milvus, num_mysql