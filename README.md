# Türkçe Kişisel Veri Maskeleyici

Bu proje, Türkçe metinlerde bulunan kişisel ve hassas verileri (isimler, IBAN, T.C. Kimlik Numaraları, telefon numaraları, konumlar, organizasyonlar vb.) otomatik olarak tespit edip maskelemek amacıyla geliştirilmiştir. Proje, hem bir Python kütüphanesi olarak hem de bir REST API üzerinden kullanılabilir.

## Temel Özellikler

*   **Kapsamlı Veri Tespiti:** Kişi adları, IBAN, T.C. Kimlik No, telefon numaraları, coğrafi konumlar (GPE), organizasyon adları (ORG), tarihler (DATE), para miktarları (MONEY), zaman ifadeleri (TIME) gibi birçok farklı PII türünü tanır.
*   **Hibrit Yaklaşım:** Yapısal veriler (IBAN, T.C. Kimlik No vb.) için düzenli ifadeler (Regex), daha karmaşık ve bağlama duyarlı veriler (isimler, organizasyonlar vb.) için ise son teknoloji Transformer tabanlı spaCy modelleri (`tr_core_news_trf`) kullanılır.
*   **Esnek Maskeleme:** Kişi adları için baş ve son harfleri koruyarak arayı yıldızlama, diğer PII türleri için tam yıldızlama gibi farklı maskeleme stratejileri uygular.
*   **API Desteği:** Maskeleme işlevselliğini `FastAPI` tabanlı bir REST API üzerinden sunar. Bu sayede farklı platform ve uygulamalarla kolay entegrasyon sağlar.
*   **Türkçe Odaklı:** Özellikle Türkçe dilinin yapısal özelliklerine ve yaygın kişisel veri formatlarına uygun olarak tasarlanmıştır.

## Kurulum

1.  **Sanal Ortam Oluşturun ve Aktive Edin (Şiddetle Önerilir):**
    ```bash
    python -m venv .venv
    ```
    Aktive etmek için:
    *   Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
    *   Windows (CMD): `.\.venv\Scripts\activate.bat`
    *   macOS/Linux: `source .venv/bin/activate`

2.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
    Bu komut, `spacy`, `spacy-transformers`, `torch`, `fastapi`, `uvicorn` gibi gerekli tüm kütüphaneleri kuracaktır.
    **Not:** `requirements.txt` dosyasında belirtilen `spaCy` sürümü (`spacy>=3.4.2,<3.5.0`), kullanılan `tr_core_news_trf` modelinin [Hugging Face sayfasında](https://huggingface.co/turkish-nlp-suite/tr_core_news_trf) belirtilen uyumluluk gereksinimlerine göre seçilmiştir. Modelin doğru çalışması için bu sürüm aralığına dikkat ediniz.

3.  **spaCy Türkçe Modelini İndirin (`tr_core_news_trf`):**
    Proje, en iyi sonuçlar için `tr_core_news_trf` Transformer tabanlı Türkçe spaCy modelini kullanır. Bu ve benzeri Türkçe NLP modelleri, genellikle [turkish-nlp-suite tarafından Hugging Face üzerinde](https://huggingface.co/turkish-nlp-suite) yayınlanmaktadır.
    `tr_core_news_trf` modelini kurmanın en doğrudan yolu, `.whl` dosyasını `pip` ile doğrudan URL üzerinden yüklemektir:

    ```bash
    pip install https://huggingface.co/turkish-nlp-suite/tr_core_news_trf/resolve/main/tr_core_news_trf-1.0-py3-none-any.whl
    ```
    Bu komut, `tr_core_news_trf` modelini indirip Python ortamınıza kuracaktır.

## Kullanım

Proje iki ana şekilde kullanılabilir:

### 1. Python Kütüphanesi Olarak

`data_masker.masker` modülündeki `mask_text` fonksiyonunu doğrudan Python kodunuzda kullanabilirsiniz. `main.py` dosyası bu kullanım için bir örnek içerir.

### 2. REST API Olarak

Proje, `FastAPI` ile geliştirilmiş bir REST API sunar.

*   **API Sunucusunu Başlatma:**
    ```bash
    uvicorn api:app --reload
    ```
*   **API Dokümantasyonu (Swagger UI):**
    Sunucu çalışırken `http://127.0.0.1:8000/docs` adresinden interaktif API dokümantasyonuna erişebilir ve API'yi test edebilirsiniz.

## Detaylı Dokümantasyon

Projenin genel bakışı, kurulum detayları, kullanım senaryoları ve maskelenen veri türleri hakkında daha ayrıntılı bilgi için lütfen [`documents`](./documents) klasöründeki belgelere göz atın.

*   [`project_overview.md`](./documents/project_overview.md)
*   [`setup_and_usage.md`](./documents/setup_and_usage.md)
*   [`masked_data_types.md`](./documents/masked_data_types.md)
