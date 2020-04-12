documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }


def people(numbers):
  for number_doc in documents:
    if number_doc['number'] == numbers:
      try:
        print(number_doc['name'])
        break
      except KeyError:
        print('Такого владельца не существует!')  
  else:
    print('Введенного документа не существует!')

def people_list():
  for all_list in documents:
    print(all_list['type'], all_list['number'], all_list['name'])
    
def people_shelf():
  documents_shelf = 0
  input_number = input('Введите номер документа:')
  for shelf in directories:
    documents_shelf += 1   
    if input_number in directories.get(shelf):
      print('Документа на полке', shelf)
      break
    elif documents_shelf == len(directories):
      print('Документа с таким номером не существует!')

def people_add(new_doc_type, new_doc_number,  new_doc_name, new_shelf):
  if int(new_shelf) == 1 or int(new_shelf) == 2 or int(new_shelf) == 3:
    documents.append({"type": new_doc_type,"number": new_doc_number, "name": new_doc_name})
    directories[new_shelf].append(new_shelf)
    print('Вы добавили документ на полку', new_shelf)
  else:
    print('Несуществующая полка!')

def menu():
 while True: 
    print('Приветсвую вас в электронном каталоге! \n Введите команду для навигации по каталогу: \n p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит \n l - команда, которая выведет список всех документов \n s – команда, которая по номеру документа и выведет номер полки, на которой он находится \n a – команда, которая добавит новый документ в каталог и в перечень полок \n n - поиск владельца по номеру документа \n Для выхода наберите q. \n  \n ')
    user_input = input('Введите команду:')
    if user_input == 'p':
      people(input('Введите номер документа:'))
    elif user_input == 'l':
      people_list()
    elif user_input == 's':
      people_shelf()
    elif user_input == 'a':
      people_add(input('Введите номер документа:'), input('Введите тип документа:'), input('Введите имя владельца:'), input('Введите номер полки на которой документ будет храниться:'))
    elif user_input == 'n':
      chek_name()
    elif user_input == 'q':
      print('До свидания!')
      break 
    else:
      print('Вы ввели не существующуюю функцию!')

def chek_name():
  num = input('Введите номер документа:')
  for doc in documents:
    for i in doc:
      name = 0
      if num == doc[i]:
        try:
          name = doc['name']
          print(name)
        except KeyError:
          return 'Несуществующий владелец!'
        print (f'Документу с номером {num} соответсвует: {doc["name"]}')  
        break
  else:
    print('Такого документа не существует!')  


menu()