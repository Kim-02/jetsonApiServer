from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 예시
# SQLite 테스트용:
# DATABASE_URL = "sqlite:///./jetson_hub.db"

# MySQL 예시:
# DATABASE_URL = "mysql+pymysql://user:password@127.0.0.1:3306/jetson_hub"

# Oracle 예시:
# DATABASE_URL = "oracle+cx_oracle://user:password@127.0.0.1:1521/?service_name=xe"

DATABASE_URL = "sqlite:///./jetson_hub.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()