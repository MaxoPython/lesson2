ans_dict={
    'Как дела?':'Хорошо', 
    'Чем занимаешься?':'Программирую', 
    'Какое сейчас время года?':'Весна'
    }

def ask_user():
    a=0
    while True:
        user_say=input('Задай мне вопрос пожалйута: ')
        for key in ans_dict:
            if key == user_say:
                print(ans_dict[key])
                a=int(1)
                break
        if a!=1:
           print('Очень витиевато формулируешь. Попробуй быть проще!') 
        else: 
           break
        
ask_user()