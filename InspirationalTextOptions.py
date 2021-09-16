#Jason Wong 3-20-2019
#Project 3 Inspirational Text
#Ths code allows the user to enter a file that can be accessed by Python and gives them
#several options that they can apply to the file. They should be able to input the number
#that correspons with the action and have it run. The user will also be able to run
#the program multiple times and quit when they are done with the program

print("Hi welcome to the better version of Google, Joogle Woogle.")
while True: #This first part of the code asks the user to input a file and has it read.
    try:
        file=input("Please enter the file name: ") 
        with open(file, "r+") as f:
            read_file=f.read()
        break
    except: #A try and except is put here in case the file was not found and they can reenter the file name
        print("File was not found. Please try entering it correctly or another file")
        print()
    
import time

def menu(): #The menu interface that shows all the options they can choose to do
    print()
    print(":::MAIN MENU:::")
    print("[1] Number of occurrences of specific word or phrase")
    print("[2] Search for a specific word or phrase in the text")
    print("[3] Search and replace a word in the text")
    print("[4] Encode the text and save it as a new textfile")
    print("[5] Text to Speech")
    print("[6] Email a text to someone")
    print("[7] Quit Menu")
    while True:
        try: #Here is where they enter the number for the action they want to run. A Try and except is put here in case the do not enter an integer.
            menu_input=int(input("Please press the number that corresponds with the action you want: "))
            break
        except ValueError:
            print()
            print("Please enter a number that corresponds with the command. \nIf you are wanting to quit then press 7")
    print()
    
    if menu_input==1: 
        def menu1(): #Has user input a word and file will go through whole text adding +1 every time word is found in text
            text1_input=input("Please enter a specific word or phrase: ")
            number_found=0
            with open(file, "r") as f:
                for line in f:
                    if text1_input in line:
                        number_found+=1
            print(number_found)
            repeat_menu1=input("Would you like to search for another word or phrase? \nPress y to repeat or any other key to go back to return to the menu. ")
            if repeat_menu1.lower()=="y": #This is how you can return back to the main menu or repeat this part of the code
                menu1()
            else:
                menu()
        menu1()

    if menu_input==2:
        def menu2():
            text2_input=input("Please search for the word or phrase you are trying to find in the text: ")
            print()
            if text2_input in read_file:
                index=read_file.find(text2_input)
                print(read_file[max((index-50),0):index+50]) #prints 50 characters left and write of the searched word
                repeat_menu2=input("\nWould you like to search for another word or phrase? \nPress y to repeat or any other key to go back to return to the menu. ")
                if repeat_menu2.lower()=="y":
                    menu2()
                else:
                    menu()
            else:
                print("Word was not found in the text") #If word is not found in text, it will print this.
                repeat_menu2=input("\nWould you like to search for another word or phrase? \nPress y to repeat or any other key to go back to return to the menu. ")
                if repeat_menu2.lower()=="y":
                    menu2()
                else:
                    menu()
        menu2()

    if menu_input==3:
        def menu3(): #Has user input word to search and what they want to replace it with. 
            text3_input=input("Enter the word to be searched for: ")
            text3_replace=input("What would you like to replace the word with? ")
            with open(file, "r") as f:
                read_file=f.read()
                new_text=read_file.replace(text3_input,text3_replace)
            #User can view the new text in the file
            print("\nThe word", text3_input,"as been replaced with",text3_replace,"\nTo view text, search in files\n")
            repeat_menu3=input("Would you like to replace another word? \nPress y to repeat or any other key to go back to return to the menu. ")
            if repeat_menu3.lower()=="y":
                menu3()
            else:
                menu()
        menu3()

    if menu_input==4:
        def menu4(): #encodes the text so it prints the last word first first word of the text as the last word.
            text4_input=input("Would you like to encode the textfile? \nPress y to encode or any other key to return back to the main menu. ")
            if text4_input=="y":
                with open(file, "r+") as f:
                    read_file=f.read()
                    str_file=str(read_file)
                    lyst_file=list(str_file.split(" "))
                    for i in lyst_file:
                        lyst_file=lyst_file[::-1]
                join_lyst=", ".join(lyst_file)
                with open("encoded_text_project3", "w+") as f: #new file name of encoded text
                    f.write(join_lyst)
                print()
                print("Your file has been encoded. To access it, go to your folder and search for the encoded_text_project3 file to view it.")
                print("You will be returned to the main menu in 10 seconds.")
                time.sleep(10) #automatic return to the menu to make program more futuristic
                menu()
            else:
                menu()

        menu4()
    if menu_input==5:
        def menu5(): #Ok this is a bit funky...I used pip and installed an API google speech so that it turns the textfile into speech and reads it to you.
                     #However, it is buggy and when an error occurs you restart your PC and it works
                     #The problem is that wants you use this part, it kind of stops python so you have to
                     #reload the whole code again. I've tried different things and I think the warning
                     #I put in is the problem why this occurs.
            import os
            from gtts import gTTS
            print("Warning: This text to speech mode can take some time to load depending on how \nlarge the text is so please be patient. \nTo access, go to files and search for file good. You may have to restart computer to run the file.")
            tts=gTTS(text=read_file,lang="en")
            #menu() #You can add this menu() back into the code but it won't run the whole code since it gets taken back to menu.
            tts.save("good.mp3")
            os.system("mpg321 good.mp3")
            
        menu5()
    if menu_input==6:
        def menu6(sender, sendee, header, body, password):
                    
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login(sender, password)
            msg = MIMEMultipart()
            msg['From']= sender
            msg['To']= sendee
            msg['Subject']= header
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)
            del msg
            s.quit()
                    
        import smtplib
        import random
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        while True: #A try and except is entered here in case there is a problm when entering the inputs for the email

            try:
                sender=input("Enter sender's email: ")
                sendee=input("Enter the receiving email i.e(Use slipperysnake117@gmail.com): ")
                header=input("What is the header?: ")
                password=input("Enter sender's password: ")
                email_text=input("Would you like to send a text with a specified word or a random chunk of text? Enter r for random or s for specific or any other key to return to menu. ")
                
                print()
                random_number=random.randint(0,len(read_file)) #This is how we generate a random chunk of text
                text_chunk=(read_file[max((random_number-50),0):min((random_number+100),len(read_file))])
                

                if email_text.lower()=="r":
                    menu6(sender, sendee, header, text_chunk, password) #After entering all the inputs. It will send an email of random text from file
                    print("Email is sent")
                    print("You will be returned to the menu")
                    time.sleep(5)
                    menu()
                if email_text.lower()=="s":
                    specific_word=input("Enter a word to search for: ")
                    if specific_word in read_file:
                        index=read_file.find(specific_word)
                        specific_text=read_file[max((index-50),0):index+50]
                        menu6(sender, sendee, header, specific_text, password)
                        print("Email is sent")
                        print("You will be returned to the menu")
                        time.sleep(5)
                        menu()
                    else:
                        print("Word was not found in text")
                        print("You will be returned to the menu")
                        time.sleep(5)
                        menu()
                else:
                    menu()
            except:
                print("You seem to have encountered error with the email or code. \nPlease try again")
     
    if menu_input==7:
        print("Quitting menu...")
        time.sleep(5)
        print("Goodbye!")
        
menu()
