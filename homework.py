class Employee:
    """
    Klasa za vraboteni.
    """
    def __init__(
            self,
            first_name:str,
            last_name:str,
            email:str,
            position:str,
            company:str,
            salary:int,
        ):
        """
        Inicijalizirame objekt od klasata Employee.

        :param first_name: str, ime
        :param last_name: str, prezime
        :param email: str, email
        :param position: str, pozicija vo kompanijata
        :param company: str, kompanija
        :param salary: int, plata
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary

    # getter
    @property
    def first_name(self):
        """
        Primer za getter.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, nekoe_frist_name):
        """
        Primer za setter
        """
        self.__first_name = nekoe_frist_name

    @property
    def last_name(self):
        """
        Primer za getter
        """
        return self.__last_name
    
    @last_name.setter
    def last_name(self, nekoe_last_name):
        """
        Primer za setter
        """
        self.__last_name = nekoe_last_name
    
    def full_name(self):
        """
        Funkcija koja vrakja Ime Prezime za Employee.
        """
        full_name = f"{self.__first_name} {self.__last_name}"
        return full_name
    
    def __str__(self):
        return self.full_name()

            
        
class Company:
    """
    Klasa za kompanija.
    """
    def __init__(self, name:str, company_id:int, address=None):
        """
        Inicijalizirame objekt od klasata Company.

        :param name: str, ime na kompanijata
        :parm company_id: int, unikaten broj na kompanija 
        :param address: str, adresa
        """
        self.name = name
        self.company_id = company_id
        self.address = address
        self.employee_list = []
    
    def hire(self, employee:Employee, position:str, salary:int):
        """
        
        """
        # if not isinstance(employee, Employee):
        #     raise Exception(f'Kompanijata ne moze da vraboti employee sto ne e od podatocen tip Employee.')
        print(f'{self.name} go vrabotuva {employee.first_name}')
        employee.position = position
        employee.salary = salary



# company_1 = Company('nekoe ime')
# company_2 = company_1
# company_2 = Company('nov objekt')
# print(id(company_1), id(company_2))
# company_2.name = '1234'
# print(company_1.name, company_2.name)

# semos = Company('Semos')
# ime1 = Employee()
# print(type(semos), type(ime1))
# print(isinstance(semos, Company))

# semos_mk = Company("Semos Makedonija", 1234)


# print(semos_mk.name)
# ime1 = Employee("Ime1", "Prezime1", "ime1@ime1.com", "developer", "semos_mk")

# print(ime1.position, ime1.salary)
# semos_mk.hire(ime1, 'support', 10000000)
# print(ime1.position, ime1.salary)

# ime3 = Employee('Ime3', 'Prezime3', 'ime3@ime3.com', 'developer', 'semos_mk', 100000000)
# print(ime3.full_name())
# print(ime3.first_name, ime3.last_name)

#---------------------------------------------------------------------------

# zadaca 1
# Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.

# company_1 = Company('Company A', 'Bulgaria', 'Street no 1')
# company_2 = Company('Company B', 'Germany', 'Another Street no 2')
# employees = [Employee('John','Doe','john.doe@example.com', 'developer1', 'semos_mk', 100000000),
# Employee('Jane','Smith','jane.smith@example.com', 'developer2', 'semos_mk', 600000),
# Employee('Mark','Wallace','mark.wallace@example.com', 'developer3', 'semos_mk', 50000000)]

#---------------------------------------------------------------------------

# zadaca 2
# Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.

# def average_salaries(companies):
#     total_salaries = sum([employee.salary for employees in companies for employee in employees])
#     return total_salaries / len(companies)
# print(average_salaries([[employees[0], employees[1]], [employees[2]]]))
#---------------------------------------------------------------------------
# zadaca 5
# Da se napravi klasa Produkt.
# Da se dodadat zadolzitelni atriibuti pri kreiranje na instanca od Produkt: 
# naziv, seriski_broj, cena, tip
# i opcionalen atribut kolicina.


class Product:
    def __init__(self, nazif:str, seriski_broj:int, cena:float, tip:str, kolicina:int ):
        self.nazif = nazif
        self.seriski_broj = seriski_broj
        self.cena = cena
        self.tip = tip
        self.kolicina = kolicina


#----------------------------------------------------------
# zadaca 6
# Da se napravi klasa Prodavnica.
# Instancata od prodavnicata, mora da ima: ime, seriski_broj.
# Da se kreira metod dodaj_produkt, koj kje dodava produkti vo prodavnicata,
# so toa sto mora da se proveri dali e od tip Produkt.

class Shop:
    def __init__(self,ime):
        self.ime = ime
        self.produkt = []

# zadaca 8
# Da se kreiraat __str__ metodi za klasite.
# Da se kreira metod pecati_produkti na klasata Prodavnica koj sto kje gi printa site dostapni produkti.

    def pecati_produkti(self):
        print(f"Produkti na prodavnica {self.ime}:")
        for p in self.produkt:
            print(f"- {p}")
    
    def dodaj_produkt(self,produkt):
        if isinstance(produkt,Product):
            self.produkt.append(produkt)
        else:
            print("Fail")
    
    # def __str__(self):
    #     return f"{self.ime} 
        
   
        

prodavnica = Shop()
product1 = Product("Something", 123, 50.0, "tip1", 5)
product2 = Product("Something2", 12345, 10.0, "tip2", 7)
print(product1.nazif)
print(product1.kolicina)

#     ##  instanca 
shop1 = ("shop_name", 123)
shop2 = ("shop_name2", 32123)
# print(type(shop1))

#     #add products   
prodavnica.dodaj_produkt(product1)
prodavnica.dodaj_produkt(product2)

# print([p.nazif for p in prodavnica.produkt])

#------------------------------------------------------------

# zadaca 7
# Da se kreira klasa Kupuvac.
# Sekoj Kupuvac mora da ima: ime, prezime, dostapni_paricni_sredstva.

class Kupuvac:
    def __init__(self, ime:str, prezime:str, dps:float):
        self.__ime = ime #privaten atribut
        self.__prezime = prezime #privaten atribut
        self.dps = dps

#---------------------------------------------------

    




    

        
    



#---------------------------------------------------------------------------

