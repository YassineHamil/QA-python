from datetime import datetime
import pandas as pd

class Employer:
    def __init__(self, nom, prenom, age, date_entre):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.date_entre = date_entre
        self.salaire = 1000
        
    def calculSalaire(self):
        new = pd.to_datetime(self.date_entre)
        now = datetime.now()
        year = now.year - new.year
        return self.salaire + year * 50
    
    def get_infos(self):
        return "L'employe", self.prenom, self.nom, self.salaire
    
# employer_1 = Employer('yass', 'h', 23, '2020-8-19')

# print(employer_1.calculSalaire())
# employer_1.get_infos()
# print(employer_1.calculSalaire())
# form = time.strftime("%d/%m/%Y")
# print(form)
# time = '2020-8-19'
# new = pd.to_datetime(time)
# # print(new)
# now = datetime.now()
# day = now.year - new.year
# print(day)

# date string




# time.strftime('%d%m%Y')
# print(time)
# d_string = "2023/09/17"
# # Convert the string to datetime
# dt_obj = pd.to_datetime(d_string)
# days = time - d_string
 
# print(days)