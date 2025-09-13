#Level Table (Progression System of the player)
def Progression_System():   
    Level_exp = [0,100,200,500,1000,2000,5000,10000,20000,50000]
    print(".")
    return Level_exp
    
# Check Level of The Player, after exp is given
def CheckLevel(PlayerExp,Level_exp):
    for el in range(len(Level_exp)):
        print(el)
        print(PlayerExp)
        print(Level_exp)
        if PlayerExp > Level_exp[el] :
            print("Player Level is " + str(el) + " Player has " + str(PlayerExp) + " exp point")
            PlayerLevel = el
        if PlayerExp < Level_exp[el]: 
            PlayerLevel = el
            print("Level")
            break
            
    print(PlayerLevel)
  
    
# Player receive exp, after an action
def Receive_exp(PlayerExp,GainedEXP,LevelArray):
    PlayerExp += GainedEXP
    CheckLevel(PlayerExp,LevelArray)


LevelArray = Progression_System()


if __name__ == "__main__":
    PlayerExp = 0
    GainedEXP = 501
    Receive_exp(PlayerExp,GainedEXP,LevelArray)
    

