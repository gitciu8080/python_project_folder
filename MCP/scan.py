import subprocess
import Get_Net_Card
import xml_to_json
def Fast_Scan(Card_name)->dict:
    ip=Get_Net_Card.format_ip_card_name(Card_name)
    shell =['nmap','-sS','-T5','-p', '21,22,25,53,80,135,139,443,445,3306,3389,8080','-sV','--version-intensity', '2','--min-parallelism', '100','--open','-oX', 'result.xml',ip]
    result=subprocess.run(shell,capture_output=True,text=True)
    result=xml_to_json.xml_to_list_Fast()
    return result

def Fast_Scan_ip(ip:str)->dict:
    shell =['nmap','-sS','-T5','-p', '21,22,25,53,80,135,139,443,445,3306,3389,8080','-sV','--version-intensity', '2','--min-parallelism', '100','--open','-oX', 'result.xml',ip]
    result=subprocess.run(shell,capture_output=True,text=True)
    result=xml_to_json.xml_to_list_Fast()
    return result
def Full_Scan(Card_name)->dict:
    ip=Get_Net_Card.format_ip_card_name(Card_name)
    shell = [
    'nmap', '-A', '-T5', '-p-', '--script',
    'http-title,http-enum,http-headers,http-methods,smb-os-discovery,smb-enum-shares,smb-enum-users,ftp-anon',
    ip, '-oX', 'result.xml']
    result=subprocess.run(shell,capture_output=True,text=True)
    # result=xml_to_json.xml_to_list_Full()
    return result

def Full_Scan_with_ip(ip:str)->dict:
    shell = [
    'nmap', '-A', '-T5', '-p-', '--script',
    'http-title,http-enum,http-headers,http-methods,smb-os-discovery,smb-enum-shares,smb-enum-users,ftp-anon',
    ip, '-oX', 'result.xml']
    result=subprocess.run(shell)
    result=xml_to_json.xml_to_list_Full()
    return result

def Advance_Scan(Card_name,shell)->str:
    ip=Get_Net_Card.format_ip_card_name(Card_name)
    result=subprocess.run(shell,capture_output=True,text=True)
    return result.stdout

print(Fast_Scan_ip('192.168.146.129'))