from dotenv import load_dotenv
import os

load_dotenv()


def get_admin_username():
    admin_username = os.getenv("ADMIN_USERNAME")
    return admin_username


def get_admin_password():
    admin_password = os.getenv("ADMIN_PASSWORD")
    return admin_password


def get_secret_key():
    jwt_secret = os.getenv("JWT_SECRET")
    return jwt_secret


def get_exp_time():
    exp_time = os.getenv("EXP_TIME")
    return exp_time


def get_ip():
    ip = os.getenv("IP")
    return ip


def get_port():
    PORT = os.getenv("PORT")
    return PORT
