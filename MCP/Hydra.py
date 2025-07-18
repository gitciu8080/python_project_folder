import subprocess
import json
class Hydra:
    def __init__(self, ip, port, user, passwd):
        # 存储基本参数
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        
    def _build_command(self, service, vnc_mode=False):
        """构建Hydra命令的通用方法"""
        base_cmd = f"hydra -L {self.user} -P {self.passwd} {self.ip} -s {self.port}"
        if vnc_mode:
            # VNC模式只使用密码
            base_cmd = f"hydra -P {self.passwd} {self.ip} -s {self.port}"
        
        # 添加服务类型和XML输出选项
        return f"{base_cmd} {service} -o {service}_result.json -b json"

    def hydra_ssh(self):
        """执行SSH爆破"""
        cmd = self._build_command("ssh")
        print(cmd)
        subprocess.run(cmd, shell=True)
        return self.format_json("ssh_result.json")

    def hydra_samba(self):
        """执行Samba爆破"""
        cmd = self._build_command("smb")
        subprocess.run(cmd, shell=True)
        return self.format_json("samba_result.json")

    def hydra_ftp(self):
        """执行FTP爆破"""
        cmd = self._build_command("ftp")
        subprocess.run(cmd, shell=True)
        return self.format_json("ftp_result.json")

    def hydra_mysql(self):
        """执行MySQL爆破"""
        cmd = self._build_command("mysql")
        subprocess.run(cmd, shell=True)
        return self.format_json("mysql_result.json")

    def hydra_postgre(self):
        """执行PostgreSQL爆破"""
        cmd = self._build_command("postgres")
        subprocess.run(cmd, shell=True)
        return self.format_json("postgres_result.json")

    def hydra_vnc(self):
        """执行VNC爆破"""
        # VNC模式特殊处理
        cmd = f"hydra -P {self.passwd} {self.ip} -s {self.port} vnc -o vnc_result.json -b json"
        subprocess.run(cmd, shell=True)
        return self.format_json("vnc_result.json")

    def hydra_telnet(self):
        """执行Telnet爆破"""
        cmd = self._build_command("telnet")
        subprocess.run(cmd, shell=True)
        return self.format_json("telnet_result.json")

    def hydra_smtp(self):
        """执行SMTP爆破"""
        cmd = self._build_command("smtp")
        subprocess.run(cmd, shell=True)
        return self.format_json("smtp_result.json")
    def format_json(self, file_name):
        with open(file_name, "r") as f:
            try:
                data=json.load(f)
                status=data['success']
                user=data['results'][0]['login']
                password=data['results'][0]['password']
                return {"status": status, "user": user, "password": password}
            except json.JSONDecodeError:
                print("爆破结果解析失败，可能是文件格式错误或内容为空。")
        """格式化JSON数据"""
        

# 使用示例
# if __name__ == "__main__":
#     # 初始化参数
#     hydra = Hydra(ip='192.168.19.134', port=21, user='users.txt', passwd='password.txt')
#     # 执行FTP爆破
#     ftp_results = hydra.hydra_ftp()
#     print("FTP破解结果:", ftp_results)
    
