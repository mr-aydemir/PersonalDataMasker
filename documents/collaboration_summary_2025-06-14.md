# İşbirliği Özeti: Türkçe Kişisel Veri Maskeleyici (14 Haziran 2025)

Bu belge, Cascade AI ve Kullanıcı arasındaki işbirliğiyle geliştirilen Türkçe Kişisel Veri Maskeleyici projesinin önemli adımlarını ve kararlarını özetlemektedir.

## 1. Projenin Ana Hedefi

Türkçe metinlerde bulunan kişisel ve hassas verilerin (isimler, IBAN, T.C. Kimlik Numaraları, telefon numaraları, konumlar, organizasyonlar vb.) tespit edilerek uygun yöntemlerle maskelenmesi ve böylece veri gizliliğinin sağlanması.

## 2. Kullanılan Temel Teknolojiler

*   **Programlama Dili:** Python
*   **Doğal Dil İşleme (NLP):** spaCy kütüphanesi
    *   **Model:** `tr_core_news_trf` (Transformer tabanlı Türkçe model)
*   **Desen Eşleştirme:** Düzenli İfadeler (Regex)
*   **Bağımlılık Yönetimi:** `requirements.txt`
*   **Versiyon Kontrolü:** Git

## 3. Maskelenen Ana Veri Türleri ve Yöntemleri

| Veri Türü                 | Tespit Yöntemi                                  | Maskeleme Yöntemi                                                                 |
| ------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------- |
| Kişi Adları/Soyadları     | spaCy (`PERSON` etiketi)                        | Her kelimenin ilk ve son harfi görünür, aradaki tüm harfler yıldız (`*`). Örn: "Ahmet Yılmaz" -> "A***t Y****z" |
| IBAN Numaraları           | Düzenli İfade (`IBAN_PATTERN`)                  | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "TR12...34" -> "********...**" |
| T.C. Kimlik Numaraları    | Düzenli İfade (`TC_KIMLIK_NO_PATTERN`)          | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "12345678901" -> "***********" |
| Telefon Numaraları        | Düzenli İfade (`PHONE_NUMBER_PATTERN`)          | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "05551234567" -> "***********" |
| Coğrafi Varlıklar (GPE)   | spaCy (`GPE` etiketi)                           | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "İstanbul" -> "********" |
| Kurum/Kuruluş Adları (ORG)| spaCy (`ORG` etiketi)                           | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "ABC A.Ş." -> "********" |
| Tarihler (DATE)           | spaCy (`DATE` etiketi)                          | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "15 Mayıs 2024" -> "*************" |
| Parasal Değerler (MONEY)  | spaCy (`MONEY` etiketi)                         | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "5.000 TL" -> "********" |
| Zaman İfadeleri (TIME)    | spaCy (`TIME` etiketi)                          | Tamamı, orijinal uzunluğu kadar yıldız (`*`). Örn: "Saat 14:30" -> "**********" |
| Unvanlar (TITLE)          | spaCy (`TITLE` etiketi)                         | Tamamı, orijinal uzunluğu kadar yıldız (`*`). |
| Tesisler (FAC)            | spaCy (`FAC` etiketi)                           | Tamamı, orijinal uzunluğu kadar yıldız (`*`). |
| Diğer Konumlar (LOC)      | spaCy (`LOC` etiketi)                           | Tamamı, orijinal uzunluğu kadar yıldız (`*`). |

## 4. Önemli Dosyalar ve Geliştirmeler

*   **`data_masker/` paketi:**
    *   `masker.py`: Ana maskeleme fonksiyonlarını (`mask_text`, `mask_names_with_spacy`) içerir. Regex ve spaCy tabanlı maskeleme mantığı burada uygulanmıştır.
    *   `patterns.py`: IBAN, T.C. Kimlik No ve telefon numaraları için Regex desenlerini barındırır.
    *   `__init__.py`, `utils.py`: Paket yapısı ve yardımcı fonksiyonlar için (şu an için `utils.py` boş).
*   **`main.py`:**
    *   Örnek metin üzerinde maskeleme işlemini test etmek ve göstermek için kullanılır.
    *   Farklı PII türlerini içeren kapsamlı bir örnek metinle güncellenmiştir.
*   **`explore_model_entities.py`:**
    *   Kullanılan spaCy modelinin (`tr_core_news_trf`) tanıyabildiği varlık türlerini listelemek ve örnek metin üzerinde test etmek için oluşturulmuştur.
*   **`requirements.txt`:**
    *   Proje bağımlılıklarını (`spacy`, `spacy-transformers`, `torch`) içerir.
*   **`documents/` klasörü:**
    *   `project_overview.md`: Projenin genel amacı, kapsamı ve teknolojileri hakkında detaylı bilgi.
    *   `setup_and_usage.md`: Kurulum adımları, sanal ortam oluşturma, bağımlılıkların yüklenmesi, spaCy modelinin indirilmesi (Hugging Face `.whl` linki dahil) ve projenin kullanımı hakkında talimatlar.
    *   `masked_data_types.md`: Maskelenen veri türleri, tespit yöntemleri ve maskeleme stratejileri hakkında detaylı tablo ve açıklamalar.
*   **`.gitignore`:**
    *   Sanal ortam klasörleri (`.venv`), Python cache (`__pycache__`), IDE ayar dosyaları (`.vscode/`, `.idea/`), `.whl` dosyaları gibi gereksiz dosyaların Git deposuna eklenmesini engellemek için oluşturulmuş ve güncellenmiştir.
*   **`tests/` klasörü:**
    *   `test_masker.py`: Maskeleme fonksiyonları için birim testleri içermektedir (içeriği bu oturumda detaylı incelenmedi ancak varlığı not edildi).
*   **`api.py`:**
    *   Maskeleme işlevselliğini bir REST API olarak sunmak için `FastAPI` kullanılarak oluşturulmuştur.
    *   `/mask` ve `/health` endpoint'lerini içerir.
    *   API başlatıldığında spaCy modelini bir kere yükleyerek performansı artırır.
    *   `__init__.py`: Test paketini tanımlar.

## 5. Model Seçimi ve Kurulumu

*   Çeşitli denemeler sonucunda, Türkçe metinlerde kişisel veri tespiti için en iyi sonuçları veren modelin `tr_core_news_trf` olduğu belirlenmiştir.
*   Bu modelin `turkish-nlp-suite` tarafından Hugging Face üzerinde yayınlanan `.whl` dosyası aracılığıyla ([link](https://huggingface.co/turkish-nlp-suite/tr_core_news_trf/blob/main/tr_core_news_trf-1.0-py3-none-any.whl)) veya `python -m spacy download tr_core_news_trf` komutuyla kurulabileceği `setup_and_usage.md` dosyasında belirtilmiştir.
*   `.whl` dosyalarının büyük boyutlu olabileceği ve Git'e eklenmemesi gerektiği vurgulanmış, `.gitignore` dosyasına `*.whl` eklenmiştir.

## 6. Git Entegrasyonu

Kullanıcı tarafından aşağıdaki Git komutları çalıştırılarak projenin yerel bir Git deposu olarak başlatıldığı ve ilk commit'in yapıldığı gözlemlenmiştir:

*   `git init` (Daha önceki bir adımda yapılmış olabilir, bu oturumda doğrudan görülmedi ancak commit yapıldığı için varsayıldı)
*   `git add .`
*   `git commit -m "İlk commit: Proje yapısı ve temel maskeleme işlevselliği"`

## 7. API Geliştirme

*   Projenin işlevselliğini daha geniş bir kitleye sunmak ve entegrasyonu kolaylaştırmak amacıyla bir FastAPI tabanlı API (`api.py`) oluşturuldu.
*   `data_masker/masker.py` ve `main.py` dosyaları, spaCy modelinin global olarak yüklenmesi yerine, fonksiyonlara bir parametre olarak geçilecek şekilde yeniden düzenlendi. Bu, hem API'nin hem de komut satırı betiğinin modeli bağımsız olarak yönetmesine olanak tanır.
*   `requirements.txt` dosyasına `fastapi` ve `uvicorn` bağımlılıkları eklendi.

## 8. Sonraki Adımlar (Öneriler)

*   Projenin bir uzak Git deposuna (örn: GitHub, GitLab) gönderilmesi.
*   `tests/test_masker.py` içerisindeki birim testlerinin kapsamının genişletilmesi ve tüm maskeleme senaryolarını kapsaması.
*   Performans testleri ve optimizasyonları (özellikle büyük metinler için).
*   Yeni PII türleri için destek eklenmesi (eğer gerekirse).
*   Kullanıcı arayüzü (CLI veya basit bir Web UI) geliştirilmesi.

Bu özet, projenin mevcut durumunu ve gelişim sürecini yansıtmaktadır.
