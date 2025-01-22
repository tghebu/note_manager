username = input('Введите имя пользователя:')
title = input('Введите название заметки:')
content = input('Напишите заметку:')
status = input('Введите статус заметки:')
created_date = input('Введите дату создания заметки ( в формате день-месяц-год, например 20-01-2025): ')
issue_date = input('Введите дату дедлайна ( в формате день-меяц-год, например 20-01-2025): ')
temp_created_date = created_date
temp_issue_date = issue_date

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', temp_created_date)
print('Дата истечения заметки (дедлайн):', temp_issue_date)