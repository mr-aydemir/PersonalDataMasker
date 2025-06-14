# Maskelenen Veri Türleri ve Yöntemleri

Bu belge, Türkçe Kişisel Veri Maskeleyici projesinin hangi tür kişisel ve hassas verileri nasıl tespit ettiğini ve hangi yöntemlerle maskelediğini açıklamaktadır.

## Genel Maskeleme Stratejisi

Proje, iki ana yöntem kullanarak veri tespiti ve maskelemesi yapar:

1.  **Düzenli İfadeler (Regex):** Belirli bir yapıya sahip olan veriler (IBAN, T.C. Kimlik No, Telefon Numarası) için kullanılır. Bu tür veriler genellikle standart formatlara sahiptir.
2.  **spaCy (Doğal Dil İşleme):** Daha karmaşık ve bağlama duyarlı verilerin (Kişi Adları, Kurum Adları, Konumlar vb.) tespiti için kullanılır. Proje, `tr_core_news_trf` gibi gelişmiş Türkçe modellerden faydalanır.

## Maskelenen Veri Türleri Detayları

Aşağıda, maskelenen her bir veri türü için tespit ve maskeleme yöntemi belirtilmiştir:

| Veri Türü                 | Tespit Yöntemi                                  | Maskeleme Yöntemi                                                                 |
| ------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------- |
| **Kişi Adları/Soyadları** | spaCy (`PERSON` etiketi)                        | Her kelimenin ilk ve son harfi görünür, aradaki tüm harfler yıldız (`*`) ile değiştirilir. Örn: "Ahmet Yılmaz" -> "A***t Y****z" |
| **IBAN Numaraları**       | Düzenli İfade (`IBAN_PATTERN`)                  | Tespit edilen IBAN'ın tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "TR12...34" -> "********...**" |
| **T.C. Kimlik Numaraları**| Düzenli İfade (`TC_KIMLIK_NO_PATTERN`)          | Tespit edilen numaranın tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "12345678901" -> "***********" |
| **Telefon Numaraları**    | Düzenli İfade (`PHONE_NUMBER_PATTERN`)          | Tespit edilen numaranın tamamı (başındaki `+` gibi bazı özel karakterler korunabilir), orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "05551234567" -> "***********" |
| **Coğrafi Varlıklar (GPE)** | spaCy (`GPE` etiketi - Ülkeler, şehirler vb.)   | Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "İstanbul" -> "********" |
| **Kurum/Kuruluş Adları (ORG)**| spaCy (`ORG` etiketi - Şirketler, ajanslar vb.)| Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "ABC A.Ş." -> "********" |
| **Tarihler (DATE)**         | spaCy (`DATE` etiketi)                          | Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "15 Mayıs 2024" -> "*************" |
| **Parasal Değerler (MONEY)**| spaCy (`MONEY` etiketi)                         | Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "5.000 TL" -> "********" |
| **Zaman İfadeleri (TIME)**  | spaCy (`TIME` etiketi)                          | Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "Saat 14:30" -> "**********" |
| **Unvanlar (TITLE)**        | spaCy (`TITLE` etiketi - Model tarafından bazen atanır) | Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "Proje Yöneticisi" -> "****************" |
| **Tesisler (FAC)**          | spaCy (`FAC` etiketi - Binalar, havaalanları vb.) | Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "Atatürk Havalimanı" -> "******************" |
| **Diğer Konumlar (LOC)**    | spaCy (`LOC` etiketi - Dağlar, göller vb.)      | Tespit edilen metnin tamamı, orijinal uzunluğu kadar yıldız (`*`) ile değiştirilir. Örn: "Van Gölü" -> "********" |

### Maskeleme Önceliği

`mask_text` fonksiyonu içerisinde maskeleme işlemleri aşağıdaki sırayla uygulanır:

1.  IBAN Numaraları (Regex)
2.  T.C. Kimlik Numaraları (Regex)
3.  Telefon Numaraları (Regex)
4.  Diğer tüm varlıklar (Kişi Adları, GPE, ORG vb. spaCy ile)

Bu sıralama, daha spesifik ve yapısal olan regex tabanlı maskelemelerin önce yapılmasını sağlar, ardından daha genel ve bağlama duyarlı spaCy tabanlı maskeleme gelir.

### Dikkate Alınması Gerekenler

*   **Model Performansı:** spaCy modelinin varlıkları doğru bir şekilde etiketlemesi, maskelemenin doğruluğu için kritik öneme sahiptir. `tr_core_news_trf` gibi Transformer tabanlı modeller genellikle yüksek doğruluk sunar, ancak hiçbir model %100 hatasız değildir.
*   **Regex Kapsamı:** Düzenli ifadeler, tanımlandıkları belirli formatlarla sınırlıdır. Farklı veya beklenmedik formatlardaki veriler tespit edilemeyebilir.
*   **Bağlam:** Özellikle spaCy ile tespit edilen varlıklarda, metnin bağlamı etiketin doğruluğunu etkileyebilir. Nadiren de olsa yanlış pozitifler (olmayan bir varlığın tespit edilmesi) veya yanlış negatifler (var olan bir varlığın tespit edilememesi) görülebilir.

Bu doküman, projenin mevcut yeteneklerini yansıtmaktadır ve gelecekteki geliştirmelerle güncellenebilir.
