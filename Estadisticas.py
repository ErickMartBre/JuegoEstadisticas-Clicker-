import shelve
import random
import tkinter as tk


class Game:
    
    def __init__(self):
        self.load_data()
        
        self.ventanaMain = tk.Tk()
        self.ventanaMain.geometry("400x250")
        
        self.LabelGame =tk.Label(self.ventanaMain, text="JUEGO DE ESTADISTICAS")
        self.LabelGame.pack()
    
        self.LevelLabel = tk.Label(self.ventanaMain, text=f"Nivel {self.Level}")
        self.LevelLabel.pack()
        
        self.XPLabel = tk.Label(self.ventanaMain, text=f"XP = {self.XP}")
        self.XPLabel.pack() 
        
        self.CoinsLabel = tk.Label(self.ventanaMain, text=f"Monedas {self.Coins}")
        self.CoinsLabel.pack()
        
        self.BotonJuego = tk.Button(self.ventanaMain, height= 5, width = 30, text="¡Click para ganar experiencia!", command=self.XPCounter)
        self.BotonJuego.pack()
        
        self.StoreButton = tk.Button(self.ventanaMain, text="Tienda",command=self.Store)
        self.StoreButton.pack(pady=10)
        
        self.GamblingButton = tk.Button(self.ventanaMain, height=1,width=12, text="¿Doble o nada?", command=self.Gambling)
        self.GamblingButton.pack()
        
        self.ventanaMain.protocol("WM_DELETE_WINDOW", self.save_and_exit)
        self.ventanaMain.mainloop()
    
    def XPCounter(self):
        self.XP += self.Click
        self.XPLabel.config(text=f"XP = {self.XP}")
        
        if self.XP >= self.NextLevel:
            self.Level += self.LevelGrow
            self.CoinsIncrease += 1
            self.LevelLabel.config(text=f"Nivel {self.Level}")
            
            self.NextLevel = round((self.XP * 0.5) + self.XP)
            
            if self.Level == self.CoinsIncrease:
                self.Coins += 1
                self.CoinsLabel.config(text=f"Monedas {self.Coins}")
    
    def BuyingClick(self):
        
        if self.Coins == 5:
            self.Click += 1
            self.Coins -= 5
            self.CoinsLabel.config(text=f"Monedas {self.Coins}")
        else:
            self.ventanaWarning =tk.Tk()
            self.ventanaWarning.geometry("200x50")
            
            WarningLabel =tk.Label(self.ventanaWarning, text="No tienes suficientes monedas")
            WarningLabel.pack()
    
            
    def Store(self):
        
        self.ventanaStore = tk.Tk()
        self.ventanaStore.geometry("400x350")
        
        StoreLabel = tk.Label(self.ventanaStore, text="Tienda")
        StoreLabel.pack()    
        
        IncrementLabel = tk.Label(self.ventanaStore, text="Incrementa tus click en 1")
        IncrementLabel.pack()
        
        IncrementButton = tk.Button(self.ventanaStore, text="5 Monedas", command=self.BuyingClick)
        IncrementButton.pack()
        
        
        
        ActualClicks = tk.Label(self.ventanaStore, text=f"Clicks adicionales: {(self.Click)-1}")
        ActualClicks.pack()
        
        HintLabel = tk.Label(self.ventanaStore, text="Pista: Cada nivel obtendrás una moneda")
        HintLabel.pack(pady=40)
    
    def Gambling(self):
        
        self.ventanaGambling= tk.Tk()
        self.ventanaGambling.geometry("300x200")
        
        self.GamblingLabel = tk.Label(self.ventanaGambling, text="¿Quieres apostar 1 moneda?\n"
                                                                 "Ganas 1 moneda adicional o la pierdes")
        self.GamblingLabel.pack()
        
        self.FiftyFifty = tk.Button(self.ventanaGambling, text="Prueba tu suerte",command=self.WorL)
        self.FiftyFifty.pack(pady=5)
        
        self.WorLLabel = tk.Label(self.ventanaGambling, text="")
        self.WorLLabel.pack()
        

        
    def WorL(self):
        
        if self.Coins == 0:
            self.ventanaWarning2 = tk.Tk()
            self.ventanaWarning2.geometry("200x50")
            
            WarningLabel2= tk.Label(self.ventanaWarning2, text="No tienes suficientes monedas")
            WarningLabel2.pack()
            
        else:
            Chances = [1,1,2,2]
        
            WorL = random.choice(Chances)
        
            if WorL == 1:
                self.Coins +=1
                self.CoinsLabel.config(text=f"Monedas {self.Coins}")
                self.WorLLabel.config(text="¡Ganaste una moneda!")
            else:
                self.Coins -= 1
                self.CoinsLabel.config(text=f"Monedas {self.Coins}")
                self.WorLLabel.config(text="Perdiste una moneda")
    
    def load_data(self):
        with shelve.open('stats_gamedata') as db:
            self.XP = db.get('XP',0)
            self.Click = db.get('Click', 1)
            self.Level = db.get('Level', 0)
            self.Coins = db.get('Coins', 0)
            self.CoinsIncrease = db.get('CoinsIncrease', 0)
            self.LevelGrow = db.get('LevelGrow', 1)
            self.NextLevel = db.get('NextLevel', 10)   
                
    def save_and_exit(self):
        with shelve.open('stats_gamedata') as db:
            db['XP'] = self.XP
            db['Click'] = self.Click
            db['Level'] = self.Level
            db['Coins'] = self.Coins
            db['CoinsIncrease'] = self.CoinsIncrease
            db['LevelGrow'] = self.LevelGrow
            db['NextLevel'] = self.NextLevel
        self.ventanaMain.destroy()   
            
juego = Game()