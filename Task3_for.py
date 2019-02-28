# Создать список из словарей с оценками учеников 
# разных 
# классов школы 
# вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

total_list=[
    {'school_class': '4a', 'scores': [2,3,4]},
    {'school_class': '5a', 'scores': [5,5,4]}
]
total_score=[]

for classes in total_list:
    class_avg=sum (classes['scores'])/float(len(classes['scores']))     #считаем среднее значение по каждому классу
    total_score.append(class_avg)                                       #добавляем в пустой список среднее значение по каждой школе
    #print (classes['scores'])
    print ("Средний балл по классу ", classes ['school_class'],":",class_avg)

school_avg=sum(total_score)/float(len(total_score))                 #считаем среднее значение по всей школе из созданного списка
print("Средняя оценка по школе составляет: ",school_avg)







