from reportlab.platypus import Paragraph, Table, Spacer, TableStyle
from reportlab.lib import colors


def create_header(datos, styles):
    return [
        Table([
            [
                Paragraph(f"<b>{datos['empresa_nombre']}</b>", styles["Heading1"]),
                Paragraph("<b>FACTURA</b>", styles["InvoiceTitle"])
            ],
            [
                Paragraph(datos["empresa_direccion"].replace('\n', '<br/>'), styles["Normal"]),
                ""
            ]
        ], colWidths=[250, 200], style=TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP')
        ])),
        Spacer(1, 12)
    ]


def create_addresses(datos, styles):
    return [
        Table([
            [
                Paragraph("<b>Facturar a</b><br/>" + datos["facturar_a"].replace('\n', '<br/>'), styles["Normal"]),
                Paragraph("<b>Enviar a</b><br/>" + datos["enviar_a"].replace('\n', '<br/>'), styles["Normal"]),
                Paragraph(
                    f"<b>Nº de factura:</b> {datos['numero_factura']}<br/>"
                    f"<b>Fecha:</b> {datos['fecha_factura']}<br/>"
                    f"<b>Nº de pedido:</b> {datos['numero_pedido']}<br/>"
                    f"<b>Fecha vencimiento:</b> {datos['fecha_vencimiento']}",
                    styles["Normal"]
                )
            ]
        ], colWidths=[200, 200, 100], style=TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP')
        ])),
        Spacer(1, 20)
    ]


def create_items_table(datos, styles):
    data = [
        [
            Paragraph("<b>FRUTA</b>", styles["Normal"]),
            Paragraph("<b>CANT.</b>", styles["Normal"]),
            Paragraph("<b>UNIDAD</b>", styles["Normal"]),
            Paragraph("<b>PRECIO UNITARIO</b>", styles["Normal"]),
            Paragraph("<b>IMPORTE</b>", styles["Normal"])
        ]
    ]

    # Filas de la tabla con los items
    for item in datos["items"]:
        data.append([
            item["descripcion"],  # Nombre de la fruta
            str(item["cantidad"]),  # Cantidad (1, 3, 0.5, etc.)
            item.get("unidad", "kg"),  # Unidad (kg o pieza)
            f"${item['precio_unitario']:.2f}",  # Precio unitario
            f"${item['importe']:.2f}"  # Importe total
        ])

    # Subtotal, IVA y Total al final
    data.append(["", "", "", "Subtotal", f"${datos['subtotal']:.2f}"])
    data.append(["", "", "", f"IVA 21.0%", f"${datos['iva']:.2f}"])
    data.append(["", "", "", Paragraph("<b>TOTAL</b>", styles["Normal"]), f"${datos['total']:.2f}"])

    return [
        Table(data, colWidths=[70, 50, 70, 120], style=TableStyle([
            ('GRID', (0, 0), (-1, -4), 0.5, colors.grey),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),
            ('ALIGN', (2, 1), (3, -1), 'RIGHT'),
            ('SPAN', (0, -3), (1, -3)),
            ('SPAN', (0, -2), (1, -2)),
            ('SPAN', (0, -1), (1, -1)),
            ('LINEABOVE', (0, -3), (-1, -3), 0.5, colors.black),
        ])),
        Spacer(1, 20),
        Spacer(1, 20)
    ]


def create_conditions(data, styles):
    text_conditions = data['condiciones'].replace('\n', '<br/>')
    return [
        Paragraph(
            f"<b>Condiciones y forma de pago</b><br/>{text_conditions}",
            styles["Normal"]
        )
    ]