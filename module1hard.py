import statistics

grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
av_gr = [[sum(grades[0])/len(grades[0])],[sum(grades[1])/len(grades[1])],[sum(grades[2])/len(grades[2])],[sum(grades[3])/len(grades[3])],[sum(grades[4])/len(grades[4])]]
#av_gr = [[statistics.mean(grades[0])],[statistics.mean(grades[1])],[statistics.mean(grades[2])],[statistics.mean(grades[3])],[statistics.mean(grades[4])]] #Подскажите, какой метод лучше использовать?
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
list_students = list(students)
s_list = sorted(list_students)
class_register = {s_list[0]:av_gr[0],s_list[1]:av_gr[1],s_list[2]:av_gr[2],s_list[3]:av_gr[3],s_list[4]:av_gr[4]}
print(class_register)