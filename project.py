print("welcome to heirsh tours and travels for maharashhtra")
print("in accosiation with the gretest codinng class SMOWL")
print("we offer bus,plane and taxi")
so=str(input("what will you choose:"))
if(so=="bus"):
    print("bus offers travel to nashik,bombay,aurangabad,navi mumbai")
    dodo=str(input("where would you like to go"))
    if(dodo=="bombay"):
        print("thats nice dont forget to check the india gate")
        print("every km is 10 rupees so your total is 1480 rupees")
        print("after applaying your first time discount your total comes to",90/100*1480,"thank you for choosing us")
    if(dodo=="nashik"):
        print("thats nice dont forget to check the pandav leni caves")
        print("every km is 10 rupees so your total is 2110 rupees")
        print("after applaying your first time discount your total comes to",90/100*2110,"thank you for choosing us")
    if(dodo=="aurangabad"):
        print("thats nice dont forget to check the Bibi Ka Maqbara")
        print("every km is 10 rupees so your total is 2360 rupees")
        print("after applaying your first time discount your total comes to",90/100*2360,"thank you for choosing us")
    if(dodo=="navi mumbai"):
        print("every km is 10 rupees so your total is 1270 rupees")
        print("after applaying your first time discount your total comes to",90/100*1270,"thank you for choosing us")
    

if(so=="plane","aeroplane"):
    print("bus offers travel to nashik,bombay,aurangabad,nagpur")
    no=str(input("where would you like to go"))
    if(no=="bombay"):
        print("thats nice dont forget to check the india gate")
        print("every km is 100 rupees so your total is 14800 rupees")
        print("after applaying your first time discount your total comes to",90/100*14800,"thank you for choosing us")
    if(no=="nashik"):
        print("thats nice dont forget to check the pandav leni caves")
        print("every km is 100 rupees so your total is 21100 rupees")
        print("after applaying your first time discount your total comes to",90/100*21100,"thank you for choosing us")
    if(no=="aurangabad"):
        print("thats nice dont forget to check the Bibi Ka Maqbara")
        print("every km is 100 rupees so your total is 23600 rupees")
        print("after applaying your first time discount your total comes to",90/100*23600,"thank you for choosing us")
    if(no=="nagpur"):
        print("every km is 100 rupees so your total is 71200 rupees","dont forget to visit the swaminarayan temple")
        print("after applaying your first time discount your total comes to",90/100*71200,"thank you for choosing us")
    else:
        print(".")
if(so=="taxi","car"):
    print("taxi offers travel to nashik,bombay,aurangabad,nagpur,navi mumbai")
    ge=str(input("where would you like to go"))
    if(ge=="bombay"):
        print("thats nice dont forget to check the india gate")
        print("every km is 20 rupees so your total is 2960 rupees")
        print("after applaying your first time discount your total comes to",90/100*2960,"thank you for choosing us")
    if(ge=="nashik"):
        print("thats nice dont forget to check the pandav leni caves")
        print("every km is 20 rupees so your total is 4220 rupees")
        print("after applaying your first time discount your total comes to",90/100*4220,"thank you for choosing us")
    if(ge=="aurangabad"):
        print("thats nice dont forget to check the Bibi Ka Maqbara")
        print("every km is 20 rupees so your total is 4720 rupees")
        print("after applaying your first time discount your total comes to",90/100*4720,"thank you for choosing us")
    if(ge=="nagpur"):
        print("every km is 20 rupees so your total is 14240 rupees","dont forget to visit the swaminarayan temple")
        print("after applaying your first time discount your total comes to",90/100*14240,"thank you for choosing us")
    if(ge=="navi mumbai"):
        print("every km is 20 rupees so your total is 2540 rupees")
        print("after applaying your first time discount your total comes to",90/100*2540,"thank you for choosing us")
        hotel=str(input("would you like to also book a hotel"))
    else:
        print("not valid")
else:
    print("we dont have that vehicle access for you")

np=str(input("would you also like to pick a package for where you are going"))
if(np=="yes"):
    db=str(input("so where have you picked as a destination"))
    if(db=="navi mumai"):
        skrt=str(input("thats great we have a package for 7 grand per head and accomodation at the taj for 4 days so yes or no"))
        if(skrt=="yes"):
            print("thats great checkout amount added 7000")

    if(db=="mumbai"):
        nope=str(input("thats great we have a package for 7 grand per head and accomodation at the taj for 4 days so yes or no"))
        if(nope=="yes"):
              print("thats great checkout amount added 7000")

    if(db=="nagpur"):
        memes=str(input("thats great we have a package for 7 grand per head and accomodation at the taj for 4 days so yes or no"))
        if(memes=="yes"):
              print("thats great checkout amount added 7000")

    if(db=="aurangabad"):
        yeti=str(input("thats great we have a package for 7 grand per head and accomodation at the taj for 4 days so yes or no"))
        if(yeti=="yes"):
              print("thats great checkout amount added 7000")

    if(db=="nashik"):
        bits=str(input("thats great we have a package for 7 grand per head and accomodation at the taj for 4 days so yes or no"))
        if(bits=="yes"):
              print("thats great checkout amount added 7000")

        else:
            print("invalid")
    else:
        print("not availible")





                
