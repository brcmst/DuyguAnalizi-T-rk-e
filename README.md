# Duygu Analizi ve Restaurant Yorumları Analizi

Bu depoda, Türkçe metinlerin duygusal tonunu analiz etmek için BERT tabanlı bir model ve bir restoran yorum veri seti üzerinde duygu analizi gerçekleştirmek için Naive Bayes sınıflandırma modeli içeren iki farklı proje bulunmaktadır.

## 1. Duygu Analizi (duygu-analizi.py)

Bu proje, Türkçe metinlerin duygusal tonunu analiz etmek için BERT tabanlı bir model kullanarak duygu analizi gerçekleştirmektedir. Hugging Face'in Transformers kütüphanesinde bulunan önceden eğitilmiş bir Türkçe BERT modeli (`dbmdz/bert-base-turkish-cased`) kullanılarak metinlere pozitif, negatif veya nötr etiketler atanmaktadır.

## 2. Restaurant Reviews Sentiment Analysis (restaurantReviewsNLP.ipynb)

Bu proje, bir restoran yorum veri seti üzerinde duygu analizi yapmayı amaçlamaktadır. Veri seti, kullanıcıların restoran deneyimleri hakkında yazdıkları yorumları içermektedir. Analiz, yorumları temizleme, özellik çıkarma ve Naive Bayes sınıflandırma modeli kullanma adımlarını içermektedir.

### Veri Seti

Proje, "Restaurant_Reviews.tsv" adlı bir tsv dosyasından veri setini kullanmaktadır. Veri seti, yorumlar ve kullanıcının beğeni durumlarını içermektedir.

### Veri Temizleme ve Ön İşleme

Veri temizleme adımları şunlardır:

- Her yorumdaki özel karakterler ve sayılar temizlenir.
- Yorumlar küçük harfe dönüştürülür.
- Stop-words (durak kelimeler) temizlenir.
- Lemmatizasyon (kelimelerin köklerine dönüştürülmesi) uygulanır.

Temizlenmiş yorumlar, "Orijinal Yorum" ve "Temiz Yorum" olarak iki sütunlu bir veri çerçevesine kaydedilir.

### Kelime Frekans Analizi

Temizlenmiş yorumlardaki kelime frekansları analiz edilir. En çok kullanılan kelimelerin frekansları, bir çubuk grafik üzerinde görselleştirilir.

### Özellik Çıkarma ve Model Eğitimi

CountVectorizer kullanılarak, yorumlardaki kelimelerin sayısını içeren bir özellik matrisi oluşturulur. Bu matris, Naive Bayes sınıflandırma modeli için eğitim ve test veri setlerine bölünür.

### Model Performansı

Gaussian Naive Bayes sınıflandırma modeli kullanılarak, test veri setindeki yorumların beğeni durumları tahmin edilir. Modelin performansı, doğruluk skoru kullanılarak ölçülür.
