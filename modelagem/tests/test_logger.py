import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "testes.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
)
def log_info(message:str):
    logging.info(message)
def log_sucess(message:str):
    logging.info(f"SUCESSO | {message}")    
def log_error(message:str):
    logging.error(message)    