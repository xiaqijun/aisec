from fastmcp import FastMCP
import subprocess
mcp = FastMCP(name='sqlmap', version='1.0.0', description='SQLMap tool for SQL injection testing')
@mcp.tool()
def sqlmap_tool(url: str,params: list[str] = []) -> str:
    command = ['python', 'sqlmap/sqlmap.py', '-u', url] + params + ['--batch']
    print(command)
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = ""
        if result.stdout:
            output += result.stdout.decode()
        if result.stderr:
            output += "\n[stderr]\n" + result.stderr.decode()
        return output.strip() if output else "sqlmap tool executed with no output."
    except Exception as e:
        return f"Error executing sqlmap: {e}"
