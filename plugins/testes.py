import os

SCHEMA = {
    "type": "function",
    "function": {
        "name": "run_tests",
        "description": "Executa um comando de teste. Retorna PASSOU ou FALHOU.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "Comando de teste a executar"}
            },
            "required": ["command"]
        }
    }
}

def executar(args: dict) -> str:
    command = args.get("command")
    tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), "_test_out.txt")
    full = f"({command}) > {tmp} 2>&1"
    code = os.system(full)
    try:
        with open(tmp, "r", errors="replace") as f:
            out = f.read()[:6000]
    except Exception as e:
        out = f"<erro lendo saida: {e}>"
    if not out.strip():
        out = "<sem saida>"
    status = "PASSOU" if code == 0 else "FALHOU"
    return f"status={status} (exit={code})\n{out}"
