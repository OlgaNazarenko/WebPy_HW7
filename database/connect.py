from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

#
# import configparser
# import pathlib
# import os
# from pathlib import Path
# # import psycopg2
#
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # path = Path(__file__)
# # ROOT_DIR = path.parent.absolute()
# # config_path = os.path.join(ROOT_DIR, "config.ini")
# # print(f'{config_path=}')
# # config = configparser.ConfigParser()
# # config.read(config_path)
#
# file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
# print(f'{file_config=}')
#
# config = configparser.ConfigParser()
# config.read(file_config)
#
# username = config.get('DB_DEV', "user")
# password = config.get("DB_DEV", "password")
# db_name = config.get("DB_DEV", "db_name")
# host = config.get("DB_DEV", "host")
# port = config.get("DB_DEV", "port")
#
#
# url_to_db = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
#
# engine = create_engine(url_to_db, echo=True)
# print(f"{engine=}")
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
