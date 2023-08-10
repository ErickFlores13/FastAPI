from sqlalchemy import create_engine, MetaData

#conexión a base de datos
engine = create_engine("mysql+pymysql://root:12345@localhost:3306/logincat")

meta_data = MetaData()