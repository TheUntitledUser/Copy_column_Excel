import pandas as pd

old_file ='file\Kemerovo.xls'
new_file = 'file\Update.xls'
column_to_copy = {"Обучающийся"}

try:
    df_ish = pd.read_excel('old_file')
    df_copy = df_ish [column_to_copy]
    df_copy.to_excel ('new_file', index = False)
    print(f"Столбцы {column_to_copy} успешно скопированы в файл {new_file}")
    
except FileNotFoundError:
    print(f"Ошибка: Файл {old_file} не найден")
except KeyError as e:
    print(f"Ошибка: Не найден один из указанных столбцов - {e}")
except Exception as e:
    print(f"Произошла ошибка - {e}")    