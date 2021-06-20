# AbiHacklendikGaliba
Şirketin sitelerinin önyüzünü periyodik olarak kontrol edip herhangi bir değişim durumunda e-posta ile bildirim gönderen Python scripti.

- Site adreslerini JSON dosyasından okur. :heavy_check_mark:
- Selenium ile bu sitelerin anasayfalarının ekran görüntünüsünü alarak ilgili klasöre kaydeder. :heavy_check_mark:
- OpenCV aracılığıyla güncel görüntüyü referans görüntü ile karşılaştırır.
- Fark tespit ettiği durumda e-posta ile bildirim gönderir.
