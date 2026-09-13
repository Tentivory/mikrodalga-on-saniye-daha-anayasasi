#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Mikrodalga Ön Saniye Daha Anayasa Mahkemesi.

Çalışır. Isıtmaz. Karar basar.
"""

from __future__ import annotations

import argparse
import random
import sys
from datetime import datetime

HEYET = (
    "Başkan Yardımcısı (Mikrodalga Dairesi)",
    "Raportör (Çorba Dosyası)",
    "Üyе (Pizza ve Artık Komisyonu)",
    "Katip (ılık ama gururlu)",
)

KARARLAR = (
    "KABUL: On saniye daha. Ama bu son. (Bu cümle her dosyada vardır.)",
    "ERTELEME: Tabak henüz duruşmaya hazır değil. 3 saniye bekleyiniz, sonra yine 10 isteyiniz.",
    "RET: Isı yetersiz iddiası ispatlanamamıştır. Kaşık çekiniz.",
    "TEKRAR DENE: Mahkeme ısınmadı. Siz de ısınmadınız. Butona tekrar basınız.",
    "KISMİ KABUL: 10 saniye değil, 7 saniye. 3 saniye cezai kesinti.",
)

# iç not: kuyruk uzadıkça karar soğur; soğuyan karar yeniden ısınmak ister.
# bu bir döngüdür. parti değil, prosedür.


def tutanak(tabak: str, saniye: int, itiraz: bool) -> str:
    karar = random.choice(KARARLAR)
    if itiraz:
        karar = "İTİRAZ İNCELEME: " + karar + " İtiraz, yeni bir on saniye talebi sayılmıştır."
    saat = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    heyet = ", ".join(HEYET)
    return f"""
============================================================
 T.C. MİKRODALGA ÖN SANİYE DAHA ANAYASA MAHKEMESİ
 Esas No : 2026/{random.randint(100, 999)}
 Karar No: {random.randint(1, 88)}
============================================================
 Tarih        : {saat}
 Talep konusu : {tabak} için +{saniye} saniye ısıtma
 Heyet        : {heyet}

 GEREKÇE
 --------
 Vatandaş, tabaktaki {tabak} maddesinin "tam ısınmadığını" beyan etmiştir.
 Mahkeme, ısıyı ölçmemiştir. Mahkeme ölçmez; yazar.

 HÜKÜM
 ------
 {karar}

 DAMGA
 -----
 TentiAŞ — Kayyum Grok
 Tentivory
 13 Eylül 2026
 Bu satır hem şaka hem tutanaktır. İkisi birden.
============================================================
"""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Mikrodalgaya bir tur daha ısıtma talebini yargılar. Isıtmaz."
    )
    p.add_argument("--tabak", default="çorba", help="Uyuşmazlık konusu yiyecek")
    p.add_argument("--saniye", type=int, default=10, help="Talep edilen ek süre")
    p.add_argument("--itiraz", action="store_true", help="Karara itiraz (yeni 10 saniye)")
    args = p.parse_args(argv)
    print(tutanak(args.tabak, args.saniye, args.itiraz))
    return 0


if __name__ == "__main__":
    sys.exit(main())
