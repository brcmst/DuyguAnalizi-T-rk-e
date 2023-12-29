from transformers import pipeline

def duygu_analizi_metodu(text):
    classifier = pipeline('sentiment-analysis', model='dbmdz/bert-base-turkish-cased')
    result = classifier(text)
    return result[0]['label']

if __name__ == "__main__":
    # Duygu analizi yapılacak Türkçe metin
    turkce_metin = input("Duygu analizi yapılacak Türkçe metni girin: ")

    # Duygu analizi metodu çağır
    duygu_etiketi = duygu_analizi_metodu(turkce_metin)

    # Çıktıyı pozitif, negatif veya nötr olarak düzenle
    if duygu_etiketi == 'LABEL_0': #pozitif
        duygu = 'pozitif'
    elif duygu_etiketi == 'LABEL_1':  #negatif
        duygu = 'negatif'
    elif duygu_etiketi == 'LABEL_2':
        duygu = 'nötr'
    else:
        duygu = 'Bilinmeyen'

    # Sonucu ekrana yazdır
    print("Duygu Etiketi:", duygu)


#metin hoca çok iyidir
# dinlediğiniz için teşekkür ederim

    
# kitap sıkıcıydı, ilgimi çekmedi
# konuyla ilgili fikrim yok
    
