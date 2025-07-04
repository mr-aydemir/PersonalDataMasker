import re
from . import patterns
from .patterns import TC_KIMLIK_NO_PATTERN, PHONE_NUMBER_PATTERN # .patterns olarak import ediyoruz çünkü aynı paketteyiz
import spacy

def mask_names_with_spacy(text: str, nlp_model) -> str:
    """
    Metindeki kişi adlarını (PER) spaCy kullanarak maskeler.
    """
    if nlp_model is None:
        print("DEBUG: NLP modeli yüklenemedi, isim maskeleme atlanıyor.")
        return text 

    doc = nlp_model(text)
    
    print("\n--- spaCy Varlık Tespiti (DEBUG) ---")
    if not doc.ents:
        print("DEBUG: spaCy metinde hiçbir varlık bulamadı.")
    else:
        for ent in doc.ents:
            print(f"DEBUG: Bulunan Varlık: '{ent.text}', Etiket: '{ent.label_}', Başlangıç: {ent.start_char}, Bitiş: {ent.end_char}")
    print("--- BİTTİ: spaCy Varlık Tespiti ---\n")

    new_text_parts = []
    current_pos = 0
    masked_something = False
    for ent in sorted(doc.ents, key=lambda e: e.start_char):
        STAR_MASK_LABELS = {"GPE", "ORG", "DATE", "MONEY", "TIME", "TITLE", "FAC", "LOC"}

        if ent.label_ == "PERSON": 
            print(f"DEBUG: '{ent.text}' (Etiket: {ent.label_}) KİŞİ ADI olarak özel maskeleniyor.")
            new_text_parts.append(text[current_pos:ent.start_char])
            
            original_name_text = ent.text
            words = original_name_text.split(' ')
            masked_words = []
            for word in words:
                if len(word) <= 2: 
                    masked_words.append(word)
                elif len(word) == 3:
                    masked_words.append(word[0] + '*' + word[-1])
                else: 
                    masked_words.append(word[0] + '*' * (len(word) - 2) + word[-1])
            new_text_parts.append(' '.join(masked_words))
            current_pos = ent.end_char
            masked_something = True
        elif ent.label_ in STAR_MASK_LABELS:
            print(f"DEBUG: '{ent.text}' (Etiket: {ent.label_}) {ent.label_} olarak yıldızla maskeleniyor.")
            new_text_parts.append(text[current_pos:ent.start_char])
            new_text_parts.append('*' * len(ent.text))
            current_pos = ent.end_char
            masked_something = True
        else:
            new_text_parts.append(text[current_pos:ent.start_char])
            new_text_parts.append(ent.text) # Varlığı olduğu gibi ekle
            current_pos = ent.end_char
            # masked_something bu durumda false kalabilir eğer sadece bu tür varlıklar varsa
            # Ancak döngü sonunda metin birleştirildiği için sorun olmaz.
    
    new_text_parts.append(text[current_pos:])
    
    if not masked_something and doc.ents:
        print("DEBUG: Metinde varlıklar bulundu ancak hiçbiri 'PER' etiketiyle eşleşmedi veya maskelenemedi.")
    elif not doc.ents:
        pass # Zaten yukarıda loglandı
    else:
        print("DEBUG: 'PERSON' etiketli varlıklar için maskeleme işlemi tamamlandı.")
        
    return "".join(new_text_parts)

def mask_text(text: str, nlp_model=None) -> str:
    """
    Metindeki bilinen hassas verileri maskeler.
    Önce IBAN'ları, sonra isimleri maskeler.
    """
    # Dinamik yıldız maskeleme fonksiyonu
    star_mask = lambda m: '*' * len(m.group(0))

    # IBAN Maskeleme
    text = patterns.IBAN_PATTERN.sub(star_mask, text)

    # T.C. Kimlik Numarası Maskeleme
    text = TC_KIMLIK_NO_PATTERN.sub(star_mask, text)

    # Telefon Numarası Maskeleme
    text = PHONE_NUMBER_PATTERN.sub(star_mask, text)

    # İsim/Soyisim ve diğer spaCy varlıklarını Maskeleme
    if nlp_model:
        text = mask_names_with_spacy(text, nlp_model)
    else:
        # Eğer API dışından (örn: main.py) model yüklenmeden çağrılırsa diye bir uyarı eklenebilir
        # veya burada varsayılan bir model yüklenebilir. Şimdilik geçiyoruz.
        print("Uyarı: mask_text fonksiyonuna nlp_model sağlanmadı. spaCy tabanlı maskeleme atlanacak.")

    return text