from reportlab.platypus import SimpleDocTemplate
from utils.func.bill_styles import get_page_config, create_styles
from utils.func.bill_components import (create_header, create_addresses, create_items_table,
                                                           create_conditions)


def generate_bill_pdf(file_name, bill_data):
    config = get_page_config()
    doc = SimpleDocTemplate(file_name, **config)
    styles = create_styles()

    story = []
    story += create_header(bill_data, styles)
    story += create_addresses(bill_data, styles)
    story += create_items_table(bill_data, styles)
    story += create_conditions(bill_data, styles)

    doc.build(story)
