from django.test import TestCase
from control_estudios.models import Curso
# Create your tests here.
class CursoTests(TestCase):
    """ En esta clase van todas la pruebas del modelo Curso. """
    def test_creacion_curso_1(self):
        #caso uso esperado
        curso= Curso(nombre="Titulo", comision=1000)
        curso.save()
        # Compruebo que el curso fue creado
        self.assertEqual(Curso.objects.count(), 1)
        self.assertIsNotNone(curso.id)

    def test_creacion_curso_2(self):
        # caso edge case
        with self.assertRaises(ValueError):
          curso = Curso(nombre="Titulo", comision="SERIAL-1")
          curso.save()
        #Compruebo que el curso fue creado
        self.assertEqual(Curso.objects.count(), 0)
        self.assertIsNotNone(curso.id)