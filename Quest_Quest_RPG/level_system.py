def Progression_System():
    Level_exp = [0,100,200,500,1000,2000,5000,10000,20000,50000]
    print(".")
    return Level_exp

def CheckLevel(PlayerExp,Level_exp):
    for el in range(len(Level_exp)):
        if PlayerExp > Level_exp[el]:
            print("Player Level is " + str(el) + " Player has " + str(PlayerExp) + " exp point")

def Receive_exp(PlayerExp,GainedEXP,LevelArray):
    PlayerExp += GainedEXP
    CheckLevel(PlayerExp,LevelArray)



LevelArray = Progression_System()

PlayerEXP = 0
GainedEXP = 501
Receive_exp(PlayerEXP,GainedEXP,LevelArray)