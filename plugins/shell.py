import os
import subprocess

SCHEMA = {
    "type": "function",
    "function": {
        "name": "run_shell",
        "description": (
            "Executa comando shell no Termux (ls, cat, grep, curl, python, etc). "
            "Possui limite de tempo para evitar processos travados."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "Comando shell a executar"
                }
            },
            "required": ["command"]
        }
    }
}

def executar(args: dict) -> str:
    comando = args.get("command") or ""

    if not comando.strip():
        return "erro: comando vazio"

    tmp = os.path.join(
        os.environ.get("TMPDIR", "/tmp"),
        "_agent_out.txt"
    )

    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            errors="replace",
            timeout=15
        )

        out = resultado.stdout[:6000]

        if not out.strip():
            out = "<sem saida>"

        return f"exit={resultado.returncode}\n{out}"

    except subprocess.TimeoutExpired as e:
        out = e.stdout or ""

        if isinstance(out, bytes):
            out = out.decode("utf-8", errors="replace")

        out = out[:6000]

        return (
            "exit=124\n"
            "ERRO: comando excedeu o limite de 15 segundos "
            "e foi interrompido.\n"
            f"{out}"
        )

    except Exception as e:
        return f"erro executando comando: {type(e).__name__}: {e}"