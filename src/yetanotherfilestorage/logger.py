from pathlib import Path

from loguru import logger


LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)


def get_logger(module_file: str):
    filename = Path(module_file).name

    logger.add(
        sink=LOGS_DIR / f"{filename}.log",
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{message}</cyan>"
        ),
        filter=lambda record: (record["extra"].get("module") == filename),
        rotation="10 MB",
        retention="7 days",
        encoding="utf-8",
    )

    return logger.bind(module=filename)
