StrikeOutput0 = 0
StrikeOutput1 = 0
StrikeTotaal = 0
BallTotaal0 = 0
BallTotaal1 = 0
BallTotaal2 = 0
BallZero = 0
InningTotaal = 0
HomeScoreTotaal = 0
OutScoreTotaal = 0
OutTotaal = 0
OutTotaal0 = 0
OutTotaal1 = 0
InningEnd = 0
Inning = 0
InningTeam = 0
def OutDef():
                    global HomeScoreTotaal
                    global OutScoreTotaal
                    global StrikeTotaal
                    global OutTotaal
                    global BallZero
                    global Inning
                    global InningEnd
                    global InningTotaal
                    global BallTotaal0
                    global BallTotaal1
                    global BallTotaal2
                    global StrikeOutput0
                    global StrikeOutput1
                    global OutTotaal0
                    global OutTotaal1
                    global HomeScoreOutput1
                    global HomeScoreOutput0
                    global OutScoreOutput1
                    global OutScoreOutput0
                    global InningTeam

                    if OutTotaal >= 1:
                         if OutTotaal == 1:
                            OutTotaal0 = 1
                            BallTotaal0 = 0
                            BallTotaal1 = 0
                            BallTotaal2 = 0
                            BallZero = 0
                            StrikeOutput0 = 0
                            StrikeOutput1 = 0
                            StrikeTotaal = 0

                         elif OutTotaal == 2:
                                OutTotaal1 = 1
                                BallTotaal0 = 0
                                BallTotaal1 = 0
                                BallTotaal2 = 0
                                BallZero = 0
                                StrikeOutput0 = 0
                                StrikeOutput1 = 0
                                StrikeTotaal = 0

                         elif OutTotaal >= 3:
                             OutTotaal0 = 0
                             OutTotaal1 = 0
                             Inning = Inning + 1
                             InningTeam = InningTeam + 1
                             Lights(0);

def ScoreInput():
    global HomeScoreTotaal
    global OutScoreTotaal

    if InningTeam == 0:

                HomeScoreInput = input("Home Score: ")
                if HomeScoreInput == '+':
                    HomeScoreTotaal = HomeScoreTotaal + 1     

                elif HomeScoreInput == '-':
                    HomeScoreTotaal = HomeScoreTotaal - 1
                   
    if InningTeam == 1:

                OutScoreInput = input("Guest Score: ")
                if OutScoreInput == '+':
                    OutScoreTotaal = OutScoreTotaal + 1
                  

                elif OutScoreInput == '-':
                    OutScoreTotaal = OutScoreTotaal - 1

def ScoreCheck():
        global HomeScoreTotaal
        global OutScoreTotaal
        global StrikeTotaal
        global OutTotaal
        global BallZero
        global Inning
        global InningEnd
        global InningTotaal
        global BallTotaal0
        global BallTotaal1
        global BallTotaal2
        global StrikeOutput0
        global StrikeOutput1
        global OutTotaal0
        global OutTotaal1
        global HomeScoreOutput1
        global HomeScoreOutput0
        global OutScoreOutput1
        global OutScoreOutput0
        global InningTeam

        if HomeScoreTotaal <= 9:
            HomeScoreOutput0 = HomeScoreTotaal
            HomeScoreOutput1 = 0

        elif HomeScoreTotaal >= 10:
            HomeScoreOutputInt = int(HomeScoreTotaal / 10)
            HomeScoreOutputMath = int(HomeScoreOutputInt * 10)
            HomeScoreOutput0 = int(HomeScoreTotaal - HomeScoreOutputMath)
            HomeScoreOutput1 = HomeScoreOutputInt

        if OutScoreTotaal <= 9:
            OutScoreOutput0 = OutScoreTotaal
            OutScoreOutput1 = 0

        elif OutScoreTotaal >= 10:
            OutScoreOutputInt = int(OutScoreTotaal / 10)
            OutScoreOutputMath = int(OutScoreOutputInt * 10)
            OutScoreOutput0 = int(OutScoreTotaal - OutScoreOutputMath)
            OutScoreOutput1 = OutScoreOutputInt
    
def Lights( Test ):
        global HomeScoreTotaal
        global OutScoreTotaal
        global StrikeTotaal
        global OutTotaal
        global BallZero
        global Inning
        global InningEnd
        global InningTotaal
        global BallTotaal0
        global BallTotaal1
        global BallTotaal2
        global StrikeOutput0
        global StrikeOutput1
        global OutTotaal0
        global OutTotaal1
        global HomeScoreOutput1
        global HomeScoreOutput0
        global OutScoreOutput1
        global OutScoreOutput0
        global InningTeam

        if Test == 1:
            BallInput = input("Ball: ")
            StrikeInput = input("Strike: ")
            OutInput = input("Out: ")
            if OutInput == "+":
                BallInput = 0
                StrikeInput = 0

            if StrikeInput == "+":
                StrikeTotaal = StrikeTotaal + 1
                if StrikeTotaal == 1:
                    StrikeOutput0 = 1
                if StrikeTotaal == 2:
                    StrikeOutput1 = 1
                if StrikeTotaal == 3:
                    StrikeOutput0 = 0
                    StrikeOutput1 = 0
                    Lights(0);
                    OutDef()

            if BallInput == '+':
                if BallZero == 3:
                    BallTotaal0 = 0
                    BallTotaal1 = 0
                    BallTotaal2 = 0
                    BallZero = 0
                    Lights(0)
                elif BallZero == 0:
                    BallTotaal0 = 1
                    BallZero =  1
                elif BallZero == 1:
                    BallTotaal1 = 1
                    BallZero = 2
                elif BallZero == 2:
                    BallTotaal2 = 1
                    BallZero = 3
            
            if OutInput == "+":
                OutTotaal = OutTotaal + 1
                global HomeScoreTotaal
                global OutScoreTotaal
                global Inning
                global InningEnd
                global InningTotaal
                global OutTotaal0
                global OutTotaal1
                global HomeScoreOutput1
                global HomeScoreOutput0
                global OutScoreOutput1
                global OutScoreOutput0
                global InningTeam
                OutDef();
                
            if Inning == 2:
                InningTeam = 0
                InningEnd = InningTotaal + 1

        else:
            BallInput = "Reset"
            if BallInput == "Reset":
                BallTotaal0 = 0
                BallTotaal1 = 0
                BallTotaal2 = 0
                BallZero = 0
                StrikeOutput0 = 0
                StrikeOutput1 = 0
                if OutTotaal <= 2:
                    OutTotaal = OutTotaal + 1
                    OutDef();
                StrikeTotaal = 0
                if OutTotaal == 3:
                    OutTotaal = 0
                return
def Printing():
   
    a = HomeScoreOutput1
    b = HomeScoreOutput0
    c = InningEnd
    d = OutScoreOutput1
    e = OutScoreOutput0
    f = BallTotaal0
    g = BallTotaal1
    h = BallTotaal2
    i = StrikeOutput0
    j = StrikeOutput1
    k = OutTotaal0
    l = OutTotaal1

    print("\n")
    print("Home:",[a,b],"______","Inning:",[InningEnd],"______","Guest:",[OutScoreOutput1,OutScoreOutput0])
    print("\n")
    print("Ball:",[f,g,h],"Strike:",[i,j],"Out:",[k,l])
    print("\n")
    print("\n")
def SendingOutPut():
    """" Here the sending of the binary codes comes to play. Also turning on the lights as GPIO's. This will probaly replace the fuction Printing. 
         But for now it will stay like this.
         """
    if a == 0:
        print
    if a == 1:
        print
    #if 

while True:
    ScoreInput();
    ScoreCheck();
    Lights(1);
    Printing();
    