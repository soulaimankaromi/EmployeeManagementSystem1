from employee import Employee 
from ir import IR

class Trainer(Employee, IR):
    def __init__(self, mtle=0, nom="soulaimane", dateNaissance="21/02/2004", dateEmbauche="1/09/2023", salaireBase=5000):
        super().__init__(mtle, nom, dateNaissance, dateEmbauche, salaireBase)
        self.__heureSup = 5
        self.__tarifHsup = 70
    
    @property
    def getheureSup(self):
        return self.__heureSup
    @property
    def gettarifHsup(self):
        return self.__tarifHsup
    
    def setheureSup(self, hs1):
        self.__heureSup = hs1
    
    def settarifHsup(self, ths1):
        self.__tarifHsup = ths1
    
    def __str__(self):
        return super().__str__() + f"Number of overtime hours per month: {self.getheureSup} - Remuneration per overtime hour: {self.gettarifHsup}"
    def getIR(self, salaire):
        for i in range(0, len(IR._tranches), 2):
            if IR._tranches[i] <= salaire <= IR._tranches[i + 1]:
                y = int(i / 2)
                return IR._tauxIR[y]
        return IR._tauxIR[len(IR._tauxIR) - 1]
    def salaireAPayer(self):
        return (self.getsalaireBase + self.getheureSup * self.gettarifHsup) * (1 - self.getIR(self.getsalaireBase))