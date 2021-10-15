from random import randint
import time

class RussianRoulette():
    def __init__(self):
        self.status = True
    
    def singleplayer(self):
        russian_roulette.trigger_single()

    def multiplayer(self):
        print("\nAfter press the trigger, the cylinder will rotate again..\n")
        time.sleep(1)

        shoot = randint(1,6)
       

        while True:
            bullet = randint(1,6) 
            trigger = input("Press 'F' for firing the gun : ")
            if trigger != 'F':
                print("You can not enter anything except 'F'!!\n")
            else:
                if shoot == bullet:
                    print("The bullet's spot : %s\nThe circle which hitting by cock : %s\n"%(bullet,shoot))
                    print("\n\n   -----  YOU ARE DEAD!  -----")
                    time.sleep(2)
                    self.run()
                    break
                else:
                    print("The bullet's spot : %s\nThe circle which hitting by cock : %s\n"%(bullet,shoot))
                    continue

    
    def trigger_single(self):

        print("\n---  Everyone will shoot himself/herself just once in an order  ---\n")
        time.sleep(2.5)
        print("---  1. shooting: the posibility of hit target is %16,6  ---\n")
        time.sleep(2.5)
        print("---  2. shooting: the posibility of hit target is %20  ---\n")
        time.sleep(2.5)
        print("---  3. shooting: the posibility of hit target is %25  ---\n")
        time.sleep(2.5)
        print("---  4. shooting: the posibility of hit target is %33,3  ---\n")
        time.sleep(2.5)
        print("---  5. shooting: the posibility of hit target is %50  ---\n")
        time.sleep(2.5)
        print("---  6. shooting: the posibility of hit target is %100  ---\n")
        time.sleep(2.5)

        shoot = randint(1,6)
        trigger = randint(1,6)
        magazine = 6
        while True:
            bullet = randint(1,6)
            if magazine > 0:
                while True:
                    trigger = input("Press 'F' for firing the gun : ")
                    if trigger != 'F':
                        print("You can not enter anything except 'F'!!\n")
                    else:
                        break

            if shoot == magazine:
                print("\n\n   -----  YOU ARE DEAD!  -----")
                time.sleep(2)
                self.run()
                break
            else:
                magazine -= 1


    def exit(self):
        print("\n\n   Has Been Quit!\n\n")
        time.sleep(1)
        self.status = False

    def menu(self):
        print("""\n\n |----|   İDRİS BERKALP The Game Of The Russian Roulette   |----|

1 - Classic
2 - MultiPlayer
3 - Exit\n""")

    def choice(self):
        while True:
            try:
                selection = int(input("Please select mode which one you play : "))
                if selection < 1 or selection > 3:
                    print("Please make your choice between 1-3 !\n")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a number !!\n")
                continue
        return selection
    
    def run(self):
        self.menu()
        choice = self.choice()

        if choice == 1:
            self.singleplayer()

        elif choice == 2:
            self.multiplayer()
        
        elif choice == 3:
            self.exit()


russian_roulette = RussianRoulette()
while russian_roulette.run():
    russian_roulette.status