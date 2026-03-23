from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from datetime import datetime
from app.db.database import Base


class Sensor(Base):
    __tablename__ = "sensor"

    sen_id = Column(Integer, primary_key=True, index=True)
    sen_dept = Column(String(10), nullable=False)
    sen_cr = Column(String(20), nullable=False)
    sen_nm = Column(String(20), nullable=False)
    sen_num = Column(String(20), nullable=False)
    sen_mnum = Column(Integer, nullable=False)
    wp_id = Column(Integer, ForeignKey("workplace.wp_id"), nullable=False)


class StateCode(Base):
    __tablename__ = "state_code"

    st_cd_id = Column(Integer, primary_key=True, index=True)
    st_sp = Column(String(20), nullable=False)


class Worker(Base):
    __tablename__ = "worker"

    dept_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)
    rank = Column(String(20), nullable=False)
    is_manager = Column(Boolean, nullable=False)
    wp_id = Column(Integer, ForeignKey("workplace.wp_id"), nullable=False)


class Manage(Base):
    __tablename__ = "manage"

    worker_dept_id = Column(Integer, ForeignKey("worker.dept_id"), primary_key=True)
    manager_dept_id = Column(Integer, ForeignKey("worker.dept_id"), nullable=False)


class ThTrans(Base):
    __tablename__ = "th_trans"

    sen_id = Column(Integer, ForeignKey("sensor.sen_id"), primary_key=True)
    time = Column(DateTime, primary_key=True, default=datetime.utcnow)
    wp_id = Column(Integer, ForeignKey("workplace.wp_id"), nullable=False)
    temp = Column(Float, nullable=False)
    humd = Column(Float, nullable=False)


class WdTrans(Base):
    __tablename__ = "wd_trans"

    sen_id = Column(Integer, ForeignKey("sensor.sen_id"), primary_key=True)
    time = Column(DateTime, primary_key=True, default=datetime.utcnow)
    wp_id = Column(Integer, ForeignKey("workplace.wp_id"), nullable=False)
    sk_temp = Column(Float, nullable=False)
    hr = Column(Float, nullable=False)


class SituTrans(Base):
    __tablename__ = "situ_trans"

    sen_id = Column(Integer, ForeignKey("sensor.sen_id"), primary_key=True)
    time = Column(DateTime, primary_key=True, default=datetime.utcnow)
    wp_id = Column(Integer, ForeignKey("workplace.wp_id"), nullable=False)
    detail = Column(String(200), nullable=False)


class EventTrans(Base):
    __tablename__ = "event_trans"

    dept_id = Column(Integer, ForeignKey("worker.dept_id"), primary_key=True)
    time = Column(DateTime, primary_key=True, default=datetime.utcnow)
    wp_id = Column(Integer, ForeignKey("workplace.wp_id"), nullable=False)
    state_code = Column(String(100), nullable=False)
    detail = Column(String(200), nullable=False)


class Workplace(Base):
    __tablename__ = "workplace"

    wp_id = Column(Integer, primary_key=True, index=True)
    wp_nm = Column(String(20), nullable=False)