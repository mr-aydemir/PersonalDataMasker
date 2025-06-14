import spacy

# Kullandığımız modelin adı (masker.py dosyasındaki ile aynı olmalı)
MODEL_NAME = "tr_core_news_trf"

def explore_entities():
    """spaCy modelinin tanıyabileceği varlık türlerini ve örnek metindeki varlıkları listeler."""
    try:
        nlp = spacy.load(MODEL_NAME)
        print(f"'{MODEL_NAME}' spaCy modeli başarıyla yüklendi.\n")
    except OSError:
        print(f"'{MODEL_NAME}' modeli bulunamadı. Lütfen doğru modelin kurulu olduğundan emin olun.")
        print(f"Kurulum için: python -m spacy download {MODEL_NAME} veya .whl dosyasını kullanın.")
        return

    # Modelin NER bileşenindeki tüm etiket türlerini alalım
    if nlp.has_pipe("ner"):
        ner_pipe = nlp.get_pipe("ner")
        all_labels = ner_pipe.labels
        print("Modelin tanıyabileceği tüm NER etiket türleri:")
        print("---------------------------------------------")
        for label in sorted(list(all_labels)):
            print(f"- {label}: {spacy.explain(label)}")
        print("\n")
    else:
        print("Modelde 'ner' (Named Entity Recognition) bileşeni bulunamadı.\n")

    # Çeşitli varlık türleri içerebilecek örnek bir metin
    sample_text = """
    Ayşe Yılmaz, İstanbul'da bulunan ABC Teknoloji A.Ş. şirketinde yazılım mühendisi olarak çalışıyor.
    Geçen hafta Salı günü, 15 Mayıs 2024 tarihinde, Ankara'ya bir iş gezisi yaptı.
    Bu gezi için 5.000 TL bütçe ayrıldı. Proje, Avrupa Birliği tarafından desteklenmektedir.
    Saat 14:30'da başlayan toplantı oldukça verimli geçti. Türkiye Büyük Millet Meclisi de ziyaret edildi.
    Rapora göre, Dolar kuru 32.50 seviyesindeydi. COVID-19 pandemisi sonrası ilk yüz yüze etkinlikti.
    """

    print("Örnek Metin:")
    print("------------")
    print(sample_text)
    print("\nBulunan Varlıklar ve Etiketleri:")
    print("-------------------------------")

    doc = nlp(sample_text)
    if not doc.ents:
        print("Örnek metinde herhangi bir varlık bulunamadı.")
    else:
        found_labels = set()
        for ent in doc.ents:
            print(f"- Metin: '{ent.text}', Etiket: {ent.label_} ({spacy.explain(ent.label_)})")
            found_labels.add(ent.label_)
        
        print("\nÖrnek metinde bulunan benzersiz etiket türleri:")
        for label in sorted(list(found_labels)):
            print(f"- {label}")

if __name__ == "__main__":
    explore_entities()
