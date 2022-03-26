import random

def hadani():

    # words = ["price","cook","committee","development","suit","canvas","volcano","wilderness","man","whistle","snakes","brother","approval","car","vessel","reward","fruit","smash","cable","curve","country","trail","island","elbow","loaf","toys","parent","boats","donkey","rate","bottle","view","ink","back","experience","air","voyage","education","bread","glass","gold","fish","flame","quarter","blade","birthday","agreement","metal","street","plough","flesh","babies","soap","lawyer","judge","sugar","motion","disgust","end","giant","glue","chairs","look","brake","cow","nut","discussion","cherries","jelly","north","town","cloud","control","grass","honey","trip","balls","break","fast","fall","company","suit","tax","canvas","donkey","music","church","skirt","stew","kiss"]

    # varianta pro manuální zadání slova
    word = str(input("Zadej slovo se kterým chceš hrát : \n"))
    print("Slovo zadáno úspěšně")
        
    # varianta pro random
    # word = random.choice(words)

    hidden_word = len(word) * "_"
    inputs = []
    attempts = 12
    guessed = False

    print(hidden_word)

    while not (guessed == True) and (attempts > 0) :

        user_input = str(input("\nNapiš písmeno : ")).lower()

        if len(user_input) == 1 and (user_input.isalpha()) :
            if user_input in inputs:
                print("Tohle písmeno už jsi hádal debile.\n" + "Použitá písmena : " + str(inputs))
            
            elif user_input in word:
                inputs.append(user_input)
                progress_word = list(hidden_word)
                chars = [i for i, char in enumerate(word) if char == user_input]

                for x in chars:
                    progress_word[x] = user_input

                hidden_word = "".join(progress_word)

                if not "_" in hidden_word:
                    guessed = True

                print(hidden_word)
                
            else :
                inputs.append(user_input)
                attempts = attempts - 1  
                print("Písmeno se nenachází ve slově. \nZbývajících pokusů : " + str(attempts) + "\nPoužitá písmena : " + str(inputs))    

        elif len(user_input) == len(word) and user_input.isalpha():
            print("To není ono slovo")
            attempts = attempts - 1 

        else:
            print("Co děláš ty kokote. Musíš zadat JEDNO PÍSMENO debile.")  

    if guessed == True :
        print("\nTotální masakr. Zbylo ti " + str(attempts) + " pokusů.")
        if attempts == 12:
            print("Hmmm dobrá práce.")
        elif attempts < 12 and attempts > 6 :
            print("Hmmm jako šlo to i líp no.")
        else :
            print("Hmmm jako málem si skončil na pracáku no, nic mlok.")
        konec()
    else:
        print("\nTak ty seš kokot, došly ti pokusy. Správné slovo : " + word)
        konec()
            
def konec():
    konec_input = input("Chceš hrát znovu ? A/N\n").upper()
    if len(konec_input) == 1 and konec_input.isalpha:
        if konec_input == "A":
            hadani()
        elif konec_input == "N":
            print("k kys")
        else:
            print("TY DEMENTE CO DĚLÁŠ PROSTĚ NAPIŠ A NEBO N DEMENTE!!!!!")
    else:
        print("TY DEMENTE CO DĚLÁŠ PROSTĚ NAPIŠ A NEBO N DEMENTE!!!!!")

hadani()