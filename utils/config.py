from dotenv import DotEnv

dotenv = DotEnv('../config/.env')


def get_admin_username():
    ADMIN_USERNAME = dotenv.get('ADMIN_USERNAME')
    return ADMIN_USERNAME


def get_admin_password():
    ADMIN_USERNAME = dotenv.get('ADMIN_USERNAME')
    return ADMIN_USERNAME


def get_secret_key():
    JWT_SECRET = dotenv.get('JWT_SECRET')
    return JWT_SECRET

def get_ip():
    IP = dotenv.get('IP')
    return IP

def get_port():
    PORT = dotenv.get('PORT')
    return PORT