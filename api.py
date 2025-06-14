from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from data_masker.masker import mask_text
import spacy

# Modeli yükleme (API başlatıldığında bir kere yüklenmesi için global)
# Modelin doğru yüklendiğinden emin olmak için try-except bloğu eklenebilir
try:
    nlp = spacy.load("tr_core_news_trf")
    print("spaCy modeli 'tr_core_news_trf' başarıyla yüklendi.")
except OSError:
    print("spaCy modeli 'tr_core_news_trf' bulunamadı.")
    print("Lütfen 'python -m spacy download tr_core_news_trf' komutuyla indirin veya")
    print("setup_and_usage.md dosyasındaki .whl kurulum adımlarını takip edin.")
    nlp = None # Model yüklenemezse None olarak ayarla

app = FastAPI(
    title="Türkçe Kişisel Veri Maskeleyici API",
    description="Bu API, Türkçe metinlerdeki kişisel ve hassas verileri maskeler.",
    version="1.0.0"
)

class MaskRequest(BaseModel):
    text: str
    # İleride eklenebilecek opsiyonel parametreler:
    # custom_mask_char: Optional[str] = None
    # mask_types: Optional[list[str]] = None

class MaskResponse(BaseModel):
    original_text: str
    masked_text: str
    # error_message: Optional[str] = None # Hata durumları için

@app.post("/mask", response_model=MaskResponse,
            summary="Metni Maskele",
            description="Verilen metindeki kişisel ve hassas verileri maskeler.")
async def create_mask(request: MaskRequest):
    """
    Bir metin alır ve içindeki kişisel verileri (isim, IBAN, T.C. Kimlik No vb.) maskeler.
    - **text**: Maskelenecek metin.
    """
    if nlp is None:
        return MaskResponse(
            original_text=request.text,
            masked_text="HATA: spaCy modeli yüklenemedi. Lütfen sunucu loglarını kontrol edin.",
            # error_message="spaCy modeli yüklenemedi."
        )
    
    masked_content = mask_text(request.text, nlp_model=nlp) # mask_text fonksiyonunu nlp modeliyle çağır
    return MaskResponse(original_text=request.text, masked_text=masked_content)

@app.get("/health", summary="Sağlık Kontrolü")
async def health_check():
    """
    API'nin çalışır durumda olup olmadığını kontrol eder.
    """
    model_status = "yüklendi" if nlp else "yüklenemedi"
    return {"status": "healthy", "message": "API çalışıyor.", "spacy_model_status": model_status}

# API'yi çalıştırmak için terminalde:
# uvicorn api:app --reload
#
# Örnek bir istek (Python requests ile):
# import requests
# response = requests.post("http://127.0.0.1:8000/mask", json={"text": "Ali Veli, İstanbul'a gitti ve TR123456789012345678901234 IBAN numaralı hesaba 100 TL yolladı."})
# print(response.json())
