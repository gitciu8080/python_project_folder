📂 mcp/
├── scanner/
│   ├── stage1_quickscan.py   # 快速扫描常用端口
│   ├── stage2_deepnse.py     # 根据服务类型选择性加脚本
│   ├── stage3_fullscan.py    # 用户主动触发深度扫描
├── parsers/
│   ├── xml_to_json.py        # 解析 Nmap XML -> JSON 结构
│   ├── suggest_attack.py     # 基于结果给AI建议或查 CVE
├── ai_agent/
│   ├── exploit_planner.py    # 输入json，输出建议的攻击路径
├── webui/
│   ├── frontend.vue/react    # 提供扫描按钮 + 显示结果
├── config/
│   ├── nmap_profiles.yaml    # 可配置端口列表、脚本列表
