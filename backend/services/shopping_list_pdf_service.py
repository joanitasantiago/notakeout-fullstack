from reportlab.pdfgen import canvas
from io import BytesIO

def generate_shopping_list_pdf(menu, items):
    """
    Gera um PDF da lista de compras de um menu.
    :param menu: objeto Menu com título e id
    :param items: lista de strings com nomes dos alimentos
    :return: bytes do PDF gerado
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle(f"Lista de Compras - {menu.title}")

    # Título
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 800, f"Lista de Compras - {menu.title}")

    # Conteúdo da lista
    pdf.setFont("Helvetica", 12)
    y = 770
    for item in items:
        pdf.drawString(70, y, f"- {item}")
        y -= 20

        # evitar sair da página:
        if y < 50:
            pdf.showPage()
            y = 800
            pdf.setFont("Helvetica", 12)

    pdf.save()
    buffer.seek(0)
    return buffer.read()
