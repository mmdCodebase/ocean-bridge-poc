from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from internal.get_secret_aws import get_secret

try:
    # Retrieve database connection parameters
    secret_data = get_secret()
    username = secret_data['username']
    password = secret_data['password']
    host = secret_data['host']
    database_name = secret_data['dbname']
    port = secret_data['port']
    ##### You can use your owner connection strings inside using AWS Secret Manager #####
    database_name_test = "OceanBridge"
    password_test = "r4du5SRv23TJ"
    username_test = "agl-akamine"
    #####################################################################################
    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URL = f"mssql+pymssql://{username_test}:{password_test}@{host}:{port}/{database_name_test}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

except Exception as e:
    print(f"An error occurred: {e}")

