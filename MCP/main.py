from mcp.server.fastmcp import FastMCP
import scan as scan
import Get_Net_Card as Get_Net_Card
import Hydra_MCP as Hydra
import logging
import os

# --- 配置日志 ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- 常量定义 ---
# 这些配置可能在您的FastMCP版本中不通过run()方法直接控制，
# 但保留它们可以用于文档或未来的版本兼容性。
DEFAULT_PORT = os.getenv("MCP_PORT", 8000)
DEFAULT_HOST = os.getenv("MCP_HOST", "0.0.0.0")
SERVER_NAME = "Nmap Scanner"

def create_mcp_server():
    logger.info(f"Initializing FastMCP server: '{SERVER_NAME}'")
    mcp = FastMCP(SERVER_NAME)

    tools_to_add = {
        scan.Fast_Scan: "快速扫描指定网卡",
        scan.Full_Scan: "全端口扫描指定网卡",
        scan.Fast_Scan_ip: "快速扫描指定IP",
        scan.Full_Scan_with_ip: "全端口扫描指定IP",
        scan.Advance_Scan: "高级扫描指定网卡",
        Get_Net_Card.get_Network_Cards: "获取所有网卡信息",
        Get_Net_Card.format_ip_card_name: "格式化指定网卡的IP+CIDR地址",
        Hydra.hydra_ssh: "执行SSH爆破",
        Hydra.hydra_ftp: "执行FTP爆破",
        Hydra.hydra_mysql: "执行MySQL爆破",       
        Hydra.hydra_postgre: "执行PostgreSQL爆破",
        Hydra.hydra_samba: "执行Samba爆破",
        Hydra.hydra_smtp: "执行SMTP爆破",
        Hydra.hydra_telnet: "执行Telnet爆破",
        Hydra.hydra_vnc: "执行VNC爆破",

    }

    for tool_func, description in tools_to_add.items():
        try:
            mcp.add_tool(tool_func, description)
            logger.info(f"Added tool: {tool_func.__name__} - {description}")
        except AttributeError:
            logger.error(f"Failed to add tool: {tool_func.__name__}. Make sure the function exists and is callable.")
        except Exception as e:
            logger.error(f"An unexpected error occurred while adding tool {tool_func.__name__}: {e}")

    return mcp

if __name__ == "__main__":
    logger.info("Starting Nmap Scanner FastMCP application...")
    mcp_app = create_mcp_server()

    # --- 核心改变：回到最初的调用方式 ---
    logger.info("Attempting to start FastMCP server using mcp.run('sse').")
    try:
        # 如果您的FastMCP版本不接受host和port，那么它应该只接受 transport
        mcp_app.run('sse')
    except Exception as e:
        logger.error(f"An error occurred while running FastMCP server: {e}", exc_info=True)
        # 如果这里再次出现 'address already in use'，那说明FastMCP在内部默认绑定了8000端口
        # 且没有提供外部参数来修改。这种情况下，您只能通过停止占用8000端口的进程来解决。
        if "Address already in use" in str(e):
             logger.error("It seems port 8000 is already in use by another process, and this FastMCP version might not allow specifying a custom port.")
             logger.error("Please stop any other applications using port 8000 or consider finding an older/newer FastMCP version that supports port configuration.")

    logger.info("Nmap Scanner FastMCP application has shut down.")