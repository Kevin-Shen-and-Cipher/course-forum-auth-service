from dotenv import load_dotenv
import os

load_dotenv()


def get_admin_username():
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    return ADMIN_USERNAME


def get_admin_password():
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
    return ADMIN_PASSWORD


def get_secret_key():
    JWT_SECRET = os.getenv("JWT_SECRET")
    return JWT_SECRET

def get_exp_time():
    EXP_TIME = os.getenv("EXP_TIME")
    return EXP_TIME

def get_ip():
    IP = os.getenv("IP")
    return IP

def get_port():
    PORT = os.getenv("PORT")
    return PORT