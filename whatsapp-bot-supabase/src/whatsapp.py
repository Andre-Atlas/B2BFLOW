import requests
from config import Config
from logger import get_logger

logger = get_logger("Z-API")


class WhatsAppClient:
    def __init__(self):
        # A url de envio de texto segue o padrão da documentação oficial da Z-API
        self.url = f"https://api.z-api.io/instances/{Config.ZAPI_INSTANCE_ID}/token/{Config.ZAPI_INSTANCE_TOKEN}/send-text"

    def enviar_mensagem(self, telefone: str, mensagem: str) -> bool:
        """Envia a mensagem chamando o endpoint do Z-API."""
        payload = {
            "phone": telefone,
            "message": mensagem
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()  # Lança erro se status >= 400
            logger.info(f"Sucesso: Mensagem enviada para {telefone}")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar mensagem para {telefone}. Motivo: {e}")
            if response is not None:
                logger.error(f"Resposta Z-API: {response.text}")
            return False