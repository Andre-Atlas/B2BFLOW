import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from logger import get_logger
from database import Database
from whatsapp import WhatsAppClient

logger = get_logger("Main")


def iniciar_automacao():

    Config.validar_configuracoes()

    db = Database()
    whatsapp = WhatsAppClient()
    template_msg = Config.MENSAGEM_TEMPLATE

    logger.info("Iniciando processo de disparo via WhatsApp...")
    contatos = db.buscar_contatos(limite=3)

    if not contatos:
        logger.warning("Nenhum contato encontrado ou banco está vazio. Finalizando.")
        return

    for contato in contatos:
        telefone = contato.get('telefone')
        nome = contato.get('nome', 'Cliente')

        mensagem_personalizada = template_msg.replace("<nome_contato>", nome)

        logger.info(f"Preparando envio para: {nome} ({telefone})")
        whatsapp.enviar_mensagem(telefone, mensagem_personalizada)

    logger.info("Processo finalizado!")


if __name__ == "__main__":
    try:
        iniciar_automacao()
    except KeyboardInterrupt:
        logger.warning("Execução cancelada pelo usuário.")
    except Exception as e:
        logger.critical(f"Falha fatal na aplicação: {e}")