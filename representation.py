from employe import Employer

class Representation(Employer):
    def __init__(self,  nom, prenom, age, date_entre, chiffre_affaire):
      super(). __init__( nom, prenom, age, date_entre)
      self.chiffre_affaire = chiffre_affaire
      
    def calculRepresentation(self):
      salaire = super().calculSalaire()
      return self.chiffre_affaire * 0.20 + 800 + salaire
    
# representation1 = Representation('y', 'h', 23, "2024-02-05", 2000)

# print(representation1.calculRepresentation())