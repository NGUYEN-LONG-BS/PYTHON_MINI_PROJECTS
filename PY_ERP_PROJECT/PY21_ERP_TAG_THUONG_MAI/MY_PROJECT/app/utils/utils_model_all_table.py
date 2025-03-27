from sqlalchemy import create_engine, Column, String, Integer, DateTime, DECIMAL
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class InventoryCategory(Base):
    __tablename__ = 'TB_INVENTORY_CATEGORIES_250214_09h05'  # Tên bảng trong SQL Server

    # Định nghĩa các trường trong bảng
    ID = Column(UNIQUEIDENTIFIER, primary_key=True, default=func.newid())  # Use NEWID() for GUID generation
    DATE = Column(DateTime, nullable=False, default=func.getdate())  # Default to current date/time
    ID_NHAN_VIEN = Column(String(10), nullable=True)
    XOA_SUA = Column(String(10), nullable=True)
    MA_HANG = Column(String(50), nullable=True)
    TEN_HANG = Column(String, nullable=True)  # Tương ứng với nvarchar(max)
    DVT = Column(String(50), nullable=True)
    SL_TON_DAU_KY = Column(DECIMAL(15, 2), nullable=True)
    DON_GIA_TON_DAU_KY = Column(DECIMAL(15, 2), nullable=True)
    MA_KHO_LUU_TRU = Column(String(50), nullable=True)