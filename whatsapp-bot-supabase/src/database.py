from supabase import create_client, Client
from config import Config
from logger import get_logger

logger = get_logger("SupabaseDB")


class Database:
    def __init__(self):
        try:
            self.cliente: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
        except Exception as e:
            logger.error(f"Falha ao conectar no Supabase: {e}")
            raise e

    def buscar_contatos(self, limite: int = 3):
        """Busca contatos limitados pelo parâmetro limite."""
        try:
            # Busca do Supabase e limita para 3
            resposta = self.cliente.table("contatos") \
                .select("*") \
                .order('id') \
                .limit(limite) \
                .execute()

            contatos = resposta.data
            logger.info(f"Busca finalizada. Encontrados {len(contatos)} contatos no banco.")
            return contatos
        except Exception as e:
            logger.error(f"Erro ao buscar contatos no Supabase: {e}")
            return []