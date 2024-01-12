import unittest 
import cambia_texto

class Pruebas(unittest.TestCase):
    def test_mayusculas(self):
        palabra = 'buenas tardes'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUENAS TARDES')
    
    '''def test_minusculas(self):
        palabra = 'BUENAS TARDES'
        resultado = cambia_texto.todo_minusculas(palabra)
        self.assertEqual(resultado, 'buenas tardes')'''
        
if __name__ == '__main__':
    unittest.main()