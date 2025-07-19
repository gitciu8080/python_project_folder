from lxml import etree

def xml_to_list_Fast():
        xml=etree.parse('result.xml')
        host=xml.xpath('//nmaprun/host')
        # ip_list=[]
        result_list=[]
        # print(host)
        for host in host:
            ip_list=[]
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
                    # print(muban)
            result_list.append({port_ip:ip_list})
            # print(list_end)
        return result_list
def xml_to_list_Full():
    xml=etree.parse('result.xml')
    host=xml.xpath('//nmaprun/host')
    
    result_list=[]
    # print(host)
    for host in host:
        ip_list=[]
        # print(host)
        
        port_ip=host.xpath('address[@addrtype="ipv4"]/@addr')[0]
        #print(port_ip)
        Xpath_port=host.xpath('ports/port')
        for Xpath_port in Xpath_port:
            port_state=Xpath_port.xpath('state/@state')[0]
            service=Xpath_port.xpath('service/@name')
            port=Xpath_port.xpath('@portid')[0]
            elem_list=[]
            try:
                script=Xpath_port.xpath('script/elem')
                
                for script in script:
                    elem_muban=({script.xpath('@key')[0]:script.xpath('text()')[0]})
                    elem_list.append(elem_muban)
            except:
                pass
            # print(port_ip,port_state,service,port,script)
        # for port_state,service,port in zip(port_state,service,port):

            if port_state=='open':
                muban={'ip':port_ip,'port':port,'service':service,'port_state':port_state,'elem':elem_list}
                
                # muban={,'ip_info':muban}
                ip_list.append(muban)
        result_list.append({port_ip:ip_list})
        # a=ip_list
        #print(a)
        # result_list.append(a)
        #print(a)
    return result_list

# print(xml_to_list_Fast())