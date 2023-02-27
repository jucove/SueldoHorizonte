from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Sueldo(Base):
    __tablename__ = 'sueldo'

    id = Column(Integer, primary_key=True)
    SueldoBasico = Column(Integer)
    horasExtras = Column(Integer)
    minutosTardanza = Column(Integer)
    diasFalta = Column(Integer)
    empleados = relationship('Empleado', secondary='sueldo_empleado')
