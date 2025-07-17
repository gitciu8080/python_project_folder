import subprocess
import Scanner.Get_Net_Card as Get_Net_Card
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'XML_to_JSON')))
import xml_to_json
def Fast_Scan(Card_name)->dict:
    ip=Get_Net_Card.format_ip_card_name(Card_name)
    shell =['nmap','-sS','-T5','-p', '21,22,25,53,80,135,139,443,445,3306,3389,8080','-sV','--version-intensity', '2','--min-parallelism', '100','--open','-oX', 'MCP/result.xml',ip]
    result=subprocess.run(shell,capture_output=True,text=True)
    result=xml_to_json.xml_to_list_Fast()
    return result
def Full_Scan(Card_name)->dict:
    ip=Get_Net_Card.format_ip_card_name(Card_name)
    shell = [
    'nmap', '-A', '-T4', '-p-', '--script',
    'http-title,http-enum,http-headers,http-methods,smb-os-discovery,smb-enum-shares,smb-enum-users,ftp-anon',
    ip, '-oX', 'MCP/result.xml']
    result=subprocess.run(shell,capture_output=True,text=True)
    result=xml_to_json.xml_to_list_Full()
    return result

def Advance_Scan(Card_name,shell:list[str] = None)->str:
    ip=Get_Net_Card.format_ip_card_name(Card_name)
    result=subprocess.run(shell,capture_output=True,text=True)
    return result.stdout

