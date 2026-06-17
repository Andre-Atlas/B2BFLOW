import os
from dotenv import load_dotenv
from logger import get_logger

logger = get_logger("Config")

load_dotenv()


class Config:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
    ZAPI_INSTANCE_TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")

    MENSAGEM_TEMPLATE = os.getenv("MENSAGEM_TEMPLATE", "Olá <nome_contato>, teste!")

    @classmethod
    def validar_configuracoes(cls):
        missing = []
        if not cls.SUPABASE_URL: missing.append("SUPABASE_URL")
        if not cls.SUPABASE_KEY: missing.append("SUPABASE_KEY")
        if not cls.ZAPI_INSTANCE_ID: missing.append("ZAPI_INSTANCE_ID")
        if not cls.ZAPI_INSTANCE_TOKEN: missing.append("ZAPI_INSTANCE_TOKEN")

        if missing:
            logger.error(f"Faltam as seguintes variáveis no .env: {', '.join(missing)}")
            raise EnvironmentError("Variáveis de ambiente ausentes. Configure o arquivo .env.")