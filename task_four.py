new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

if 'task_005' in new_tasks:
    completed_tasks.append(new_tasks.pop(-1)) #Перенес task_005 из new_tasks в completed_tasks

if 'task_007' in new_tasks:
    new_tasks.remove('task_007') # Удалил task_007 из new_tasks


if new_tasks:
    new_priority_task = new_tasks[-1] # Беру последний элемент списка
    print("Задача с высшим приоритетом:", new_priority_task) # Вывожу задачу с наивысшим приоритетом

print(new_tasks)
