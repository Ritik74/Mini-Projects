def start_game():
    print("Aapka swagat hai! Aapka ek adventure shuru hota hai.")
    print("Aap ek jungle mein hain. Aage do raaste hain: ek left aur ek right.")
    choice = input("Kya aap left ya right jana chahenge? (left/right): ").strip().lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Galat input! Kripya 'left' ya 'right' ka chunav karein.")
        start_game()

def left_path():
    print("Aap left raaste par chale gaye. Aap ek nadi ke paas pahunche.")
    print("Nadi mein do machhliyan hain. Ek sundar aur ek ajeeb.")
    choice = input("Aap kaunsi machhli ko pakadne ka soch rahe hain? (sundar/ajeeb): ").strip().lower()

    if choice == "sundar":
        print("Aapne sundar machhli pakad li. Yeh ek magical machhli hai jo aapko ek wish degi!")
        wish = input("Aap kya wish karte hain? (paisa/taqat/dosti): ").strip().lower()
        if wish == "paisa":
            print("Aapko ek bag bhar paisa milta hai! Aap ameer ho gaye!")
        elif wish == "taqat":
            print("Aap ek superhero ban gaye! Aap duniya ko bachane chale gaye.")
        elif wish == "dosti":
            print("Aapki dosti ka asar hai! Aapko ek loyal dost mil gaya.")
        else:
            print("Galat input! Khel khatam hua.")
    elif choice == "ajeeb":
        print("Aapne ajeeb machhli pakad li. Yeh ek dangerous machhli hai! Aapko bhagaana pada.")
        print("Aap jungle se bahar nikal gaye. Khel khatam!")
    else:
        print("Galat input! Kripya 'sundar' ya 'ajeeb' ka chunav karein.")
        left_path()

def right_path():
    print("Aap right raaste par chale gaye. Aap ek purani haveli ke paas pahunche.")
    print("Haveli ka darwaza khula hai. Aap andar jaane ka soch rahe hain.")
    choice = input("Aap andar jaayenge ya nahi? (haan/nahi): ").strip().lower()

    if choice == "haan":
        print("Aap andar gaye. Aapko ek treasure chest milta hai!")
        print("Chest kholne ke liye aapko ek puzzle solve karna hoga.")
        puzzle = input("2 + 2 kitna hota hai? ").strip()
        if puzzle == "4":
            print("Aapne puzzle sahi solve kiya! Chest khulta hai aur aapko bahut saara sona milta hai!")
            next_choice = input("Kya aap sona lekar wapas jana chahte hain ya haveli ke andar aur jaane ka soch rahe hain? (wapas/aur): ").strip().lower()
            if next_choice == "wapas":
                print("Aap sona lekar wapas chale gaye. Aap ameer hain! Khel khatam.")
            elif next_choice == "aur":
                print("Aap haveli ke andar aur jaate hain. Aapko ek spooky ghost milta hai!")
                ghost_choice = input("Kya aap ghost se dosti karna chahenge ya bhagna chahenge? (dosti/bhag): ").strip().lower()
                if ghost_choice == "dosti":
                    print("Aapne ghost se dosti ki! Ab aap ek ghost ke dost hain! Khel khatam.")
                elif ghost_choice == "bhag":
                    print("Aap bhaag gaye aur jungle mein chhup gaye. Khel khatam.")
                else:
                    print("Galat input! Khel khatam.")
        else:
            print("Puzzle galat hai. Haveli ke ghosts aapko pakad lete hain! Khel khatam.")
    elif choice == "nahi":
        print("Aap haveli ke bahar khade hain. Jungle ki taraf wapas chale gaye.")
        print("Khel khatam!")
    else:
        print("Galat input! Kripya 'haan' ya 'nahi' ka chunav karein.")
        right_path()

def mountain_path():
    print("Aap ek pahaad ki taraf badh rahe hain. Wahan pe ek choti si gufa hai.")
    enter_cave = input("Kya aap gufa mein jaayenge? (haan/nahi): ").strip().lower()
    
    if enter_cave == "haan":
        print("Gufa ke andar aapko ek magical crystal milta hai!")
        crystal_choice = input("Kya aap crystal ko uthane ka soch rahe hain? (haan/nahi): ").strip().lower()
        if crystal_choice == "haan":
            print("Jab aap crystal uthate hain, aapko ek magical duniya mein bhej diya jaata hai!")
            magical_choice = input("Kya aap magical duniya mein rehna chahenge ya wapas jana chahenge? (rehna/wapas): ").strip().lower()
            if magical_choice == "rehna":
                print("Aapne magical duniya mein rehne ka chunav kiya! Aapka naya jeevan shuru hota hai!")
            elif magical_choice == "wapas":
                print("Aap wapas aate hain aur phir se gufa se bahar nikalte hain.")
            else:
                print("Galat input! Khel khatam.")
        else:
            print("Aapne crystal ko nahi uthaya. Aap gufa se bahar nikalte hain.")
    elif enter_cave == "nahi":
        print("Aap gufa ke paas khade hain. Aap jungle ki taraf wapas chale gaye.")
    else:
        print("Galat input! Kripya 'haan' ya 'nahi' ka chunav karein.")
        mountain_path()

def village_path():
    print("Aap ek gaon ke paas pahunche. Wahan logon ka bheed hai.")
    print("Ek purani aurat aapko bula rahi hai. Unke paas ek khazana hai lekin unhe madad chahiye.")
    help_choice = input("Kya aap unki madad karna chahenge? (haan/nahi): ").strip().lower()
    
    if help_choice == "haan":
        print("Aapne unki madad ki! Aapko kuch dhoondhna hai jo purani haveli mein hai.")
        search_choice = input("Kya aap haveli ki taraf jaayenge? (haan/nahi): ").strip().lower()
        
        if search_choice == "haan":
            print("Aap haveli pahunche aur andar jaate hain. Aapko ek chhupa hua khazana milta hai!")
            treasure_choice = input("Kya aap khazana le jayenge ya gaon waapas aayenge? (le jaana/waapas): ").strip().lower()
            if treasure_choice == "le jaana":
                print("Aapne khazana le liya aur gaon walon ki madad ki. Aapka naam yaad rakha jaayega!")
            elif treasure_choice == "waapas":
                print("Aap gaon waapas chale gaye. Aapne kisi ki madad nahi ki, lekin aap safe hain.")
            else:
                print("Galat input! Khel khatam.")
        elif search_choice == "nahi":
            print("Aapne unki madad nahi ki. Aap gaon se bhaag gaye.")
        else:
            print("Galat input! Kripya 'haan' ya 'nahi' ka chunav karein.")
            village_path()
    elif help_choice == "nahi":
        print("Aapne unki madad nahi ki. Aap gaon se chale gaye.")
    else:
        print("Galat input! Khel khatam.")
        village_path()

def forest_path():
    print("Aap ek ghane jungle mein hain. Yahan bahut saari kahaniyan hain.")
    print("Aapko ek raazdaar sadak dikhti hai jo aapko alag alag dishao mein le jaati hai.")
    path_choice = input("Kya aap sadak par chalna chahenge? (haan/nahi): ").strip().lower()
    
    if path_choice == "haan":
        print("Aap sadak par chalne lagte hain aur ek pariyon ka ghar dekhte hain.")
        fairy_choice = input("Kya aap pariyon se baat karna chahenge? (haan/nahi): ").strip().lower()
        
        if fairy_choice == "haan":
            print("Pariyan aapko apne ek khaas gyaan se bharpoor karti hain.")
            secret_choice = input("Kya aap unse ek raaz jaan na chahenge? (haan/nahi): ").strip().lower()
            if secret_choice == "haan":
                print("Unhone aapko bataya ki jungle ke beech ek chhupi hui jagah hai jahan aapko khazana mil sakta hai.")
                hidden_treasure_choice = input("Kya aap us jagah ki taraf jaayenge? (haan/nahi): ").strip().lower()
                if hidden_treasure_choice == "haan":
                    print("Aapne chhupi hui jagah dhoondh li aur aapko bahut saara sona milta hai!")
                else:
                    print("Aapne us jagah ki taraf nahi gaya. Aap pariyon ke sath baithkar khush hote hain.")
            elif secret_choice == "nahi":
                print("Aapne raaz jaanne se mana kar diya. Aap pariyon ke saath mazeed samay bitate hain.")
        else:
            print("Aapne pariyon se nahi bola. Aap jungle ke beech aur aage badhte hain.")
    elif path_choice == "nahi":
        print("Aapne sadak par chalne se mana kar diya. Aap jungle mein hi rahte hain.")
    else:
        print("Galat input! Kripya 'haan' ya 'nahi' ka chunav karein.")
        forest_path()

def river_path():
    print("Aap ek nadi ke kinare hain. Nadi ka paani bahut saaf hai.")
    print("Yahan kuch log machhli pakadne aaye hain.")
    fishing_choice = input("Kya aap machhli pakadne ka soch rahe hain? (haan/nahi): ").strip().lower()
    
    if fishing_choice == "haan":
        print("Aapne machhli pakadne ki koshish ki aur ek badi machhli pakad li.")
        print("Machhli ke paas ek secret hai jo aapko ek treasure tak le ja sakta hai.")
        secret_choice = input("Kya aap machhli se raaz jaan na chahenge? (haan/nahi): ").strip().lower()
        if secret_choice == "haan":
            print("Machhli aapko batati hai ki nadi ke paani mein ek chhupi hui khazana hai.")
            treasure_choice = input("Kya aap khazana dhoondne jayenge? (haan/nahi): ").strip().lower()
            if treasure_choice == "haan":
                print("Aap nadi mein dive karte hain aur khazana dhoondh lete hain!")
            else:
                print("Aapne khazana dhoondne se mana kar diya. Aap machhli ke saath samay bitate hain.")
        else:
            print("Aapne raaz jaanne se mana kar diya. Aap machhli ke sath baithkar relax karte hain.")
    elif fishing_choice == "nahi":
        print("Aapne machhli pakadne se mana kar diya. Aap nadi ke kinare chalte hain.")
    else:
        print("Galat input! Kripya 'haan' ya 'nahi' ka chunav karein.")
        river_path()

def final_battle():
    print("Aapka ek final battle hone wala hai. Aapko ek dusht rakshas se ladna hai!")
    print("Aapke paas teen choices hain: sword, magic, ya run.")
    battle_choice = input("Kya aap kya chunenge? (sword/magic/run): ").strip().lower()
    
    if battle_choice == "sword":
        print("Aapne sword uthayi aur rakshas ke sath ladne lage.")
        print("Aap jeet gaye! Rakshas hara diya aur gaon ko bacha liya!")
    elif battle_choice == "magic":
        print("Aapne magic ka istemal kiya aur rakshas ko pyaar se shant kar diya.")
        print("Aapne gaon ko shanti di! Sab khush hain.")
    elif battle_choice == "run":
        print("Aap bhaag gaye! Lekin aapne apne doston ko khud se bacha liya.")
        print("Aap gaon waapas aate hain aur sabko aapka sammaan karte hain.")
    else:
        print("Galat input! Khel khatam.")

def adventure_choice():
    print("Aap ek adventure ka chunav kar sakte hain:")
    print("1. Jungle")
    print("2. Pahaad")
    print("3. Gaon")
    print("4. Jungle Ka Raasta")
    print("5. Nadi Ka Raasta")
    adventure = input("Kya aap jungle, pahad, gaon, jungle ka raasta ya nadi ka raasta ka chunav karte hain? (jungle/pahaad/gaon/jungle/nadi): ").strip().lower()
    
    if adventure == "jungle":
        start_game()
    elif adventure == "pahaad":
        mountain_path()
    elif adventure == "gaon":
        village_path()
    elif adventure == "jungle":
        forest_path()
    elif adventure == "nadi":
        river_path()
    else:
        print("Galat input! Khel khatam.")

if __name__ == "__main__":
    adventure_choice()
    final_battle()