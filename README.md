# Kişisel Veri Maskeleme Projesi

Bu proje, metinlerdeki kişisel ve hassas verileri (isim, soyisim, IBAN vb.) maskelemek için geliştirilmiştir.
Proje, Türkçe metinlerle uyumlu çalışacak şekilde tasarlanmıştır.

## Kurulum

1.  **Sanal Ortam Oluşturma (Önerilir):**
    ```bash
    python -m venv .venv
    ```
    Ardından sanal ortamı aktive edin:
    *   Windows: `.\.venv\Scripts\activate`
    *   macOS/Linux: `source .venv/bin/activate`

2.  **Gerekli Kütüphanelerin Yüklenmesi:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **spaCy Türkçe Modelinin İndirilmesi:**
    Hassas bilgileri (özellikle kişi adları) tanımak için spaCy kütüphanesini ve Türkçe modelini kullanacağız.
    Aşağıdaki komutla `tr_core_news_sm` (küçük) modelini indirebilirsiniz:
    ```bash
    python -m spacy download tr_core_news_sm
    ```
    Daha yüksek doğruluk için `tr_core_news_md` (orta) veya `tr_core_news_lg` (büyük) modellerini de tercih edebilirsiniz. Bu modeller daha fazla disk alanı kaplar ve daha yavaş çalışabilir. Model seçimi projenin ilerleyen aşamalarında ihtiyaca göre güncellenebilir.

## Kullanım

Projenin ana betiği `main.py` dosyası olacaktır.
```bash
python main.py
```
(Kullanım detayları proje geliştikçe eklenecektir.)

## Proje Yapısı (Önerilen)

-   `data_masker/`: Ana maskeleme mantığını içeren modüller.
    -   `masker.py`: Maskeleme fonksiyonları.
    -   `patterns.py`: Regex desenleri ve hassas veri tanımları.
    -   `utils.py`: Yardımcı fonksiyonlar.
-   `tests/`: Birim testler.
-   `main.py`: Projenin çalıştırılacağı ana betik.
-   `requirements.txt`: Gerekli Python kütüphaneleri.
-   `README.md`: Bu dosya.
