import logging
from common.config import LOGO_TABLE, LOGO_DIMENSION, FACE_DIMENSION
from indexer.tools import create_table_mysql, insert_data_to_pg


def do_insert_logo(image_encoder, index_client, conn, cursor, table_name, filename, name, info):
    if not table_name:
        table_name = LOGO_TABLE
    
    vector = image_encoder.execute(filename)
    ids = index_client.insert(table_name, vectors, LOGO_DIMENSION)
    create_table_mysql(conn, cursor, table_name)
    insert_data_to_pg(conn, cursor, table_name, ids[0], name, info, filename)
    
    return "insert successfully!"

def do_insert_face(image_encoder, index_client, conn, cursor, table_name, filename, name, info):
    if not table_name:
        table_name = FACE_TABLE
    
    vector = image_encoder.execute(filename)
    create_table_mysql(conn, cursor, table_name)
    ids = index_client.insert(table_name, vectors, FACE_DIMENSION)
    insert_data_to_pg(conn, cursor, table_name, ids[0], name, info, filename)
    
    return "insert successfully!"

