import Hydra

def hydra_ssh(ip, port, user:list[str] = None, passwd:list[str] = None)->dict:
    """执行SSH爆破"""
    hydra_instance = Hydra.Hydra(ip, port, user, passwd)
    return hydra_instance.hydra_ssh()

def hydra_ftp(ip, port, user:list[str] = None, passwd:list[str] = None)->dict:
    """执行FTP爆破"""
    hydra_instance = Hydra.Hydra(ip, port, user, passwd)
    return hydra_instance.hydra_ftp()

def hydra_mysql(ip, port, user:list[str] = None, passwd:list[str] = None)->dict:
    """执行MYSQL爆破"""
    hydra_instance = Hydra.Hydra(ip, port, user, passwd)
    return hydra_instance.hydra_mysql()

def hydra_postgre(ip, port, user:list[str] = None, passwd:list[str] = None)->dict:
    """执行POSTGRESQL爆破"""
    hydra_instance = Hydra.Hydra(ip, port, user, passwd)
    return hydra_instance.hydra_postgre()

def hydra_samba(ip, port, user:list[str] = None, passwd:list[str] = None)->dict:
    """执行SAMBA爆破"""
    hydra_instance = Hydra.Hydra(ip, port, user, passwd)
    return hydra_instance.hydra_samba()

def hydra_vnc(ip, port, passwd:list[str] = None)->dict:
    """执行VNC爆破"""
    hydra_instance = Hydra.Hydra(ip, port, None, passwd)  # VNC只需要密码
    return hydra_instance.hydra_vnc()

def hydra_telnet(ip, port, user:list[str] = None, passwd:list[str] = None)->dict:
    """执行Telnet爆破"""
    hydra_instance = Hydra.Hydra(ip, port, user, passwd)
    return hydra_instance.hydra_telnet()

def hydra_smtp(ip, port, user:list[str] = None, passwd:list[str] = None)->dict:
    """执行SMTP爆破"""
    hydra_instance = Hydra.Hydra(ip, port, user, passwd)
    return hydra_instance.hydra_smtp()

def hydra(ip, port,shell)->dict:


print(hydra_ftp('192.168.19.134',21,['admin','1234','msfadmin'],['admin','1234','msfadmin']))