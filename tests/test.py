import unittest
from SueldoHorizonte.src.logica.grupoEmpleado import grupoEmpleado
from SueldoHorizonte.src.modelo.empleado import Empleado
from SueldoHorizonte.src.modelo.declarative_base import Session

class EmpleadoTestCase(unittest.TestCase):
    def setUp(self):
        self.GrupoEmpleado = grupoEmpleado()

        self.session = Session()

        self.empleado1 = Empleado(nombre='Juan', apellido="Montes")
        self.empleado2 = Empleado(nombre='Aldo', apellido="Gavilan")
        self.empleado3 = Empleado(nombre='Samuel', apellido="Torres")
        self.empleado4 = Empleado(nombre='Arturo', apellido="Sandoval")

        self.session.add(self.empleado1)
        self.session.add(self.empleado2)
        self.session.add(self.empleado3)
        self.session.add(self.empleado4)

        self.session.commit()
        self.session.close()

    def tearDown(self):

        self.session = Session()

        busqueda = self.session.query(Empleado).all()

        for empleado in busqueda:
            self.session.delete(empleado)

        self.session.commit()
        self.session.close()

    def test_agregar_empleado(self):

        resultado = self.GrupoEmpleado.agregar_empleado(nombre="Felipe", apellido="Perez")
        self.assertEqual(resultado, True)

    def test_agregar_empleado_repetido(self):

        resultado = self.GrupoEmpleado.agregar_empleado(nombre="Felipe", apellido="Perez")
        self.assertNotEqual(resultado, False)

