from employe import Employer

class Production(Employer):
    def __init__(self,  nom, prenom, age, date_entre, unite_produite):
      super(). __init__( nom, prenom, age, date_entre)
      self.unite_produite = unite_produite
      
    def calculProduction(self):
      salaire = super().calculSalaire()
      return self.unite_produite * 5 + salaire
    
# production1 = Production('y', 'h', 23, "2024-02-05", 5)

# print(production1.calculProduction())