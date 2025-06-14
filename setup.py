import setuptools

# README.md dosyasını oku (PyPI'da uzun açıklama olarak kullanılacak)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# requirements.txt dosyasını oku (bağımlılıklar için)
with open("requirements.txt", "r", encoding="utf-8") as f:
    # Yorumları ve boş satırları filtrele
    requirements = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

setuptools.setup(
    name="turkish-pii-masker",
    version="0.1.0",           # İlk versiyon
    author="Emre Aydemir, Elif Hanedan",
    author_email="aydemir_emre65@hotmail.com",
    description="Türkçe metinler için Kapsamlı Kişisel Veri Maskeleyici.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-aydemir/PersonalDataMasker",
    packages=setuptools.find_packages(), # Projedeki paketleri otomatik bulur (data_masker)
    install_requires=requirements, # requirements.txt'den gelen bağımlılıklar
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: General",
        "Natural Language :: Turkish",
    ],
    python_requires='>=3.8',
)
