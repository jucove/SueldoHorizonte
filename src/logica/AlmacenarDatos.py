from SueldoHorizonte.src.modelo.empleado import Empleado
from SueldoHorizonte.src.modelo.sueldo import Sueldo
from SueldoHorizonte.src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
   #Crea la BD
   Base.metadata.create_all(engine)

   #Abre la sesión
   session = Session()

   # Crear sueldo
   sueldo1 = Sueldo(SueldoBasico = 1500, horasExtras = 5, minutosTardanza = 30, diasFalta = 2)
   sueldo2 = Sueldo(SueldoBasico = 2000, horasExtras = 10, minutosTardanza = 20, diasFalta = 1)
   session.add(sueldo1)
   session.add(sueldo2)
   session.commit()

   # Crear empleado
   empleado1 = Empleado(nombre = "Samuel", apellido = "Torres")
   empleado2 = Empleado(nombre = "Robin", apellido = "Espinoza")
   empleado3 = Empleado(nombre = "Juan", apellido = "Perez")
   session.add(empleado1)
   session.add(empleado2)
   session.add(empleado3)
   session.commit()

   # Relacionar sueldo con empleado
   sueldo1.empleados = [empleado2,empleado3]
   sueldo2.empleados = [empleado1]
   session.commit()

   session.close()