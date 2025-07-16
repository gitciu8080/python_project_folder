import Get_Net_Card,subprocess,json
from lxml import etree
def Fast_Scan(Card_name):
    ip=Get_Net_Card.format_ip_card_name(Card_name)
    shell = [
    'nmap', '-sS', '-T4', '-p', '21,22,23,25,53,80,110,135,139,143,443,445,3306,3389,8080',
    '-sV', '-O', '--version-intensity', '5',
    '-oX', 'MCP/result.xml', ip]
    result=subprocess.run(shell)
    return result

print(Fast_Scan('eth0'))