menu_function = """
           *****Menu*****
            (1) Phonebook
            (2) Messages
            (3) Chat
            (4) Cell Register
            (5) Tones
            (6) Settings
            (7) Call divert
            (8) Music
            (9) Games
            (10) Calculator
            (11) Reminders
            (12) Clock
            (13) Profiles
            (14) Services
            (15) Sim services

                        """;
print (menu_function)
        
  menu_decision = int(input("Enter number: "))
        
   match menu_decision:

            case 1: 

                print("PhoneBook"):

                        phone_book = """

                                    (1) Search
                                    (2) Services No
                                    (3) Add name
                                    (4) Erase
                                    (5) Edit
                                    (6) Copy
                                    (7) Assign tone
                                    (8) Send b card
                                    (9) Options
                                    (10) Speed dials
                                    (11) Voice tags

                                                """

      print(phone_book)
    first_decision = int(input("Enter a number: "))
                
match(first_decision)
        case 1:
            print ("Serch")
              

        case 2: 
            print("Service No")
                

        case 3:
            print("Add name")
                

        case 4: 
            print("Erase")
                

        case 5:
            print("Edit")
                

        case 6: 
            print("Copy")
                

        case 7:
            print("Assign tone")
                
        
        case 8: 
            print("Send b card")
                
        
        case 9:
           print("Option")
                
        Option = """
                (1) Memory in use
                (2) Type of view
                (3) Memory status
                            """
                                                      

  print(Options)
                                                               
    first_choice = ("Entwe a number: ")

    match first_chioce:

       case 1: 
         print("Memory in use");
                

         case 2: 
         print("Types of view");
               

          case 3: 
         print("Memory status");
                

         case _:
            print("Invalid");
                

         case 10: 
            print ("Speed dials")
               

         case 11:
            print("Voice tags")

         case _: 
            print("invalid")
             
            
 case 2:
    print("Messages")
                       
       String meassages = """
               (1) Write messages
                (2) Inbox
                (3) outbox
                (4) Picture messages
                (5) Templates
                (6) Smileys
                (7) Message setting
                (8) Info service
                (9) Voice mailbox number
                (10) Services Command editor  

                               """

  print(messages)

   text_messages = int(input("Enter a number: "))
                
    match text_messages


            case 1:
                print ("Write Messages")
                    

            case 2: 
                print("Inbox")
                    

            case 3:
                print("Outbox")
                    

            case 4: 
                print("Picture messages")
                    

            case 5:
                print("Templates")
                    

            case 6: 
                print("Smileys")
                    

            case 7:
                print("Message Settings")
                    
       messages_setting = """

                    (1) Set 1
                    (2) Common

                            """  

           print(messages_setting)

            subChoice1 = int(input("Input Number Choice: "))
                match subChoice1:

                    case 1:
                        print("Set");
            
                    set_menu = """

                            (1) Message centre number
                            (2) Message  sent as
                            (3) Message validity

                                """

               print(set_menu)

           subChoice2 = int(input("Enter a Number: "))
            match subChoice2:

                    case 1:
                        print("Message centre number")

                    case 2: 
                        print("Message sent as")

                    case 3: 
                        print("Message validity")

                    case _: 
                        print("invalid") 

          
        Case 2:
            print("common")
        
            
           common = """
                
               (1) Delivery reports 
               (2) Reply via same centre 
               (3) Character support
        
                        """

            print (common)
        
        subChoice3 = int(input("input A Number Choice: "))
                match subChoice3: 
    
                            case 1:
                                print("delivery reports") 

                            case 2: 
                                print("Reply via same centre")

                            case 3:
                                print("Character via support")
                            
                    
                            case 4: 
                                print("Invalid")

            
                 case 8: 
                    print("info services")
          
                case 9: 
                    print("Voice mailbbox number")

                case 10: 
                    print("Service command editor")

                case _;                                                           
                    print("Invalid")

    
        case 3: 
           print("Chat")

        case 4: 
           print("Call register")

        
        call_register = """

            (1) Missed Calls
            (2) Received Call
            (3) Dialled Numbers
            (4) Erase recent call lista
            (5) Show call duration
            (6) Show call cost
            (7) Call cost settings
            (8) Prepaid credit

                        """

        print(Call_register) 
            register = int(input("Enter Number Choice: "))
             match register: 

                case 1: 
                    print("Missed calls")    

                case 2: 
                    print("Received calls")

                case 3: 
                    print("Dialled Number")

                case 4: 
                    print("Erased recent call lists")

                case _: 
                    print("Call duration")  

            
        call-duration = """
                
                    (1) Last call duration
                    (2) All call duration
                    (3) Received call duration
                    (4) Dialled call duration
                    (5) Clear timers

                        """

         print(call_duration)

      duration = int(Input("Enter number choice: ")
        match duration:
    
            
            case 1:
                print("Last call duration")

            case 2; 
                print("All cals duration")                                                                    
            
            case 3: 
                print("Received calls duration")

            case 4:
                print("Dialled calls duration")

            case 5: 
                print("Clear timers")

            case _: 
                print("Invalid")


        case 6:  Number
            print("Show call costs")

        call_cost = """
        
                (1) Last call costs
                (2) All calls cost
                (3) Clear counters

                """

        print(call_costs)

        costs = int(input("Input Number choice: "))
            match costs: 

            case 1: 
                print("Last call costs")
    
            case 2: 
                print("All calls cost")
            
            case 3: 
               print("Clear counters")
    
            case _:
                print("Invalid")


        case 7:
            print("Call cost setting")

        call_cost_settings = """
            
                    (1) Call cost limit
                    (2) show cost in

                        """

        print(call-cost_settings)

        cost-settings = int(input("input Number Choice: "))
            match cost_settings:

                case 1:
                    print("Call cost limit")

                case 2:
                    print("Show cost in")

                case _: 
                    print("Invalid")


        case 8: 
            print("Prepaid credit")

 case 5: 
      print("Tones")

        tones = """

                    (1) Ringing tone
                    (2) Ringing volumes
                    (3) Incoming call alert
                    (4) Message alert tone
                    (5) Keypad tones
                    (6) warnimg tones
                    (7) Vibrating alert
                    (8) Screen saver
                                    """

        print(tones)
        
        tone_list = int(input("Enter number choice"))
            match tone_list: 

                case 1:
                    print("Ringing tone")

                case 2:
                    print("Ringing volumes")

                case 3:
                    print("Incoming call alert")

                case 4:
                    print("Message alert tone")

                case 5:
                    print('Keypad tones')

                case 6: 
                    print("Warning tones")

                case 7: 
                    print("Vibrating alert")
    
                case 8:
                    print("Screen saver")



    case 6:
        print("Settings")

        settings = """

                (1) Call settings
                (2) Phone settings
                (3) Security settings
                (4) Restor factory settings

                                """
    print (setting)
            
        setting_lists = int(input("Enter number choice; ")
            match setting_lists

        case 1: 
            print("Call setting")

        
            call setting  =  """

                (1) Automatic
                (2) Speed dailing
                (3) Call  waiting options
                (4) Own number sending
                (5) Phone line in use
                (6) Automatic answer
                 
                            """

        print(Call_settings)
    
        call = int(input("Enter number choices: "))
    
            match cell: 

            case 1:
                print("Automatic")

            case 2: 
                print(("Speed dailing"))

            case 3: 
                print("Call waitting option")

            case 4:
                print("Phone line in use")

            case 5: 
                print("Automatic answer"
        
            case_: 
                print("Inalid")




    case 2: 
    
            print("Phone Settings")

            phone settings =  """

                        (1) Language
                        (2) Cell info display
                        (3) Welcome note
                        (4) Network selection
                        (5) Confirm sim service action           
                                                    
                                            """

            print(Phone_setting)
    
        phone = int(input("Enter number choice"))
            match phone: 
                    
                    case 1:
                          print("Language")

                    case 2: 
                         print("Call info display)

                    case 3: 
                        print("welcoe note")

                    case 4: 
                        print("Network selection")

                    case 5: 
                        print("Confirm sim services actions")

                    case _:
                        print("Invalid")

            case 3: 
                print("Security Settings")

            security_settings = """


                        (1) pin code request
                        (2) cell barring service
                        (3) fixed dailing
                        (4) closed user group
                        (5) security level
                        (6) change access coodes
        
                                        """

        print(security_settings)

            security = int(input("input number choice; "))
                match security:
                    
                            case 1:
                                print("PIN code request")

                            case 2: 
                                print("Call barring service")

                            case 3: 
                                print("Fixed dailing")

                            case 4:
                                print("Closed user group")

                            case 5:
                                print("Security level")

                            case 6:
                                print("Change access codes")

                            case _: 
                                print("Invaid")

            
                case 4:
                    print("Restore factory setting")

        
      case 7;
           print("call divert")


      case 8:
           print("Music")

        
                music = """
        
                    (1) Music player
                    (2) Radio
                    (3) Recorder
                    (4) Tracl List
                                    """
    print(music)
    
        music_mennu = int(input("Enter number choice: "))

         match mmusic_menu

                     case 1:
                         print("Music player"

                    case 2:
                         print("Radio")

                    case 3:
                         print("Recorder")

                    case 4: 
                         print("Track list")

                    case _: 
                         print("invalid")

    
    case 9:
        print("Games")

    case 10: 
        print("Calculator")

    case 11; 
        print("reminder")

    casev 12: 
        print("Clock")


        clock = """

            (1) Alarm clock
            (2) Clock settings
            (3) Date Setting
            (4) Stopwatch
            (5) Countdown timer
            (6) Auto update of date and time
                   
                                """

        print(Clock);

            clock_mennu = int(input("Enter number choice: "))

                 case  1:
                     print("Alarm clock")

                case  2:
                     print("Clock setting")
        
        
                case  3:
                     print("Date setting")

                case 4:
                     print("Stopwatch")

                case  5:
                     print("Countdown timer")

                case  6:
                     print("Auto update or date and time")

                case _:
                     print("Invalid") 



    case 13:
        print("Profiles")

    case 14:
        print("Services")

    case 13:
        print("SIM Services")

    case 13:
        print("Invalid")


































































































































                                 
                                   
