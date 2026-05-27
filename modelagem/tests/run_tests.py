import subprocess
import sys
from datetime import datetime
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

RUN_LOG = LOG_DIR / "run_tests.log"


testes = [
    "test_crud_client.py",
    "test_crud_prop.py",
    "test_crud_corretor.py",
    "test_crud_imovel.py",
    "test_crud_contrato.py",
]


def escrever_log(mensagem: str):
    with open(RUN_LOG, "a", encoding="utf-8") as arquivo:
        arquivo.write(mensagem + "\n")


inicio = datetime.now()

escrever_log("=" * 80)
escrever_log(f"Inicio da execucao dos testes: {inicio}")
escrever_log("=" * 80)


for teste in testes:
    mensagem_inicio = f"Executando {teste}..."
    print(mensagem_inicio)
    escrever_log(mensagem_inicio)

    resultado = subprocess.run(
        [sys.executable, teste],
        capture_output=True,
        text=True,
    )

    if resultado.returncode == 0:
        mensagem_sucesso = f"SUCESSO | {teste} executado com sucesso."
        print(mensagem_sucesso)
        escrever_log(mensagem_sucesso)
    else:
        mensagem_erro = f"ERRO | Falha ao executar {teste}."
        print(mensagem_erro)
        escrever_log(mensagem_erro)

        if resultado.stdout:
            escrever_log("STDOUT:")
            escrever_log(resultado.stdout)

        if resultado.stderr:
            escrever_log("STDERR:")
            escrever_log(resultado.stderr)

        sys.exit(resultado.returncode)


fim = datetime.now()
duracao = fim - inicio

escrever_log("=" * 80)
escrever_log(f"Fim da execucao dos testes: {fim}")
escrever_log(f"Duracao total: {duracao}")
escrever_log("Todos os testes foram executados com sucesso.")
escrever_log("=" * 80)

print("\nTodos os testes foram executados com sucesso.")
print(f"Log da execucao geral salvo em: {RUN_LOG}")