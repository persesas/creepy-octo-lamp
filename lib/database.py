import string
import random
from datetime import datetime

import tinydb
from tinydb import where
from tinydb.serialize import Serializer
from tinydb.storages import JSONStorage
from tinydb.middlewares import SerializationMiddleware

"""
Main tables:
Client = id(str), name(str), age(int), address(str), email(str), phone(str),
		 events(event ids)
Employee = id(str), name(str), age(int), address(str), position(str)
Event = id(str), client_id(str), event_type (str), description(str), from_date(date), to_date(date), exp_no(int),
		planned_budget(int), decorations(str), filming(str), poster(str),food(str),
		music(str), computer(str), other(str)
Task = id(str), sub_team(str), priority(str), assign_to(employee id), description(str), event_id(str)
Financial Req = id(str), event_id(str), reason(str), req_dpt(str)
Recruitment Req = id(str), type(str), years_exp(str), job_title(str), job_description(str), req_dpt(str)
Support tables:
Auth = username(str), password(hashed + salt str), salt(str), user_id(cl, empl str)
"""


class Database():
    """Docstring for database manager"""

    tables = ['client', 'event', 'employee', 'task', 'auth', 'financial_req', 'recruitment_req']

    def __init__(self, name='db.json', purge=False):
        # test initial number of tables
        serialization = SerializationMiddleware()
        serialization.register_serializer(DateTimeSerializer(), 'TinyDate')
        self.db = tinydb.TinyDB('Data/' + name, storage=serialization)

        if purge:
            self.db.purge_tables()

        self._init_db()

    def _init_db(self):
        # Ensure that the tables exist
        self.tables_db = {t: self.db.table(t) for t in self.tables}

    def _gen_id(self, length=6, chars=string.digits):
        return ''.join([random.choice(chars) for _ in range(length)])

    # Generic functions
    def get_row_by_id(self, tbl_name, id):
        # Search Client, Employee, Department, Event
        return self.tables_db[tbl_name].search(where('id') == id)

    def search(self, tbl_name, col_name, value):
        # Arbitrary search
        # invalid column
        return self.tables_db[tbl_name].search(where(col_name) == value)

    def insert(self, tbl_name, data):
        # data = {col1:data1, col2:data2, ...}
        # name(test) = non empty and follow the rules, exists -> KeyError
        # empty data on return(where=blabla) = []
        self.tables_db[tbl_name].insert(data)

    def update(self, tbl_name, update_data, cond_col, cond_val):
        # update_data = fields to update in a dictionary
        # Only the event and task will ever need updating
        # The client too, to change his events
        self.tables_db[tbl_name].update(update_data, where(cond_col) == cond_val)

    # Specific functions
    def new_client(self, **kwargs):
        # Client = id(str), name(str), age(int), address(str), email(str),
        #          phone(str), events(event ids)
        user_id = 'cl' + self._gen_id()
        data = {'id': user_id}
        data.update(kwargs)
        self.insert('client', data)

        return user_id

    def get_client(self, col_name, criteria, all_data=False):
        if not all_data:
            return self.tables_db['client'].search(where(col_name) == criteria)
        else:
            return self.tables_db['client'].all()

    def update_client_events(self, cl_id, events):
        # Events is the updated list of events
        self.update('client', {'events': events}, 'id', cl_id)

    def new_employee(self, **kwargs):
        # Employee = id(str), name(str), age(int), address(str), boss(employee id)
        user_id = 'em' + self._gen_id()
        data = {'id': user_id}
        data.update(kwargs)
        self.insert('employee', data)

        return user_id

    def get_employee(self, col_name, criteria, all_data=False):
        if not all_data:
            return self.tables_db['employee'].search(where(col_name) == criteria)
        else:
            return self.tables_db['employee'].all()

    def new_task(self, **kwargs):
        # Task = id(str), subject(str), priority(int), sender(employee id), description(str)
        user_id = 't' + self._gen_id()
        data = {'id': user_id, 'seen': False}
        data.update(kwargs)
        self.insert('task', data)

        return user_id

    def get_task(self, col_name, criteria, all_data=False):
        if not all_data:
            return self.tables_db['task'].search(where(col_name) == criteria)
        else:
            return self.tables_db['task'].all()

    def update_task(self, new_data):
        # Task id is in the new_data
        self.update('task', new_data, 'id', new_data['id'])

    def new_financial_req(self, **kwargs):
        user_id = 'fr' + self._gen_id()
        data = {'id': user_id}
        data.update(kwargs)
        self.insert('financial_req', data)
        return user_id

    def get_financial_req(self, col_name, criteria, all_data=False):
        if not all_data:
            return self.tables_db['financial_req'].search(where(col_name) == criteria)
        else:
            return self.tables_db['financial_req'].all()

    def update_financial_req(self, new_data):
        # Task id is in the new_data
        self.update('financial_req', new_data, 'id', new_data['id'])

    def new_recruitment_req(self, **kwargs):
        user_id = 'rr' + self._gen_id()
        data = {'id': user_id}
        data.update(kwargs)
        self.insert('recruitment_req', data)
        return user_id

    def update_recruitment_req(self, new_data):
        # Task id is in the new_data
        self.update('recruitment_req', new_data, 'id', new_data['id'])

    def get_recruitment_req(self, col_name, criteria, all_data=False):
        if not all_data:
            return self.tables_db['recruitment_req'].search(where(col_name) == criteria)
        else:
            return self.tables_db['recruitment_req'].all()

    def new_event(self, **kwargs):
        # After creating a new event, we have to add it in the clients' event list
        user_id = 'ev' + self._gen_id()
        data = {'id': user_id}
        data.update(kwargs)
        self.insert('event', data)

        return user_id

    def get_event(self, col_name, criteria, all_data=False):
        if not all_data:
            return self.tables_db['event'].search(where(col_name) == criteria)
        else:
            return self.tables_db['event'].all()

    def update_event(self, new_data):
        # Event id is in the new_data
        # def update(self, tbl_name, update_data, cond_col, cond_val):
        self.update('event', new_data, 'id', new_data['id'])

    def get_login_data(self, username):
        r = self.tables_db['auth'].search(where('username') == username)
        return r[0] if r else []

    # Create accounts(admin, pending)
    def new_user(self, username, password, salt, user_id):
        if self.get_login_data(username):
            raise KeyError('User {} already exists.'.format(username))

        self.tables_db['auth'].insert({'username': username,
                                       'password': password,
                                       'salt': salt,
                                       'user_id': user_id})


class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime  # The class this serializer handles

    def encode(self, obj):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')

    def decode(self, s):
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')
