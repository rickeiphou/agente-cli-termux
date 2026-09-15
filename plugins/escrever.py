import os

SCHEMA = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Escreve conteudo em um arquivo. Use para criar scripts, HTML, CSS, JSON, etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Caminho do arquivo"},
                "content": {"type": "string", "description": "Conteudo completo do arquivo"}
            },
            "required": ["path", "content"]
        }
    }
}

def executar(args: dict) -> str:
    path = args.get("path")
    content = args.get("content")
    try:
        d = os.path.dirname(os.path.abspath(path))
        if d and not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"ok: {len(content)} bytes escritos em {path}"
    except Exception as e:
        return f"erro ao escrever {path}: {e}"
