import sys
if ".." not in sys.path:
    sys.path.append("..")

from lib.database import Database
from lib.auth import Authentication

def gen_db():
    #Purge the database
    Database(purge=True)

    # Generate the employees - one of each rank
    gen_employees()
    # Generate two clients
    gen_clients()

def gen_employees():
    a = Authentication()
    """
    name=name, age=age, address=address, mail=mail, position=position
    """
    # Vice presidnent
    a.create_user('employee', 'e8', name='Don Hartley', age='55',
                   address='Beech Street 365', mail='don@gmail.com', position='8')
    # Service
    a.create_user('employee', 'e7', name='Shaw Stonebridge', age='52',
                   address='Oak Street 582', mail='Shaw@gmail.com', position='7')
    # Production
    a.create_user('employee', 'e6', name='Casey Netley', age='49',
                   address='11th Street 749', mail='casey@gmail.com', position='6')
    # Financial
    a.create_user('employee', 'e5', name='Raven Brown', age='50',
                   address='Washington avenue 113', mail='raven@gmail.com', position='5')
    # Administration
    a.create_user('employee', 'e4', name='Eddy Brady', age='35',
                   address='East Street 572', mail='eddy@gmail.com', position='4')
    # Human Resources
    a.create_user('employee', 'e3', name='Neddy Hayley', age='41',
                   address='Crescentt Street 271', mail='neddy@gmail.com' ,position='3')
    # Senior Customer service oficcer
    a.create_user('employee', 'e2', name='Elaina Kelsey', age='39',
                   address='Hamilton Street 29', mail='elaina@gmail.com' ,position='2')
    # Customer service
    a.create_user('employee', 'e1', name='Kayla Bunce', age='28',
                   address='School Street 455', mail='kayla@gmail.com', position='1')
    # Staff
    a.create_user('employee', 'e0', name='Peter Pana', age='22',
                   address='Bro Street 42', mail='peter@gmail.com', position='0')

def gen_clients():
    a = Authentication()

    a.create_user('client', 'c1', name='Ima Client', age='16', address='Clientville 2',
                  mail='invalid@mail.se', phone='01234567', events=[])

    a.create_user('client', 'c2', name='YAC Client', age='106', address='Nexttohighway 42',
                  mail='yaim@mail.se', phone='76543210', events=[])

if __name__ == '__main__':
    gen_db()