while True:
    comand = input('')
    try:
        exec(comand)
        print('program successfuly run')
    except:
        print("this program has encounterd a error in your command. please try to fix it." + comand)