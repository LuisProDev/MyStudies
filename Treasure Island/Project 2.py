while True:
  print('''
  *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
  |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____ /
  *******************************************************************************
  ''')
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.") 
  
  start = input("Do you want to start? Y/N: ")
  start = start.lower()
  if start != 'y':
    exit()
  
  print('''\n*************************************************************************
       _________________________________________________________
   /|     -_-                                             _-  |\
  / |_-_- _                                         -_- _-   -| \   
    |                            _-  _--                      | 
    |                            ,                            |
    |      .-'````````'.        '(`        .-'```````'-.      |
    |    .` |           `.      `)'      .` |           `.    |          
    |   /   |   ()        \      U      /   |    ()       \   |
    |  |    |    ;         | o   T   o |    |    ;         |  |
    |  |    |     ;        |  .  |  .  |    |    ;         |  |
    |  |    |     ;        |   . | .   |    |    ;         |  |
    |  |    |     ;        |    .|.    |    |    ;         |  |
    |  |    |____;_________|     |     |    |____;_________|  |  
    |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
    |  |  / __  ()        -|        -  |  /  __--      -   |  |
    |  | /        __-- _   |   _- _ -  | /        __--_    |  |
    |__|/__________________|___________|/__________________|__|
   /                                             _ -        lc \
  /   -_- _ -             _- _---                       -_-  -_ \

  ***********************************************************************************''')

  cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ")
  cross_road = cross_road.lower()
  if cross_road == 'right':
    print(''' 
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⡿⠛⠋⠁⠀⠀⢀⣀⣀⣀⣠⣤⣤⣄⣀⣀⣀⡀⠀⠀⠈⠙⠛⢿⣿⣿⣿
        ⣿⡿⠃⠀⢀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠘⢿⣿
        ⣿⡇⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢸⣿
        ⣿⣷⡄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢠⣾⣿
        ⣿⣿⣿⣷⣤⣌⡙⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⢋⣡⣤⣾⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')
    print("You fell into a hole. Game Over :(")
    exit()
  elif cross_road == 'left':
    print('''
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⠿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿
        ⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿
        ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
        ⣿⠀⠀⣀⣀⣀⣀⣠⣤⣤⣤⣿⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿
        ⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠉⠉⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠉⠉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠛⠂⠀⠀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣦⣤⣀⡀⠐⠒⠢⢤⣄⡀⠀⠀⠈⠉⠉⠙⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡉⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⡀⠀⠀⡠⠞⠃⠀⣠⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡏⠀⠀⣆⠀⠀⠻⣄⠀⠀⠀⣄⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣧⣤⣤⣬⣷⣤⣤⣤⣵⣤⣤⣬⣿⣦⣤⣤⣤⣤⣬⣭⣿⣿⣿⣿ ''')
    
    lake = input("You come by a lake. There is a little island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across ")
    lake = lake.lower()
    
  if lake != 'wait':
    print('''       
                                                      ___.-----.______
                                            ___.-----'::::::::::::::::`---.___
                          _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
            _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
            ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
          :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
            :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
            `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                            `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                                  / `,--.\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
          _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                          ///--\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                          `'           _.'   (    /______     (   `-._   `-._,-'
              ()  ()                 .-' __.-//     /_______---'       `-._   `.
            * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
            `\ )( /*                `'`'                            /_______   _.'
              {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
              !|       `                                              ~~~
            ~~~~~~~~
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')
    
    print("You were attacked by crocodiles. Game Over :(")
    exit()
  if lake == 'wait':
    print("""
                          |
                          |
                |        |
              |-|-|      |
                |        |
                | {O}    |
                '--|     |
                  .|]_   |
            _.-=.' |     |
            |    |  |]_   |
            |_.-='  |   __|__
            _.-='  |\   /|\
            |    |  |-'-'-'-'-.
            |_.-='  '========='
                `   |     |
                  `. |    / \
                    ||   /   \____.--=''''==--.._
                    ||_.'--=='    |__  __  __  _.'
                    ||  |    |    |\ ||  ||  || |                        ___
      ____         ||__|____|____| \||__||__||_/    __________________/|   |
      |    |______  |===.---. .---.========''''=-._ |     |     |     / |   |
      |    ||     |\| |||   | |   |      '===' ||  \|_____|_____|____/__|___|
      |-.._||_____|_\___'---' '---'______....---===''======//=//////========|
      |--------------\------------------/-----------------//-//////---------/
      |               \                /                 // //////         /
      |                \______________/                 // //////         /
      |                                        _____===//=//////=========/
      |==============================================================LGB/
      '----------------------------------------------------------------`""")
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?: ")
    door = door.lower()
      
    if door == 'yellow':
        
      print('''   
          *******************************************************************************
                    |                   |                  |                     |
          _________|________________.=""_;=.______________|_____________________|_______
          |                   |  ,-"_,=""     `"=.|                  |
          |___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
          _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
          |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
          |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
          _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
          |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
          |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
          ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
          /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
          ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
          /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
          ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
          /______/______/______/______/______/______/______/______/______/______/_____ /
          ******************************************************************************* ''')
      print("You've won. Congratulations")
    elif door == 'red':
      print('''                         
              (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) \
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
         )            . `--=.._____..=--'. ./         (
        ((     ) (          )             (     ) (   )>
         > \/^/) )) (   ( /(.      ))     ))._/(__))./ (_.
        (  _../ ( \))    )   \ (  / \.  ./ ||  ..__:|  _. \
        |  \__.  ) |   (/  /: :)) |   \/   |(  <.._  )|  ) )
       ))  _./   |  )  ))  __  <  | :(     :))   .//( :  : |
       (: <     ):  --:   ^  \  )(   )\/:   /   /_/ ) :._) :
        \..)   (_..  ..  :    :  : .(   \..:..    ./__.  ./
                   ^    ^      \^ ^           ^\/^     ^ JaL''')
      print("You were consumed by flames. Game over")
      exit()
    elif door == 'blue':
      print('''                                                                _
                                                                              _( (~\
                      _ _                        /                          ( \> > \
                  -/~/ / ~\                     :;                \       _  > /(~\/
                  || | | /\ ;\                   |l      _____     |;     ( \/ /   /
                  _\\)\)\)/ ;;;                  `8o __-~     ~\   d|      \   \  //
                ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
                (((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
                )))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
                ((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
                )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::| |
                  \ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
                |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
                  ;~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
                  ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
                      ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
                :       ;                     `.      "``::::::''    .'
                    ;                           `.   \_              /
                  ;       ;                       +:   ~~--  `:'  -';
                                                  `:         : .::/
                      ;                            ;;+_  :::. :..;;; ''') 
      print("You were eaten by a beast. Game over")
      exit()
  continue_game = input("Do you want to play again?Y/N ")
  continue_game = continue_game.lower()
  if continue_game == 'y':
    continue
  else:
    exit()