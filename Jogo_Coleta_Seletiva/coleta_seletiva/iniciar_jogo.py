"""
Servidor local para o Jogo Coleta Seletiva.
Permite jogar em tela cheia no PC ou no celular pela mesma rede Wi-Fi!
Não precisa de Streamlit ou pacotes externos (apenas Python padrão).
"""

import http.server
import os
import socket
import socketserver
import sys
import webbrowser

PORTA = 8000
PASTA_JOGO = os.path.dirname(os.path.abspath(__file__))


def obter_ip_local():
    """Descobre o IP local do computador na rede Wi-Fi/Ethernet."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Não precisa conectar de verdade à internet, apenas determina a interface local
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


class RequisicaoHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PASTA_JOGO, **kwargs)

    def end_headers(self):
        # Desabilitar cache para refletir mudanças imediatamente
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        # Reduz logs desnecessários no console
        pass


def main():
    ip_local = obter_ip_local()
    porta_usada = PORTA

    # Se a porta 8000 estiver ocupada, tenta as próximas
    for p in range(PORTA, PORTA + 20):
        try:
            with socketserver.TCPServer(("", p), RequisicaoHandler) as httpd:
                porta_usada = p
                break
        except OSError:
            continue

    url_local = f"http://localhost:{porta_usada}"
    url_celular = f"http://{ip_local}:{porta_usada}"

    print("=" * 60)
    print(" ♻️  JOGO COLETA SELETIVA - MODO TELA CHEIA & MOBILE")
    print("=" * 60)
    print(f"\n💻 Jogar no PC (abre automaticamente):\n   -> {url_local}")
    print(f"\n📱 Jogar no CELULAR (na mesma rede Wi-Fi):\n   -> {url_celular}")
    print("\n💡 Dica: no celular, você pode tocar no botão [⛶] para")
    print("   entrar em TELA CHEIA e jogar sem as barras do navegador!")
    print("\n   Pressione Ctrl + C no terminal para encerrar.")
    print("=" * 60 + "\n")

    # Abre no navegador do PC automaticamente
    webbrowser.open(url_local)

    try:
        with socketserver.TCPServer(("", porta_usada), RequisicaoHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado. Bom jogo!")
        sys.exit(0)


if __name__ == "__main__":
    main()
