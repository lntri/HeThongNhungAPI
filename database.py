from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# engine = create_engine("sqlite:///signal.db")
engine = create_engine("mysql+pymysql://nhom2:uitstudent@192.168.5.129/SignalAPI")  # Sử dụng pymysql driver
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class Turbidity(Base):
    __tablename__ = "turbidity"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String(50))
    raw = Column(Integer)
    ntu = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)