SCHEMA = {
    "type": "function",
    "function": {
        "name": "edit_file",
        "description": "Substitui um trecho exato de um arquivo por outro. Cirurgico.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Caminho do arquivo"},
                "old": {"type": "string", "description": "Trecho exato a ser substituido"},
                "new": {"type": "string", "description": "Novo trecho"}
            },
            "required": ["path", "old", "new"]
        }
    }
}

def executar(args: dict) -> str:
    path = args.get("path")
    old = args.get("old")
    new = args.get("new")
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if old not in content:
            return f"erro: trecho nao encontrado em {path}"
        count = content.count(old)
        if count > 1:
            return f"erro: trecho aparece {count}x em {path}. seja mais especifico."
        content = content.replace(old, new, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"ok: patch aplicado em {path} ({len(old)} -> {len(new)} chars)"
    except Exception as e:
        return f"erro ao editar {path}: {e}"
