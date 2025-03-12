from pdf_generator import generate_bill_pdf

DATOS_EJEMPLO = {
    "empresa_nombre": "Barragang Solutions.",
    "empresa_direccion": "Blvd. Tecnológico 150\nEx Ejido Chapultepec, CP 22780",
    "facturar_a": "Leda Villarreal\nVirgen Blanca 83\n08759 Burgos, Burgos",
    "enviar_a": "Leda Villarreal\nCercas Bajas 68\n47300 Cádiz, Cádiz",
    "numero_factura": "BG-001",
    "fecha_factura": "28/01/2025",
    "numero_pedido": "1730/2019",
    "fecha_vencimiento": "28/01/2019",
    "items": [
        {"cantidad": 1, "descripcion": "Talla pequeña traje de luces en rojo", "precio_unitario": 100.00, "importe": 100.00},
        {"cantidad": 2, "descripcion": "Muñ grande churumbito", "precio_unitario": 25.00, "importe": 50.00},
        {"cantidad": 3, "descripcion": "Equipaje de Fútbol", "precio_unitario": 5.00, "importe": 15.00}
    ],
    "subtotal": 165.00,
    "iva": 34.65,
    "total": 199.65,
    "condiciones": "El pago se realizará en un plazo de 5 días\n\nBanco Automatas\nIBAN: ES12 3456 7891\nSWIFT/BIC: ABCDESMMXXX"
}

if __name__ == "__main__":
    generate_bill_pdf("factura_ejemplo.pdf", DATOS_EJEMPLO)