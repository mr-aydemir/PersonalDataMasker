# Proje Genel Bakışı: Türkçe Kişisel Veri Maskeleyici

## Amaç

Bu proje, Türkçe metinlerde bulunan kişisel ve hassas verileri otomatik olarak tespit edip maskelemek amacıyla geliştirilmiştir. Temel hedef, gizliliği korumak ve veri güvenliğini artırmaktır. Özellikle Türkçe dilinin yapısal özelliklerine ve yaygın kişisel veri formatlarına uygun çözümler sunmayı amaçlar.

## Kapsam

Proje, aşağıdaki türdeki kişisel verileri maskeleyebilmektedir:

*   **Kişi Adları ve Soyadları:** spaCy'nin gelişmiş Doğal Dil İşleme (NLP) modelleri kullanılarak tespit edilir.
*   **IBAN Numaraları:** Türkiye'ye özgü IBAN formatlarına uygun düzenli ifadeler (regex) ile tespit edilir.
*   **T.C. Kimlik Numaraları:** Standart T.C. Kimlik Numarası formatına uygun regex ile tespit edilir.
*   **Telefon Numaraları:** Türkiye'deki yaygın telefon numarası formatlarına uygun regex ile tespit edilir.
*   **Coğrafi Varlıklar (GPE):** Ülkeler, şehirler, eyaletler gibi konum bilgileri (spaCy ile).
*   **Kurum ve Kuruluş Adları (ORG):** Şirketler, ajanslar, kurumlar (spaCy ile).
*   **Tarihler (DATE):** Mutlak veya göreceli tarihler ve periyotlar (spaCy ile).
*   **Parasal Değerler (MONEY):** Para birimi içeren değerler (spaCy ile).
*   **Zaman İfadeleri (TIME):** Saat gibi bir günden küçük zaman dilimleri (spaCy ile).
*   **Unvanlar (TITLE):** Kişilere ait mesleki veya sosyal unvanlar (spaCy ile).
*   **Tesisler (FAC):** Binalar, havaalanları, otoyollar gibi yapılar (spaCy ile).
*   **Diğer Konumlar (LOC):** GPE olmayan dağ sıraları, su kütleleri gibi yerler (spaCy ile).

## Temel Teknolojiler

*   **Python:** Ana programlama dili.
*   **spaCy:** Doğal Dil İşleme (NLP) görevleri, özellikle Adlandırılmış Varlık Tanıma (NER) için kullanılır. `tr_core_news_trf` gibi Türkçe'ye özel Transformer tabanlı modeller tercih edilmiştir.
*   **Düzenli İfadeler (Regex):** Yapısal olarak tanımlanabilen IBAN, T.C. Kimlik No, telefon numarası gibi verilerin tespiti için kullanılır.

## Hedef Kitle

Bu proje, metin verileriyle çalışan ve bu veriler içindeki kişisel bilgileri koruma altına almak isteyen geliştiriciler, veri analistleri ve araştırmacılar için tasarlanmıştır.
