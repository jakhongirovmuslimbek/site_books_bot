from environs import Env
import os

env = Env()
env.read_env()

API_TOKEN = env.str("API_TOKEN")
MYURL = env.str("MYURL")
MYTOKEN = env.str("MYTOKEN")