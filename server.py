from fastmcp import FastMCP
from config import USERNAME,PASSWORD,Zoomeye_IP
import requests
import json
mcp = FastMCP(name='ZoomeyePro', version='1.0.0')
def zoomeye_login():
    data={
        'username':USERNAME,
        'password':PASSWORD
    }
    url = "https://{}/api/v4/external/login".format(Zoomeye_IP)
    response = requests.post(url=url, json=data, verify=False)
    if response.status_code != 200:
        print("登录失败，状态码:", response.status_code)
        return None
    token=json.loads(response.text)
    return token

@mcp.tool()
def query_assets(
    site_ids: list = None,
    search_name: str = None,
    search_ip: str = None,
    search_url: str = None,
    search_mac: str = None,
    search_assetCategory: str = None,
    search_title: str = None,
    search_os: str = None,
    search_port: str = None,
    search_service: str = None,
    search_component: str = None,
    search_tag: str = None,
    search_waf: str = None,
    search_organization: str = None,
    search_vul: str = None,
    search_vulLevel: str = None,
    search_origin: str = None,
    page: int = 1,
    pageSize: int = 20
):
    """
    查询资产列表，支持多条件筛选和分页。
    """
    token = zoomeye_login()
    if not token:
        return {"error": "登录失败"}
    headers = {"Authorization": f"JWT {token['access_token']}"}
    params = {
        "page": page,
        "pageSize": pageSize
    }
    # 添加所有非空参数
    if site_ids:
        for sid in site_ids:
            params.setdefault("site_ids", []).append(sid)
    for k, v in locals().items():
        if v and k not in ["site_ids", "page", "pageSize", "token", "headers", "params"]:
            params[k] = v
    url = f"https://{Zoomeye_IP}/api/v4/external/siteList"
    response = requests.get(url, headers=headers, params=params, verify=False)
    if response.status_code != 200:
        return {"error": f"查询失败，状态码: {response.status_code}"}
    return response.json()