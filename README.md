# ZoomeyePro 资产管理接口

本项目基于 FastMCP 框架，封装了对 ZoomeyePro 平台的资产查询与探测任务下发接口，便于自动化资产管理与安全检测。

## 功能简介

- **资产查询**：支持多条件筛选和分页，查询资产列表。
- **探测任务下发**：支持自定义目标、端口、协议等参数，批量下发资产探测任务。

## 主要文件

- `server.py`：核心接口实现，包含资产查询与探测任务下发方法。
- `requirements.txt`：依赖库列表。

## 快速开始

1. 配置 `config.py`，填写 ZoomeyePro 平台的账号信息和 IP。
2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```
3. 运行接口服务或在其他项目中导入使用。

## 接口说明

### 1. 资产查询

```python
query_assets(
    site_ids: list = None,
    search_name: str = None,
    ...
    page: int = 1,
    pageSize: int = 20
)
```
- 支持多种筛选条件，返回资产列表。

### 2. 探测任务下发

```python
create_detection_task(
    name: str,
    target: list,
    ports: list = None,
    ...
    priority: str = "middle"
)
```
- 支持自定义探测参数，批量下发任务。

## 注意事项

- 需保证 ZoomeyePro 平台账号信息正确。
- 接口请求均为 HTTPS，证书校验已关闭（`verify=False`），如有安全要求请自行调整。

---

如需更详细的接口参数说明或示例，请参考 `server.py` 源码。
