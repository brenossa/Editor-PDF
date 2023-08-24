from pdf_editor import EditorPDF

# Uso do código
editor = EditorPDF("input.pdf", "destino.pdf")
editor.adicionar_texto("Esse pdf foi editado pelo EditorPDF", (50, 780))