from SueldoHorizonte.src.modelo.empleado import Empleado
from SueldoHorizonte.src.modelo.sueldo import Sueldo
from SueldoHorizonte.src.modelo.declarative_base import engine, Base, session

class grupoEmpleado():
    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_empleado(self, nombre, apellido):
        busqueda = session.query(Empleado).filter(Empleado.nombre == nombre).all()
        if len(busqueda) == 0:
            empleado = Empleado(nombre=nombre, apellido=apellido)
            session.add(empleado)
            session.commit()
            return True
        else:
            return False

    def editar_empleado(self, empleado_id, nombre, apellido):
        busqueda = session.query(Empleado).filter(Empleado.nombre == nombre, Empleado.id != empleado_id).all()
        if len(busqueda) == 0:
            empleado = session.query(Empleado).filter(Empleado.id == empleado_id).first()
            empleado.nombre = nombre
            empleado.apellido = apellido
            session.commit()
            return True
        else:
            return False

    def eliminar_empleado(self, empleado_id):
        try:
            empleado = session.query(Empleado).filter(Empleado.id == empleado_id).first()
            session.delete(empleado)
            session.commit()
            return True
        except:
            return False

    def dar_empleado_por_id(self, empleado_id):
        return session.query(Empleado).get(empleado_id).__dict__
