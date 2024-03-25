# class Device:
#     def __init__(self,price='',work=''):
#         self.price = price
#         self.work = work
#     def action(self):
#         print('продается и работает')

# class CoffeeMachine(Device):
#     def __init__(self,price,work,brand,model):
#         super().__init__(price,work)
#         self.brand= brand
#         self.model = model
#     def coffe_show(self):
#         print(f'кофемашина стоит {self.price},умеет {self.work} кофе,,бренд-{self.brand},модель-{self.model}')

# class Blender(Device):
#     def __init__(self, price,work,brand,model):
#         super().__init__(price, work)
#         self.brand = brand
#         self.model = model
#     def blender_show(self):
#         print(f'блендер стоит {self.price},умеет {self.work} пищу,бренд-{self.brand},модель-{self.model}')
# class MeatGrinder(Device):
#     def __init__(self, price,work,brand,model,):
#         super().__init__(price, work)
#         self.brand = brand
#         self.model = model

#     def meatgrinder_show(self):
#         print(f'стоиомость {self.price}умеет {self.work} мясо в фаршб,бренд-{self.brand},модель-{self.model}')

# device = Device()
# CoffeeMachine(100,'варить','tefal', 'X95').coffe_show()
# Blender(300,'перемалывать','tefal','Gala S21').blender_show()
# MeatGrinder(400,'перекручивает','Naiser', 'V8').meatgrinder_show()




# class Ship:
#     def __init__(self, name='', length=''):
#         self.name = name
#         self.length = length
#     def action(self):
#         print("Плавает и ходит в порт")
# class Frigate(Ship):
#     def __init__(self, name,length,countPeople,speed,paluba):
#         super().__init__(name, length)
#         self.countPeople = countPeople
#         self.speed = speed
#         self.paluba = paluba
#     def  frigate_action(self):
#         print(f'название фригата {self.name},длинна коробля {self.length},аксимальное количетсво человек на борту {self.countPeople},максимальна скорость фригата {self.speed} узлов, количество палуб фригата {self.paluba}')

# class Destroyer(Ship):
#     def __init__(self, name, length, countPeople,speed,paluba):
#         super().__init__(name, length)
#         self.countPeople = countPeople
#         self.speed = speed 
#         self.paluba = paluba
#     def  destroyer_action(self):
#         print(f'название эсминца {self.name},го длинна составляет {self.length},вместимость коробля {self.countPeople},максимальная скорость эсминца {self.speed} узлом,количество палуб судна {self.paluba}')
# class Cruiser(Ship):
#     def __init__(self, name,length,countPeople,speed,paluba):
#         super().__init__(name, length)
#         self.countPeople = countPeople
#         self.speed = speed
#         self.paluba =paluba
#     def  cruiser_action(self):
#         print(f'название лайнера {self.name},его длинна составляет {self.length},максимальное количество человек на борту {self.countPeople},максимальная скорость лайнера {self.speed} узлов,количество палуб у судна {self.paluba}')

# ship = Ship()
# Frigate('черная жемчужина','90 метров','600','50','2').frigate_action()
# Destroyer('Donald Cooke','140 метров','1500','100','4').destroyer_action()
# Cruiser('посейдон' ,'160 метров','3000','60',"7").cruiser_action()




# class Money:
#     def __init__(self,name='', sotni='',edin='',copeika=''):
#         self.name = name
#         self.sotni=sotni
#         self.edin=edin
#         self.copeika=copeika
#     def money_show(self):
#         print('название монеты и ее количество')
# class Euro(Money):
#     def __init__(self, name='', sotni='', edin='', copeika='',country=''):
#         super().__init__(name, sotni, edin, copeika)
#         self.country = country
#     def euro_show(self):
#         print(f'название валюты {self.name},количество:{self.sotni} сотен {self.edin} десятков и {self.copeika} евроцентов используются в стране {self.country}')
# class Dollar(Money):
#     def __init__(self, name='', sotni='', edin='', copeika='',country=''):
#         super().__init__(name, sotni, edin, copeika)
#         self.country = country
#     def dollar_show(self):
#         print(f'название валюты {self.name},количество:{self.sotni} сотен {self.edin} десятков и {self.copeika} центов используются в стране {self.country}')
# class Rubles(Money):
#     def __init__(self, name='', sotni='', edin='', copeika='',country=''):
#         super().__init__(name, sotni, edin, copeika)
#         self.country = country
#     def rubles_show(self):
#         print(f'название валюты {self.name},количество:{self.sotni} сотен {self.edin} десятков и {self.copeika} копеек используются в стране {self.country}')
# money = Money()
# Euro('евро','200','10','50','Евросоюз').euro_show()
# Dollar('доллар','150','50','20','Америка').dollar_show()
# Rubles('рубль','500','50','10','Россия').rubles_show()

