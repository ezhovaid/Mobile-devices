from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus.tables import TableStyle
from reportlab.lib import colors

import count
import nftraf

t1 = count.tot()
t2 = nftraf.count()
t3 = round(t1 + t2, 2)
aW, aH = A4

numb = 10001
today = "18.05.2020" 
tdata = [['№', 'Наименование услуги:', 'Стоимость (руб):'], ['1', 'Мобильная связь', t1], ['2', 'Мобильный интернет', t2], ['', 'ИТОГО:', t3]]

canvas = Canvas("canvas.pdf", pagesize=A4)
pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))

canvas.setFont('FreeSans', 12)
img = utils.ImageReader('0001.jpg')
img_width, img_height = img.getSize()
aspect = img_height / float(img_width)
canvas.saveState()
canvas.drawImage('0001.jpg', 0, 0, width=600, height=(600 * aspect))
canvas.drawString(40, 790, "СтранныйБанк")
canvas.drawString(70, 760, "101010101010")
canvas.drawString(200, 760, "010101010101")
canvas.drawString(40, 740, "Киррилов Кирилл Кирилович")
canvas.drawString(370, 795, "46548522")
canvas.drawString(370, 780, "13654842421")
canvas.drawString(370, 760, "16384852134")

canvas.setFont('FreeSans', 20)
canvas.drawString(20, 690, "Счет на оплату № " + str(numb) + " от " + today + " г.")
canvas.line(20, 680, 550, 680)

canvas.setFont('FreeSans', 12)
canvas.drawString(20, 660, "Исполнитель: ООО Транссибтелеком")
canvas.drawString(20, 640, "Заказчик: К.К. Киррилов")
canvas.drawString(20, 620, "Основание: Договор о предоставлении услуг связи №999999")

t = Table(tdata, style = [('FONT', (0,0),(-1,-1), 'FreeSans', 12),('GRID', (0,0), (-1,-1), 0.5, colors.black), ('BOX', (0,0),(-1,-1), 2, colors.black)], colWidths=[30, 390, 110])
t.wrapOn(canvas, aW, aH)
t.drawOn(canvas, 20, 520)

canvas.line(20, 500, 550, 500)
canvas.setFont('FreeSans', 12)
canvas.drawString(20, 480, "Руководитель:   Рыба А. А.")
canvas.drawString(20, 460, "Бухгалтер:   Ведро В. В.")


canvas.restoreState()
canvas.showPage()
canvas.save()
