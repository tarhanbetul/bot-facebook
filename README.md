# bot-facebook

Urllist dosyamda  facebook linkleri bulunmaktadır.
Yaptığım çalışma ile selenium kütüphanesini kullanarak url listemdeki facebook linklerini tek tek gezerek her linke girdiğinde eğer login olması gerekiyorsa
kullanıcıbilgileri dosyamdan kullanıcı bilgilerini alarak facebook'un login sayfasında bu bilgileri girerek login olup anasayfaya girmekte ve png olarak ekran görüntüsü
alıp ilk ekran görüntüsü aldığında bir klasör oluşturup tüm linkleri bitirene kadar her ekran görüntüsü aldığında bu klasöre ekleyen ve ansayfadaki 10 görselin beğeni,
paylaşım, yorum bilgilerini alıp önce her görselinki ayrı bir liste olarak alıp bir dosya oluşturup kaydetmekte sonra her linkdeki toplam beğeni paylaşım yorum sayısını
toplayarak başka bir dosya oluşturarak bu dosyaya kaydeden bir çalışma yapmış bulunmaktayım.

Yukarıda bahsettiğim bilgileri almam için paylaşımların html elementleri tarayıcı dom'unda yorumlanmış olması gerekiyor bu süreci ise ilgili sayfada scrolldown yapan bir
selenium fonksiyonu ile gerçekleştiriyorum.

URL bazında çıktı olarak oluşturduğum tüm dosyaların adları ilgili URL'nin MD5 ile hash'lenmiş halini içermektedir. Böylelikle MD5 algoritmasının tarih bazlı hashed
string üretmesi ile oluşan dosya isimlerinin  projenin her yeniden çalışmasında ürettiği çıktılarda isim çakışması yaşanmamasını sağlanmaktadır.

