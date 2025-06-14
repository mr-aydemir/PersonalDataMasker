# main.py
from data_masker.masker import mask_text
import spacy

def main():
    # spaCy modelini yükle (main.py için özel)
    try:
        nlp = spacy.load("tr_core_news_trf")
        print("main.py: spaCy modeli 'tr_core_news_trf' başarıyla yüklendi.")
    except OSError:
        print("main.py: spaCy modeli 'tr_core_news_trf' bulunamadı. Lütfen 'python -m spacy download tr_core_news_trf' komutuyla indirin veya .whl dosyasını kurun.")
        nlp = None
        return # Model yoksa devam etme

    sample_text_with_pii = """
    Merhaba ELİF HANEDAN Hanım (Proje Yöneticisi),
    Toplantı için CEMİL FİDANLIGÜL Bey ile İstanbul'dan Ankara'ya 25 Aralık 2023 Pazartesi günü saat 09:00'da görüştünüz mü?
    Ödemenizi TR33 0006 1005 1978 6457 8413 26 numaralı IBAN hesabına yapabilirsiniz. Maaşı 15000 USD oldu.
    Ayrıca, Zeynep Kaya ve Mehmet Öztürk de Google şirketindeki projeye dahil olacaklar.
    Diğer bir IBAN ise TR123456789012345678901234.
    Lütfen T.C. Kimlik Numaranızı (12345678901) ve telefon numaranızı (0555 123 45 67) bizimle paylaşın.
    Bir diğer telefon +905329876543 ve TC No: 98765432109.
    Kendisi Atatürk Havalimanı'na indi ve Van Gölü kenarında bir otelde kaldı.
    Saygılarımla,
    ALİ ŞANLI
    """

    print("Orijinal Metin:")
    print("-----------------")
    print(sample_text_with_pii)
    print("\nMaskelenmiş Metin:")
    print("-------------------\n") # Ekstra bir satır boşluk
    masked_text = mask_text(sample_text_with_pii, nlp_model=nlp)
    print(masked_text)

if __name__ == "__main__":
    main()