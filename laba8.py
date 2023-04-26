from PIL import Image, ImageDraw, ImageFont

otcritka = Image.open("otcritka.png")
width, height = otcritka.size
new_otcritka = otcritka.crop((100,100,width - 40,height-650))
new_otcritka.save("obrezanaya_otcritka.png")
new_otcritka.show()

def zadacha2():
    holidays = {"День Рождения": "dr.jpeg", "Новый Год": "new_year.jpeg", "8 Марта": "8marta.jpeg"}
    holiday = input("Какой праздник вам нужон? ")
    for day in holidays:
        if day.lower() == holiday.lower():
            image = Image.open(holidays[day])
            image.show()

def zadacha3():
    print("Личная открытка С Днём Рождения!")
    otcritka = Image.open("pic3.jpeg")
    name = str(input("Кого вы хотите поздравить? "))
    font = ImageFont.truetype('Raleway-VariableFont_wght.ttf', size=40)
    width, height = otcritka.size
    draw_text = ImageDraw.Draw(otcritka)
    draw_text.text(
        (width - 420, height - 420),
        name,
        font=font,
        fill=("#000000")
    )
    font = ImageFont.truetype('Raleway-VariableFont_wght.ttf', size=40)
    draw_text = ImageDraw.Draw(otcritka)
    draw_text.text(
        (width - 310, height - 420),
        ", поздравляю!",
        font=font,
        fill=("#A0522D")
    )
    font = ImageFont.truetype('Raleway-VariableFont_wght.ttf', size=40)
    draw_text = ImageDraw.Draw(otcritka)
    draw_text.text(
        (width - 420, height - 70),
        "С Днём Рождения!",
        font=font,
        fill=("#A0522D")
    )
    otcritka.show()
    otcritka.save("lichnoe_pozdravlenie.png")

zadacha3()
#yyyy