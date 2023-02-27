from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Empleado(Base):
    __tablename__ = 'empleado'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    sueldos = relationship('Sueldo', secondary='sueldo_empleado')

class SueldoEmpleado(Base):
    __tablename__ = 'sueldo_empleado'

    empleado_id = Column(
        Integer,
        ForeignKey('empleado.id'),
        primary_key=True)
    sueldo_id = Column(
        Integer,
        ForeignKey('sueldo.id'),
        primary_key=True)