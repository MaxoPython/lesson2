def occupation (age):
    if age >0 and age<=7:
        return "Вам самое время посещать Детский сад!"
    elif age>7 and age<=16:
       return "Время учиться - идите в школу!"
    elif age>16 and age<=22:
        return "Вы вечный студент!"
    elif age >22 and age<=65:
        return "Принесите стране пользу - идите на завод!"
    else:
        return "Вы стар! Вы - супер Стар!"

age=int(input("Введите свой возраст: "))
if age<=0:
    print("Возраст не может быть отрицательным или равен 0!")
else:  
    occupation(age)
    print(occupation(age))