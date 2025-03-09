from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm



def get_page_config():
    return {
        "pagesize": A4,
        "rightMargin": 20 * mm,
        "leftMargin": 20 * mm,
        "topMargin": 20 * mm,
        "bottomMargin": 20 * mm
    }


def create_styles():
    styles = getSampleStyleSheet()

    # Modificar estilos existentes
    styles["Normal"].spaceAfter = 6
    styles["Normal"].leading = 14

    styles["Heading1"].fontSize = 14
    styles["Heading1"].leading = 16
    styles["Heading1"].spaceAfter = 10

    # Crear estilos personalizados
    styles.add(ParagraphStyle(
        name='InvoiceTitle',
        parent=styles['Normal'],
        fontSize=16,
        leading=20,
        spaceAfter=10,
        alignment=1,
        textColor=colors.black
    ))

    return styles