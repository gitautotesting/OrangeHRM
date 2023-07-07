import configparser

config = configparser.RawConfigParser()

config.read('D:\\Classes\\Framework_Practice\\Configuration\\Config.ini')


class ReadConfig:

    @staticmethod
    def application_url():
        url = config.get('Common Data', 'url')
        return url

    @staticmethod
    def get_username():
        username = config.get("Common Data", 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Common Data', 'password')
        return password

    @staticmethod
    def get_firstname():
        firstname = config.get('Add Employee', 'firstname')
        return firstname

    @staticmethod
    def get_middlename():
        middlename = config.get('Add Employee', 'middlename')
        return middlename

    @staticmethod
    def get_lastname():
        lastname = config.get('Add Employee', 'lastname')
        return lastname

    @staticmethod
    def get_emp_id():
        emp_id = config.get("Add Employee", "emp_id")
        return emp_id
