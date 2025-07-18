"""
模块：获取网卡信息
"""
import subprocess,json
def get_Network_Cards()->dict:
        shell=['ip','-j','addr']
        run=subprocess.run(shell,capture_output=True, text=True).stdout
        result=json.loads(run)
        result_list=[]
        for result in result:
            ip=result['addr_info'][0]
            muban={'Net_name':result['ifname'],'ip':ip['local'],'perfixlen':str(ip['prefixlen'])}
            result_list.append(muban)
        return result_list

def select_network_card(Card_name):
        ifconfig=get_Network_Cards()
        for ifconfig in ifconfig:
            try:
                if ifconfig['Net_name']==Card_name:
                    return ifconfig
            except:
                pass

def format_ip(network_card_info)->str:
    ip=network_card_info['ip']
    ip_parts=ip.split('.')
    ip_parts[-1]='0'
    network_card_info['ip']='.'.join(ip_parts)
    ip=f'{network_card_info['ip']}/{network_card_info['perfixlen']}'
    return ip
#使用ethX获取IP
def format_ip_card_name(Card_name)->str:
    network_card_info=select_network_card(Card_name)
    return format_ip(network_card_info)
