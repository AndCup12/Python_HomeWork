# Напишите программу, удаляющую из текста все слова, содержащие "yt".

text = 'Краткие yt ежедневные занятия ytне помогают yt накапливать знания. Исследования доказывают, что  yt студенты, выработавшие  yyyt привычку регулярно учиться, чаще достигают своих целей.'
text_list = text.split()
del_text = 'yt'

result_list = [item for item in text_list if del_text not in item]

print(result_list)