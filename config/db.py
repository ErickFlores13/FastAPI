from sqlalchemy import create_engine, MetaData

#conexión a base de datos
engine = create_engine("mysql+pymysql://root:12345@localhost:3306/logincat")

#Mantiene la conexión a la base de datos, pero afecta rendimiento
conn = engine.connect()

meta_data = MetaData()