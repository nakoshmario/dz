text = input('введите имя фаила c расширением .txt ')
try:
        with open(text, 'r', encoding='utf-8') as file:
            print(file.readlines())
except FileNotFoundError:
      print('ERROR')
      with open(text,'w', encoding='utf-8') as file:
            print(file)
def newAliens(file):
    newAliens = input('введите нового сотрудника: ')
    with open (file,'a',encoding='utf-8')as file:
        file.write(f'{newAliens} \n') 
# newAliens(text)

def removie(file):
    # изменить значения в фенкции
    id_aliens=input("Введите ID сотрудника: ")
    
    with open(file,"r",encoding="utf-8") as f:
         data = f.readlines()
         data2 = []
         for i in data:
                if i.find(id_aliens) != -1:
                   l = i.split(" ")
                   print(l)
                   old = input('старое значение: ')
                   new = input('новое значение: ')
                   for  j in range(len(l)):
                        if l[j] == old:
                             l[j] = new
                             gj= ' '.join(l)
                             data2.append(gj)
                else:
                    data2.append(i)

    with open(text,'w',encoding='utf-8') as fiila:
        fiila.writelines(data2)             

removie(text)  

def deleted(file):
     id_aliensdel = input('введите ID  для удаления: ')

     with open(file, "r", encoding= 'utf-8') as server_file :
        lines = server_file.readlines()
        for line in lines:
            if id_aliensdel in line:
               server_file.write(line)
     print("Удалено")

deleted(file)     

def  search_famaly(file):
     spisok1 = []
     fam = input ("Введите Фамилию: ")
     with open (file ,'r', encoding='utf-8') as f:
          lines = f.readlines()
          for line in lines:
                if fam in line:
                        print(f'{line}')
                if fam[0].lower() in line:
                    spisok1.append(line)
    #  print(f'{line}-все вхождения на первую букву {fam[0]}')
     print(spisok1)
search_famaly(text)


def finddel(file):
    text22= []
    id_delete = int(input ('Введите ID для удаления: '))
    with open(file,"r",encoding= 'utf-8') as file:
        lines = file.readlines()
        for i in lines:
            if  id_delete not in i:
                text22.append(i)
        print(text22)
    with open(file,'w',encoding= 'utf-8') as file:
        file.writelines(text22)
finddel(text)
            
                
   

              


    

