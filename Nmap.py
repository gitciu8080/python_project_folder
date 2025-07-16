import subprocess,json
from lxml import etree
class Nmap:
    # # 手动选择网卡
    # def select_ipconfig():
    #     shell=['ip','-j','addr']
    #     run=subprocess.run(shell,capture_output=True, text=True).stdout
    #     result=json.loads(run)
    #     result_list=[]
    #     for result in result:
    #         ip=result['addr_info'][0]
    #         muban={'Net_name':result['ifname'],'ip':ip['local'],'perfixlen':ip['prefixlen']}
    #         result_list.append(muban)
    #     for index, ip in enumerate(result_list, 1):  # 从1开始编号
    #         print(f"{index}. {ip['Net_name']} - {ip['ip']}")
        
    #     try:
    #         select = int(input('输入数字：')) - 1  # 转换为0-based索引
    #         if select < 0 or select >= len(result_list):
    #             raise ValueError("输入超出范围")
    #         return result_list[select]
    #     except ValueError:
    #         print('falied')
    # #获取配置
    # def get_Network_Cards():
    #     shell=['ip','-j','addr']
    #     run=subprocess.run(shell,capture_output=True, text=True).stdout
    #     result=json.loads(run)
    #     result_list=[]
    #     for result in result:
    #         ip=result['addr_info'][0]
    #         muban={'Net_name':result['ifname'],'ip':ip['local'],'perfixlen':ip['prefixlen']}
    #         result_list.append(muban)
    #     return result_list
    # # 获取网卡信息
    # def select_network_card(Card_name):
    #     ifconfig=Nmap.get_Network_Cards()
    #     for ifconfig in ifconfig:
    #         try:
    #             if ifconfig['Net_name']==Card_name:
    #                 return ifconfig
    #         except:
    #             pass
    #  # 格式化IP地址           
    # def format_ip(network_card_info):
    #     ip=network_card_info['ip']
    #     ip_parts=ip.split('.')
    #     ip_parts[-1]='0'
    #     network_card_info['ip']='.'.join(ip_parts)
    #     ip=f'{network_card_info['ip']}/{network_card_info['perfixlen']}'
    #     return ip
    # #使用ethX获取IP
    # def format_ip_card_name(Card_name):
    #     network_card_info=Nmap.select_network_card(Card_name)
    #     return Nmap.format_ip(network_card_info)
    #格式化XML
    # def xml_to_list():
    #     xml=etree.parse('result.xml')
    #     host=xml.xpath('//nmaprun/host')
    #     ip_list=[]
    #     # print(host)
    #     for host in host:
    #         # print(host)
    #         port_ip=host.xpath('address[@addrtype="ipv4"]/@addr')[0]
    #         port_state=host.xpath('ports/port/state/@state')
    #         service=host.xpath('ports/port/service/@name')
    #         port=host.xpath('ports/port/@portid')
    #         for port_state,service,port in zip(port_state,service,port):

    #             if port_state=='open':
    #                 muban={'ip':port_ip,'port':port,'service':service,'port_state':port_state}
    #                 # muban={,'ip_info':muban}
    #                 ip_list.append(muban)
    #     return ip_list
    
    def xml_to_list():
        xml=etree.parse('result.xml')
        host=xml.xpath('//nmaprun/host')
        ip_list=[]
        # print(host)
        for host in host:
            # print(host)
            port_ip=host.xpath('address[@addrtype="ipv4"]/@addr')[0]
            port_state=host.xpath('ports/port/state/@state')
            service=host.xpath('ports/port/service/@name')
            port=host.xpath('ports/port/@portid')
            for port_state,service,port in zip(port_state,service,port):

                if port_state=='open':
                    muban={'port':port,'service':service,'port_state':port_state}
                    # muban={,'ip_info':muban}
                    ip_list.append(muban)
            a={port_ip:ip_list}
        return a
    #扫描ip
    def scan_ip(ip):
        shell = ['nmap', '-A', '-T4', '--script','http-title,http-enum,http-headers,http-methods,smb-os-discovery,smb-enum-shares,smb-enum-users,ftp-anon',ip, '-oX', 'result.xml']
        result=subprocess.run(shell)
    #xml转list
    def xml_to_list_scan(ip):
        Nmap.scan_ip(ip)
        return Nmap.xml_to_list()

    def Auto_scan(Card_name)->str:
        """
        自动扫描指定网卡的IP地址
        :param Card_name: 网卡名称
        :return: 扫描结果列表
        """
        ip = Nmap.format_ip_card_name(Card_name)
        return Nmap.xml_to_list_scan(ip)
    

print(Nmap.Auto_scan('eth0'))  # 替换为实际的网卡名称