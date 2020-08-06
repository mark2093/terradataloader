import json
import os


def read_credential_file():
    auth = {}
    auth_dict = {}
    env_dict = {}
    path1 = R"D:\TestingTools\fastteradata\.fastteradata"
   
    if os.path.exists(os.path.expanduser(path1)):
        auth = json.load(open(os.path.expanduser(path1)))
        auth_dict = auth["auth_dict"]
        env_dict = auth["env_dict"]
        
    return(auth, auth_dict, env_dict)

def load_db_info(env, custom_auth=False):
    print(env)
    auth, auth_dict, env_dict = read_credential_file()
  
    env_n = env_dict["__env__"][0]
    
    env_dsn = env_dict["__env__"][1]

    env_short = env_dict["__env__"][2]
  
    if not custom_auth:
        usr = auth_dict["__env1__"][0]
   
        passw = auth_dict["__env1__"][1]
  
    else:
        usr = auth_dict["__env1__"]
       
        passw = auth_dict["__env1__"]
       
    return(env_n, env_dsn, env_short, usr, passw)
    
    #Return the env name, dsn shorthands username and password. for our understanding#
