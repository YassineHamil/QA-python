from employe import Employer

class Vente(Employer):
    def __init__(self,  nom, prenom, age, date_entre, chiffre_affaire):
      super(). __init__( nom, prenom, age, date_entre)
      self.chiffre_affaire = chiffre_affaire
      
    def calculTotal(self):
      salaire = super().calculSalaire()
      return self.chiffre_affaire * 0.20 + 400 + salaire
    
# vendeur1 = Vente('y', 'h', 23, "2024-02-05", 2000)

# print(vendeur1.calculTotal())