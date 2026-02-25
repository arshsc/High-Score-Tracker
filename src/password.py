from helper import *
import bcrypt

def pass_encoder(username, password):
    password = b"{password}"
    username = bcrypt.gensalt()
    return bcrypt.hashpw(password, username)

print(pass_encoder("BobertThe4th", "3gG4s"))

def pass_checker():
    
