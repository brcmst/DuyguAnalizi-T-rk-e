Türkçe Duygu Analizi (BERT Tabanlı)
Bu proje, Türkçe metinlerin duygusal tonunu analiz etmek için BERT tabanlı bir model kullanarak duygu analizi gerçekleştirmektedir. Hugging Face'in Transformers kütüphanesinde bulunan önceden eğitilmiş bir Türkçe BERT modeli (dbmdz/bert-base-turkish-cased) kullanılarak metinlere pozitif, negatif veya nötr etiketler atanmaktadır.

Kullanım
Projeyi bilgisayarınıza klonlayın:

bash
Copy code
git clone https://github.com/kullanici_adi/turkce-duygu-analizi.git
Gerekli kütüphaneleri yükleyin:

bash
Copy code
pip install transformers
duygu_analizi.py dosyasını çalıştırarak Türkçe metinlerin duygu analizini gerçekleştirin:

bash
Copy code
python duygu_analizi.py
Ardından, ekrandaki talimatları takip ederek Türkçe metinleri girin ve duygu analizi sonuçlarını gözlemleyin.

Örnek
python
Copy code
from transformers import pipeline

def duygu_analizi_metodu(text):
    classifier = pipeline('sentiment-analysis', model='dbmdz/bert-base-turkish-cased')
    result = classifier(text)
    return result[0]['label']

if __name__ == "__main__":
    turkce_metin = input("Duygu analizi yapılacak Türkçe metni girin: ")
    duygu_etiketi = duygu_analizi_metodu(turkce_metin)

    if duygu_etiketi == 'LABEL_0':
        duygu = 'Negatif'
    elif duygu_etiketi == 'LABEL_1':
        duygu = 'Nötr'
    elif duygu_etiketi == 'LABEL_2':
        duygu = 'Pozitif'
    else:
        duygu = 'Bilinmeyen'

    print("Duygu Etiketi:", duygu)
Bu örnek kod, Türkçe metinlerin duygu analizi için basit bir arayüz sağlar ve Hugging Face'in Türkçe BERT modelini kullanarak duygusal tonları sınıflandırır.
