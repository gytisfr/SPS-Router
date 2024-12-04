import PIL
from PIL import ImageDraw, Image

curdir = "D:\\Ridgeway\\SPS\\Router\\"

cyrus = list(range(1, 16))
sterling = list(range(3200, 4701, 50))
oakland = list(range(950, 1701, 25))
palmer = [f"RA{el}" for el in range(1, 7)] + [f"RB{el}" for el in range(1, 7)] + [f"SA{el}" for el in range(1, 3)] + [f"SB{el}" for el in range(1, 3)]

async def main(houses):
    cyrush, sterlingh, oaklandh, palmerh = [], [], [], []
    images = {"Cyrus": None, "Oakland": None, "Palmer": None, "Sterling": None}

    for house in houses:
        if house in cyrus:
            cyrush.append(house)
        elif house in sterling:
            sterlingh.append(house)
        elif house in oakland:
            oaklandh.append(house)
        elif house in palmer:
            palmerh.append(house)

    with Image.open(f"{curdir}Cyrus.png").convert("RGBA") as img:
        image = ImageDraw.Draw(img)
        for el in cyrush:
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
            overlaydraw = ImageDraw.Draw(overlay)
            if el == 1:
                overlaydraw.line([(365, 179), (336, 185)], fill=(255, 0, 0, 90), width=10)
            elif el == 2:
                overlaydraw.line([(351, 225), (351, 252)], fill=(255, 0, 0, 90), width=10)
            elif el == 3:
                overlaydraw.line([(332, 234), (332, 260)], fill=(255, 0, 0, 90), width=10)
            elif el == 4:
                overlaydraw.line([(303, 185), (308, 211)], fill=(255, 0, 0, 90), width=10)
            elif el == 5:
                overlaydraw.line([(293, 172), (266, 177)], fill=(255, 0, 0, 90), width=10)
            elif el == 6:
                overlaydraw.line([(227, 175), (229, 201)], fill=(255, 0, 0, 90), width=10)
            elif el == 7:
                overlaydraw.line([(279, 190), (285, 216)], fill=(255, 0, 0, 90), width=10)
            elif el == 8:
                overlaydraw.line([(275, 242), (282, 267)], fill=(255, 0, 0, 90), width=10)
            elif el == 9:
                overlaydraw.line([(259, 228), (249, 252)], fill=(255, 0, 0, 90), width=10)
            elif el == 10:
                overlaydraw.line([(247, 251), (247, 275)], fill=(255, 0, 0, 90), width=10)
            elif el == 11:
                overlaydraw.line([(246, 282), (271, 292)], fill=(255, 0, 0, 90), width=10)
            elif el == 12:
                overlaydraw.line([(314, 329), (286, 337)], fill=(255, 0, 0, 90), width=10)
            elif el == 13:
                overlaydraw.line([(304, 268), (280, 282)], fill=(255, 0, 0, 90), width=10)
            elif el == 14:
                overlaydraw.line([(358, 308), (332, 312)], fill=(255, 0, 0, 90), width=10)
            elif el == 15:
                overlaydraw.line([(363, 269), (337, 269)], fill=(255, 0, 0, 90), width=10)
            img.alpha_composite(overlay)
        images["Cyrus"] = img

    with Image.open(f"{curdir}Oakland.png").convert("RGBA") as img:
        image = ImageDraw.Draw(img)
        for el in oaklandh:
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
            overlaydraw = ImageDraw.Draw(overlay)
            if el == 950:
                overlaydraw.line([(350, 377), (300, 377)], fill=(255, 0, 0, 90), width=15)
            elif el == 975:
                overlaydraw.line([(206, 403), (163, 379)], fill=(255, 0, 0, 90), width=15)
            elif el == 1000:
                overlaydraw.line([(261, 318), (212, 334)], fill=(255, 0, 0, 90), width=15)
            elif el == 1025:
                overlaydraw.line([(262, 282), (215, 280)], fill=(255, 0, 0, 90), width=15)
            elif el == 1050:
                overlaydraw.line([(185, 326), (157, 287)], fill=(255, 0, 0, 90), width=15)
            elif el == 1075:
                overlaydraw.line([(214, 286), (169, 270)], fill=(255, 0, 0, 90), width=15)
            elif el == 1100:
                overlaydraw.line([(166, 219), (121, 232)], fill=(255, 0, 0, 90), width=15)
            elif el == 1125:
                overlaydraw.line([(187, 181), (141, 192)], fill=(255, 0, 0, 90), width=15)
            elif el == 1150:
                overlaydraw.line([(211, 221), (165, 221)], fill=(255, 0, 0, 90), width=15)
            elif el == 1175:
                overlaydraw.line([(234, 186), (188, 186)], fill=(255, 0, 0, 90), width=15)
            elif el == 1200:
                overlaydraw.line([(256, 219), (210, 217)], fill=(255, 0, 0, 90), width=15)
            elif el == 1225:
                overlaydraw.line([(281, 189), (235, 189)], fill=(255, 0, 0, 90), width=15)
            elif el == 1250:
                overlaydraw.line([(269, 244), (269, 200)], fill=(255, 0, 0, 90), width=15)
            elif el == 1275:
                overlaydraw.line([(332, 239), (332, 284)], fill=(255, 0, 0, 90), width=15)
            elif el == 1300:
                overlaydraw.line([(274, 271), (268, 318)], fill=(255, 0, 0, 90), width=15)
            elif el == 1325:
                overlaydraw.line([(331, 284), (325, 331)], fill=(255, 0, 0, 90), width=15)
            elif el == 1350:
                overlaydraw.line([(313, 391), (292, 433)], fill=(255, 0, 0, 90), width=15)
            elif el == 1375:
                overlaydraw.line([(293, 434), (255, 463)], fill=(255, 0, 0, 90), width=15)
            elif el == 1400:
                overlaydraw.line([(295, 556), (247, 564)], fill=(255, 0, 0, 90), width=20)
            elif el == 1425:
                overlaydraw.line([(301, 470), (261, 495)], fill=(255, 0, 0, 90), width=15)
            elif el == 1450:
                overlaydraw.line([(343, 529), (302, 555)], fill=(255, 0, 0, 90), width=20)
            elif el == 1475:
                overlaydraw.line([(302, 471), (331, 435)], fill=(255, 0, 0, 90), width=15)
            elif el == 1500:
                overlaydraw.line([(383, 485), (351, 525)], fill=(255, 0, 0, 90), width=20)
            elif el == 1525:
                overlaydraw.line([(400, 435), (384, 481)], fill=(255, 0, 0, 90), width=20)
            elif el == 1550:
                overlaydraw.line([(340, 390), (329, 434)], fill=(255, 0, 0, 90), width=15)
            elif el == 1575:
                overlaydraw.line([(406, 385), (406, 431)], fill=(255, 0, 0, 90), width=20)
            elif el == 1600:
                overlaydraw.line([(410, 331), (410, 377)], fill=(255, 0, 0, 90), width=20)
            elif el == 1625:
                overlaydraw.line([(366, 275), (348, 319)], fill=(255, 0, 0, 90), width=15)
            elif el == 1650:
                overlaydraw.line([(429, 278), (416, 323)], fill=(255, 0, 0, 90), width=20)
            elif el == 1675:
                overlaydraw.line([(365, 229), (365, 274)], fill=(255, 0, 0, 90), width=15)
            elif el == 1700:
                overlaydraw.line([(431, 224), (431, 271)], fill=(255, 0, 0, 90), width=20)
            img.alpha_composite(overlay)
        images["Oakland"] = img
    
    with Image.open(f"{curdir}Palmer.png").convert("RGBA") as img:
        aptra, aptrb, apts = None, None, None
        image = ImageDraw.Draw(img)
        for el in palmerh:
            el = str(el)
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
            overlaydraw = ImageDraw.Draw(overlay)
            if el.startswith("RA"):
                if not aptra:
                    overlaydraw.line([(771, 513), (736, 564)], fill=(255, 0, 0, 90), width=27)
                    aptra = True
            elif el.startswith("RB"):
                if not aptrb:
                    overlaydraw.line([(713, 586), (662, 605)], fill=(255, 0, 0, 90), width=24)
                    aptrb = True
            elif el.startswith("S"):
                if not apts:
                    overlaydraw.line([(382, 478), (382, 554)], fill=(255, 0, 0, 90), width=30)
                    apts = True
            img.alpha_composite(overlay)
        images["Palmer"] = img

    with Image.open(f"{curdir}Sterling.png").convert("RGBA") as img:
        image = ImageDraw.Draw(img)
        for el in sterlingh:
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
            overlaydraw = ImageDraw.Draw(overlay)
            if el == 3200:
                overlaydraw.line([(167, 264), (125, 264)], fill=(255, 0, 0, 90), width=10)
            elif el == 3250:
                overlaydraw.line([(163, 240), (120, 240)], fill=(255, 0, 0, 90), width=10)
            elif el == 3300:
                overlaydraw.line([(140, 204), (167, 235)], fill=(255, 0, 0, 90), width=10)
            elif el == 3350:
                overlaydraw.line([(178, 229), (178, 187)], fill=(255, 0, 0, 90), width=10)
            elif el == 3400:
                overlaydraw.line([(232, 243), (187, 243)], fill=(255, 0, 0, 90), width=10)
            elif el == 3450:
                overlaydraw.line([(230, 263), (188, 258)], fill=(255, 0, 0, 90), width=10)
            elif el == 3500:
                overlaydraw.line([(182, 276), (225, 276)], fill=(255, 0, 0, 90), width=10)
            elif el == 3550:
                overlaydraw.line([(182, 298), (225, 298)], fill=(255, 0, 0, 90), width=10)
            elif el == 3600:
                overlaydraw.line([(182, 318), (225, 318)], fill=(255, 0, 0, 90), width=10)
            elif el == 3650:
                overlaydraw.line([(166, 325), (124, 320)], fill=(255, 0, 0, 90), width=10)
            elif el == 3700:
                overlaydraw.line([(183, 338), (226, 338)], fill=(255, 0, 0, 90), width=10)
            elif el == 3750:
                overlaydraw.line([(169, 342), (128, 342)], fill=(255, 0, 0, 90), width=10)
            elif el == 3800:
                overlaydraw.line([(184, 359), (228, 359)], fill=(255, 0, 0, 90), width=10)
            elif el == 3850:
                overlaydraw.line([(169, 363), (128, 363)], fill=(255, 0, 0, 90), width=10)
            elif el == 3900:
                overlaydraw.line([(187, 376), (233, 385)], fill=(255, 0, 0, 90), width=10)
            elif el == 3950:
                overlaydraw.line([(170, 382), (128, 382)], fill=(255, 0, 0, 90), width=10)
            elif el == 4000:
                overlaydraw.line([(171, 402), (129, 402)], fill=(255, 0, 0, 90), width=10)
            elif el == 4050:
                overlaydraw.line([(189, 413), (230, 413)], fill=(255, 0, 0, 90), width=10)
            elif el == 4100:
                overlaydraw.line([(189, 436), (231, 436)], fill=(255, 0, 0, 90), width=10)
            elif el == 4150:
                overlaydraw.line([(172, 435), (129, 435)], fill=(255, 0, 0, 90), width=10)
            elif el == 4200:
                overlaydraw.line([(194, 448), (234, 450)], fill=(255, 0, 0, 90), width=10)
            elif el == 4250:
                overlaydraw.line([(176, 459), (130, 459)], fill=(255, 0, 0, 90), width=10)
            elif el == 4300:
                overlaydraw.line([(191, 465), (231, 465)], fill=(255, 0, 0, 90), width=10)
            elif el == 4350:
                overlaydraw.line([(174, 473), (129, 473)], fill=(255, 0, 0, 90), width=10)
            elif el == 4400:
                overlaydraw.line([(189, 488), (231, 488)], fill=(255, 0, 0, 90), width=10)
            elif el == 4450:
                overlaydraw.line([(175, 488), (129, 488)], fill=(255, 0, 0, 90), width=10)
            elif el == 4500:
                overlaydraw.line([(186, 509), (228, 509)], fill=(255, 0, 0, 90), width=10)
            elif el == 4550:
                overlaydraw.line([(172, 508), (126, 508)], fill=(255, 0, 0, 90), width=10)
            elif el == 4600:
                overlaydraw.line([(185, 527), (228, 533)], fill=(255, 0, 0, 90), width=10)
            elif el == 4650:
                overlaydraw.line([(171, 527), (126, 527)], fill=(255, 0, 0, 90), width=10)
            elif el == 4700:
                overlaydraw.line([(128, 551), (172, 547)], fill=(255, 0, 0, 90), width=10)
            img.alpha_composite(overlay)
        images["Sterling"] = img
    
    return images