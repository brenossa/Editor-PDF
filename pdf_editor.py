from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class EditorPDF:
    def __init__(self, arquivo_original: str, arquivo_destino: str) -> None:
        self.arquivo_original = arquivo_original
        self.arquivo_destino = arquivo_destino

    def adicionar_texto(self, texto: str, posicao: tuple[int, int]) -> bool:
        pacote = io.BytesIO()
        can = canvas.Canvas(pacote, pagesize=letter)
        can.drawString(posicao[0], posicao[1], texto)
        can.save()

        pacote.seek(0)

        novo_pdf = PdfReader(pacote)
        pdf_existente = PdfReader(open(self.arquivo_original, "rb"))

        saida = PdfWriter()

        pagina = pdf_existente.pages[0]
        pagina.merge_page(novo_pdf.pages[0])
        saida.add_page(pagina)

        stream_saida = open(self.arquivo_destino, "wb")
        saida.write(stream_saida)
        stream_saida.close()

        return True
