# Kurulum ve Kullanım Talimatları

Bu belge, Türkçe Kişisel Veri Maskeleyici projesinin nasıl kurulacağını ve kullanılacağını açıklamaktadır.

## Ön Gereksinimler

*   **Python 3.8 veya üstü:** [Python'un resmi web sitesinden](https://www.python.org/downloads/) indirilebilir.
*   **pip:** Python paket yöneticisi (genellikle Python ile birlikte gelir).
*   **Git (Opsiyonel):** Projeyi klonlamak için.

## Kurulum Adımları

1.  **Proje Dosyalarını İndirin:**
    *   Eğer Git kuruluysa, projeyi klonlayın:
        ```bash
        git clone <proje_git_reposu_adresi> # Eğer bir git reposu varsa
        cd PersonalDataMasker # Proje dizinine girin
        ```
    *   Alternatif olarak, proje dosyalarını manuel olarak bir klasöre kopyalayın.

2.  **Sanal Ortam Oluşturun ve Aktive Edin (Önerilir):
    Proje bağımlılıklarını sistem genelindeki Python kurulumunuzdan izole etmek için bir sanal ortam kullanmanız şiddetle tavsiye edilir.
    Proje ana dizinindeyken (`PersonalDataMasker`):
    ```bash
    # Sanal ortam oluştur (örneğin .venv adında)
    python -m venv .venv

    # Sanal ortamı aktive et
    # Windows (PowerShell):
    .\.venv\Scripts\Activate.ps1
    # Windows (Komut İstemi - cmd.exe):
    .\.venv\Scripts\activate.bat
    # macOS / Linux:
    source .venv/bin/activate
    ```
    Sanal ortam aktif olduğunda, komut satırınızın başında `(.venv)` gibi bir ifade görmelisiniz.

3.  **Bağımlılıkları Yükleyin:**
    Proje için gerekli olan Python kütüphanelerini `requirements.txt` dosyasını kullanarak yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
    Bu komut, `spaCy`, `spacy-transformers`, `torch` gibi gerekli tüm kütüphaneleri kuracaktır.

4.  **spaCy Türkçe Modelini İndirin:**
    Proje, çeşitli denemeler sonucunda en iyi performansı veren `tr_core_news_trf` adlı Transformer tabanlı bir Türkçe spaCy modeli kullanmaktadır. Bu model, `turkish-nlp-suite` tarafından Hugging Face üzerinde sunulmaktadır.
    Modeli kurmanın en güvenilir yolu, doğrudan Hugging Face üzerinden `.whl` dosyasını `pip` kullanarak yüklemektir. Bu yöntem, `python -m spacy download` komutunun bu spesifik transformer modeli için bazen yaşattığı uyumluluk sorunlarını aşmanızı sağlar.

    `tr_core_news_trf` modelini kurmak için aşağıdaki komutu kullanabilirsiniz:
    ```bash
    pip install https://huggingface.co/turkish-nlp-suite/tr_core_news_trf/resolve/main/tr_core_news_trf-1.0-py3-none-any.whl
    ```
    Bu komut, modeli doğrudan belirtilen URL'den indirip Python ortamınıza kuracaktır.
        **Not:** `.whl` dosyaları genellikle büyük boyutlu olabilir. Bu dosyaları Git reponuzda tutmak yerine, yukarıdaki gibi bir indirme linki veya talimatı sağlamak daha iyi bir pratiktir. `.gitignore` dosyanıza `*.whl` eklenerek bu dosyaların yanlışlıkla repoya eklenmesi engellenebilir.

## Kullanım

Projenin temel kullanımı, `main.py` betiğini çalıştırmaktır. Bu betik, örnek bir metin üzerinde maskeleme işlemini gösterir.

1.  Sanal ortamınızın aktif olduğundan emin olun.
2.  Proje ana dizinindeyken aşağıdaki komutu çalıştırın:
    ```bash
    python main.py
    ```
    Bu komut, `main.py` içerisinde tanımlanmış olan örnek metni okuyacak, `data_masker.masker.mask_text` fonksiyonunu kullanarak kişisel verileri maskeleyecek ve hem orijinal metni hem de maskelenmiş metni konsola yazdıracaktır.

### Kendi Metinlerinizle Kullanım

Kendi metinlerinizi maskelemek için `main.py` dosyasını düzenleyebilir veya `data_masker.masker.mask_text` fonksiyonunu kendi Python betiklerinizde doğrudan kullanabilirsiniz:

```python
from data_masker.masker import mask_text

metin = "Bu metin Ayşe Hanım'a ait olup IBAN'ı TR123456789012345678901234 ve T.C. Kimlik No'su 12345678901'dir."
maskelenmis_metin = mask_text(metin)
print(maskelenmis_metin)
```

## Model Varlıklarını Keşfetme

Kullanılan spaCy modelinin hangi varlık türlerini (entity labels) tanıyabildiğini görmek için `explore_model_entities.py` betiğini çalıştırabilirsiniz:

```bash
python explore_model_entities.py
```
Bu, modelin yeteneklerini anlamanıza yardımcı olacaktır.

## API Kullanımı

Proje, maskeleme işlevselliğini bir REST API üzerinden de sunmaktadır. API, FastAPI kullanılarak oluşturulmuştur.

### 1. API Bağımlılıklarını Yükleme

Eğer daha önce yapmadıysanız, `requirements.txt` dosyasındaki tüm bağımlılıkları yükleyin. Bu komut, `fastapi` ve `uvicorn` gibi API için gerekli kütüphaneleri de kuracaktır.

```bash
pip install -r requirements.txt
```

### 2. API Sunucusunu Başlatma

Proje ana dizinindeyken terminalde aşağıdaki komutu çalıştırarak API sunucusunu başlatın:

```bash
uvicorn api:app --reload
```

*   `uvicorn`: ASGI sunucusudur.
*   `api:app`: `api.py` dosyasındaki `app` adlı FastAPI örneğini işaret eder.
*   `--reload`: Kodda değişiklik yaptığınızda sunucunun otomatik olarak yeniden başlatılmasını sağlar.

Sunucu başarıyla başladığında, terminalde `http://127.0.0.1:8000` adresinde çalıştığına dair bir mesaj göreceksiniz.

### 3. API'yi Test Etme (Swagger UI ile)

FastAPI, otomatik olarak interaktif bir API dokümantasyonu (Swagger UI) oluşturur. Bu arayüzü kullanarak API'yi kolayca test edebilirsiniz.

1.  API sunucusu çalışırken, web tarayıcınızı açın ve şu adrese gidin: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
2.  Açılan sayfada `/mask` ve `/health` endpoint'lerini göreceksiniz.
3.  `/mask` endpoint'ini genişletin ve **"Try it out"** butonuna tıklayın.
4.  **"Request body"** alanına, maskelemek istediğiniz metni JSON formatında girin. Örneğin:
    ```json
    {
      "text": "ALİ ŞANLI yarın İstanbul'a gidecek. IBAN'ı TR123456789012345678901234."
    }
    ```
5.  **"Execute"** butonuna tıklayın.
6.  Aşağıdaki **"Responses"** bölümünde API'den dönen orijinal ve maskelenmiş metni görebilirsiniz.
