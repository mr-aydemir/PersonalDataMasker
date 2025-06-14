# data_masker/patterns.py
import re

# IBAN (Türkiye)
# TR ile başlar, ardından 2 kontrol basamağı ve 22 haneli temel hesap numarası gelir.
# Toplam 26 alfanümerik karakter (TR + 24 rakam).
# Aralarda boşluk olabilir.
IBAN_PATTERN = re.compile(r"TR\s?[0-9]{2}\s?[0-9]{4}\s?[0-9]{4}\s?[0-9]{4}\s?[0-9]{4}\s?[0-9]{4}\s?[0-9]{2}")


# Gelecekte eklenecek diğer desenler# T.C. Kimlik Numarası için regex
# 11 haneli, ilk hanesi 0 olmayan sayılar
TC_KIMLIK_NO_PATTERN = re.compile(r"\b[1-9][0-9]{10}\b")


# Telefon Numarası (Türkiye)
# Çeşitli formatları destekler: +90 5xx xxx xx xx, 05xx xxx xx xx, 5xx xxx xx xx vb.
PHONE_NUMBER_PATTERN = re.compile(r"\b(?:\+?90\s*?)?(?:0?5\d{2})\s*?\d{3}\s*?\d{2}\s*?\d{2}\b")


# Diğer desenler buraya eklenebilir.
# Örneğin:
# TC_KIMLIK_NO_PATTERN = re.compile(r"^[1-9]{1}[0-9]{9}[02468]{1}$")
# TC_KIMLIK_NO_MASK = "[TCKN GİZLENDİ]"