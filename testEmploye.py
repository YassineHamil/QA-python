import unittest
from employe import Employer
from vente import Vente
from representation import Representation
from production import Production

class EmployerTest(unittest.TestCase):

    def setUp(self):
        self.employer = Employer('yass', 'h', 23, '2020-8-19')
    def test_employer_is_instance(self):
#grace a self.assert on fait la verification des elements que l'on veux verifier 

# assertTrue Equal verifie si toto un es un nom correcte etc etc... 
        self.assertTrue(isinstance(self.employer,Employer))
        self.assertEqual("yass", self.employer.nom)
        self.assertEqual("h", self.employer.prenom)
        self.assertEqual(23, self.employer.age)
        self.assertEqual('2020-8-19', self.employer.date_entre)
        self.assertEqual(1000, self.employer.salaire)

# Dans ce cas la on verifie le contexte  (verifie si la phrase attendue es la meme )

    def test_calcule_salaire_employe(self):
        employer = Employer('yass', 'h', 23, '2020-8-19')
        self.assertEqual(1200, employer.calculSalaire())
        # self.assertEqual(300, employer.calculSalaire(employer.salaire))
    
    def test_calcule_salaire_vente(self):
        vendeur = Vente('y', 'h', 23, "2024-02-05", 2000)
        self.assertEqual(1800, vendeur.calculTotal())
        
    def test_calcule_salaire_reprentation(self):
        representation = Representation('y', 'h', 23, "2024-02-05", 2000)
        self.assertEqual(2200, representation.calculRepresentation())
        
    def test_calcule_salaire_production(self):
        production = Production('y', 'h', 23, "2024-02-05", 5)
        self.assertEqual(1025, production.calculProduction())
        
if __name__ == '__main__':
    unittest.main()
    