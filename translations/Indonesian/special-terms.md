# Indonesian translation style guide (Panduan gaya penerjemahan bahasa Indonesia)

## Preface (Pendahuluan)

Indonesia is a developing country. With this status, Indonesia can be thought
of as it is still seeking for international knowledge. With a low APM (Angka
Partisipasi Murni, Pure Participation Number) that is steadily increasing, some
Indonesian Zulip users will have a possibility of having a difficult time
understanding English. Apart from that, recall that the user may just like
their own national language more, and this is reasonable. This is one of the
backgrounds of this document creation. This document is created to guide
translators in using the right style for translating the vocabularies from
Zulip, so that the results of the translation will be consistent and better.

Please note that the contributors **may not** be a linguistic expert nor
translation expert. But attempts have been made to make this style guide as
good as possible. So if there is any suggestion about the document, feel free
to contribute as well to improve the quality of the document.

Indonesia adalah negara yang berkembang. Dengan status ini, Indonesia dapat
dikatakan masih dalam proses pengembangan pengetahuan internasional. Dengan
Angka Partisipasi Murni yang terbilang masih cukup rendah namun dengan
perlahan naik, beberapa pengguna Zulip yang berasal dari Indonesia akan
berkemungkinan mengalami kesulitan dalam memahami bahasa Inggris. Selain 
dari itu, perlu diingat juga bahwa pengguna mungkin lebih suka dengan 
bahasa nasionalnya sendiri, dan ini merupakan hal yang wajar. Ini merupakan
salah satu latar belakang dokumen ini dibuat. Pembuatan dokumen ini bertujuan
untuk memandu para penerjemah dalam menggunakan gaya yang benar dalam
menerjemahkan kosakata yang ada dalam Zulip, sehingga hasil terjemahan akan
konsisten dan lebih baik.

Perlu diketahui bahwa para kontributor **mungkin bukanlah** seorang ahli 
linguistik ataupun ahli terjemahan. Tetapi para kontributor telah mencoba 
untuk membuat panduan gaya ini sebaik mungkin. Jadi apabila ada saran 
tentang dokumen ini, jangan merasa sungkan untuk ikut berkontribusi juga 
untuk meningkatkan kualitas dokumen ini.

## Terms (Istilah)

* Message - Pesan

Message in this case is pesan. If we look at the Indonesian dictionary, pesan
is something that is told **through** other people. This is clearly incorrect,
but because there is a shift in meaning through time, the word pesan can be
used instead of surat, even though surat has a more accurate definition, surat
can only be translated through a physical media (paper), so using the word
pesan is more appropriate in this context.

Message dalam hal ini adalah pesan. Apabila kita lihat dalam kamus bahasa
Indonesia, pesan adalah sesuatu yang disampaikan **lewat** orang lain. Ini
melenceng, namun karena pergeseran makna yang semakin meluas, kata pesan dapat
digunakan daripada kata surat, walaupun surat memiliki definisi yang lebih
tepat, surat hanya dapat ditranslasikan ke dalam media fisik (kertas), sehingga
penggunaan kata pesan lebih cocok dalam konteks ini.

* Private Message (PM) - (Pesan Pribadi (PM))

The word private, if translated into a word in Indonesian will not work, as it
got lost in translation. But the best word to use in this case is pribadi.
Pribadi has a general meaning of: between people or groups, therefore it is
more appropriate to use.

The insertion of (PM) in this case is optional, it's even better to not use it
at all. This insertion can be intended as a shorter way to say in an informal 
conversation between Zulip users. For example: "check pm, info's right
there" (informal), and "Check Private Message, the info is located there."
(formal). And most of the time people use the informal way of the conversation
than the formal one.

Makna private apabila diartikan ke dalam satu kata bahasa Indonesa akan
mengalami kehilangan makna dalam terjemahan. Namun kata yang paling tepat untuk
digunakan dalam hal ini adalah pribadi. Pribadi memiliki makna umum antar 
seseorang atau suatu kelompok, sehingga lebih cocok penggunaannnya.

Penyisipan (PM) dalam hal ini bersifat optional, bahkan lebih baik apabila
tidak disisipkan sama sekali. Penyisipan ini dapat bertujuan untuk penggunaan
kata yang lebih singkat dalam percakapan informal pengguna Zulip. Contoh: "cek
pm, ada disitu infony" (informal), dan "Periksa Pesan Pribadi, infonya terdapat
disana." (formal). Dan sering kali percakapan informal lebih digunakan daripada
yang formal.

* Group PM - Pesan Pribadi Grup

Grup has a same meaning with group, so it can be translated directly. You can
also translate it into PM Grup. But at this point, you might as well use the
English word in its entirety.

Grup memiliki makna yang sama dengan group, sehingga dapat diterjemahkan secara
langsung. Anda dapat juga menerjemahkannya menjadi PM Grup. Tapi pada saat ini,
Anda gunakan saja keseluruhan kata Inggris tersebut.

* Realm - Bidang

The choice of the word bidang is caused by a more generalised meaning than the
meaning of organisasi, bagian, or komunitas. Bidang also represents realms more
correctly in Zulip than the other, and it is more flexible so that it can be
directly used for translation.

Pemilihan kata bidang digunakan sebab makna bidang lebih luas daripada makna
organisasi, bagian, atau komunitas. Bidang juga lebih merepresentasikan realms
dalam Zulip dan lebih fleksibel sehingga dapat langsung digunakan dalam proses 
penerjemahan.

* Stream - Siaran

Siaran is used because it has the closest meaning with stream in the context of
Zulip rather than aliran, pengaliran, sungai, urutan, cucuran, etc.

The other alternative is arus, where arus has the same explicit meaning as the
explicit meaning of stream. But this is doesn't really match well for Zulip, so
siaran is used instead.

Siaran digunakan sebab memiliki makna yang paling mirip dengan stream dalam
konteks Zulip daripada aliran, pengaliran, sungai, urutan, cucuran, dsb.

Alternatif lain adalah arus, dimana arus mempunyai makna denotatif yang sama
dengan makna denotatif dari stream. Namun ini tidak terlalu cocok untuk
digunakan di Zulip, sehingga dipakai kata siaran.

* Topic - Topik

Topic is included in the list of "uptaken" words from English in Indonesian.
Direct translation would not be a problem.

Topik termasuk dalam daftar kata serapan dari bahasa Inggris dalam bahasa
Indonesia. Penerjemahan secara langsung tidak akan menjadi masalah.

* Private/Invite-Only Stream - Siaran Pribadi/Undangan

The meaning of "Private/Invite-Only Stream" is a stream that can only be
entered if the person is invited, like attending to an invitation, you need to
get the invitation so you can (and "*deserve*") enter to that place.

Arti siaran undangan adalah siaran yang hanya dapat dimasuki apabila orang
tersebut diundang, layaknya kita ke dalam suatu acara undangan, kita perlu
mendapatkan undangan tersebut agar kita dapat *layak* masuk dalam tempat
undangan tersebut.

* Public Stream - Siaran Publik

Other than the word publik, which is also the "uptake" word, the word "umum"
can also be used, so the translation will be "Siaran Umum". But "Siaran Umum"
has this context that is not really appropriate for Zulip, because the word
"umum" here can mean "a persuasive stream, the one that people *must* watch"

Selain kata publik yang termasuk kata serapan, kata "umum" juga dapat
digunakan, sehingga terjemahan akan menjadi "Siaran Umum". "Siaran Umum"
memiliki konteks yang tidak terlalu cocok untuk Zulip, karena kata "umum"
disini memiliki arti "siaran yang persuasif, yang mengundang umum untuk 
dilihat"

* Bot - Robot

Both can be used (Bot/Robot), but for consistency, use the word robot.

Kedua kata dapat dipakai (Bot/Robot), namun untuk konsistensi, gunakan kata 
robot.

* Integration - Integrasi

Integrasi is an "uptake" word. So no problem here translating it directly.

Integrasi merupakan kata serapan juga. Jadi tidak menjadi masalah untuk
diterjemahkan secara langsung.

* Notification - Notifikasi/Pemberitahuan

Notifikasi has a meaning that is similar with notification, but pemberitahuan
is a better choice meaning-wise. However, because notifikasi is more commonly
used, and it resembles the English word more, notification can be translated as
notifikasi.

Notifikasi mempunyai arti yang mirip dengan notification, namun pemberitahuan 
adalah kata yang lebih tepat dalam segi makna. Tapi karena notifikasi lebih
sering digunakan, dan lebih mirip dengan huruf Inggris yang diterjemahkan, 
notification akan diartikan sebagai notifikasi.

* Alert Word - Kata Pemberitahuan

Alert in this context can't be translated as a dangerous situation or something
like that, but can be translated more as a "notification"

Alert dalam konteks ini tidak dapat diartikan sebagai situasi yang
genting/gawat atau berbahaya, namun lebih dapat diartikan sebagai pemberitahuan
akan hal yang **penting** (namun belum tentu bersifat bahaya). Sehingga kata
yang paling cocok untuk mengartikan alert adalah pemberitahuan.

* View - Lihat

* Home - Beranda

Translate the word home into Indonesian and you will get a literal meaning of
home. This is obviously not the right word to use. The word beranda can be used
instead. Facebook does this as well. They translate Home -> Beranda. Here's the
catch: If this word gets translated back into English, the result will have a
more specific meaning than just home. It will be more like a terrace. This is
not an accurate thing to do too, but this is the best that we can do to
represent the meaning of the word home in this context.

Terjemahkan home ke bahasa Indonesia dan Anda akan mendapatkan kata rumah. Ini
bukan kata yang cocok untuk digunakan. Kata beranda dapat digunakan, seperti
yang dipakai oleh Facebook untuk menerjemahkan Home -> Beranda. Apabila ini
diterjemahkan kembali ke bahasa Inggris, hasilnya akan mempunyai makna teras.
Ini bukan merupakan hal yang akurat, namun ini hal yang paling
merepresentasikan arti Home dalam konteks ini.

* Emoji - Emoji

* Subscribe - Berlanggan

Notice that berlangganan is not the same as berlanggan. Berlangganan and
berlanggan can be thought of as the analogy of a seller and a buyer. A seller
berlangganan newspapers and the buyer berlanggan newpapers.

Perhatikan bahwa berlangganan tidak sama dengan berlanggan. Berlangganan dan
berlanggan dapat dianalogikan layaknya seorang penjual dan pembeli. Penjual
berlangganan koran dan pembeli berlanggan koran.

# Phases (Frasa)

* Subscribe to a stream/Unsubscribe from a stream - Berlanggan ke siaran/
Berhenti berlanggan dari siaran

* Narrow to - Bataskan sampai

The word batas is used because it has the closest meaning with narrow. Narrow
has this as one of the meanings: Limited in area or scope. There is an
alternative word, which is sempit. But the usage of the word is not natural for
Zulip, so batas is used instead.

Kata batas dipakai karena memiliki arti yang paling mirip dengan narrow.
Narrow memiliki salah satu arti: terbatas dalam suatu area ada bagian. Terdapat
kata alternatif, yaitu sempit, namun penggunaan katanya berkesan tidak natural
dengan Zulip, sehingga dipakai kata batas.

* Filter - Saring

The word filter here has one of the meaning, is to view different kinds of
messages that are listed in the top left corner of Zulip application (All
messages, Private messages, Starred messages, and Mentions). Therefore, saring
is choosed.

Filter disini mempunyai makna salah satu pilihan untuk melihat berbagai macam
pesan yang disajikan pada bagian pojok kiri atas aplikasi Zulip (Semua pesan,
Pesan pribadi, Pesan dibintangi, dan Singgungan). Oleh karena itu, dipilih kata
saring.

* Mute/Unmute - Diam/Nyalakan

This is related to muting a topic or stream. When a user wants to stop being
notified from the messages sent from a specific stream or topic, the user can
choose to mute the stream or topic if they want to do so.

Diam has a meaning of silent, and the adjective to describe the unableness to
talk in Indonesian is bisu. Bisu commonly targets certain objects, and we use
diam as the absence of sound in our daily lives. Both are fine to use, but 
diam is better because it resembles the actual meaning of mute in Zulip.

Nyalakan has a meaning of "flipping the switch", or "to light (back)". 
Because there is no correct word to describe unmute in Indonesian, use the 
word nyalakan instead.

Ini berhubungan tentang mendiamkan suatu topik atau siaran. Saat pengguna ingin
menghentikan notifikasi yang diterima pada suatu siaran atau topic, pengguna
dapat memilih untuk mendiamkan siaran atau topik tersebut jika mereka mau.

Diam mempunyai arti silent, tetapi kata sifat untuk mendeskripsikan
ketidakmampuan seseorang untuk berbicara adalah bisu. Bisu biasa menargetkan
objek tertentu, dan kita gunakan kata diam dalam kehidupan sehari-hari untuk 
memberitahukan ketidakadaan suara. Dua-duanya dapat digunakan, tetapi kata diam
lebih baik digunakan karena kata ini lebih pas dnegan kata mute pada Zulip.

Nyalakan mempunyai arti menghidupkan (kembali), karena tidak ada kata yang
tepat untuk mendeskripsikan unmute di bahasa Indonesia, gunakan kata nyalakan.

* Deactivate/Reactivate - Nonaktifkan/Aktifkan (kembali)

Aktif(kan) kembali literally translates to active(it) back, which matches with
the meaning of reactivate.

Aktifkan kembali apabila diartikan secara langsung adalah active(it) back, yang
mempunyai arti yang mirip dengan reactivate.

* Search - Cari

* Pin - Semat

Pinning a stream will move the stream to the top. Semat has a meaning to pin
something up, which is exactly what pinning in Zulip means.

Menyematkan suatu siaran akan memindahkan siaran tersebut ke tempat teratas.
Semat mempunyai makna untuk menyematkan sesuatu, sehingga maknanya sama dengan
pinning pada Zulip.

* Mention/@Mention - Singgung

The word singgung is the most appropriate word to use in the context of Zulip
because the meaning of singgung is similar with mention in Zulip. There are
other alternatives: Sebut, Saut, Seru, Panggilan. But the word sebut, saut, and
seru does not reflect the true meaning of the mention itself.

Mention in Zulip functions as some type of notification to someone when their
name is notified in a conversation. But changing the word mention to "disebut",
"sebutan", "disaut", "sautan", "diseru", "seruan", "dipanggil", or "panggilan",
does not really work well with the word mention in Zulip, so the only choice
left is singgung, where bersinggungan has a meaning: related; has a
connection.

Kata singgung paling cocok digunakan dalam konteks Zulip karena mempunyai arti
yang mirip dengan mention di Zulip. Terdapat alternatif lainnya: Sebut, Saut,
Seru, Panggilan. Namun kata sebut, saut, dan seru tidak merefleksikan arti 
mention yang sebenarnya.

Mention di Zulip mempunyai fungsi untuk memberitahukan seseorang apabila nama
orang tersebut ada disebut dalam suatu percakapan. Tetapi menggantikan kata
mention menjadi "disebut", "sebutan", "disaut", "sautan", "diseru", "seruan",
"dipanggil", atau "panggilan", tidak terlalu cocok dengan kata mention di
Zulip, sehingga satu-satunya pilihan yang ada adalah singgung, dimana
bersinggungan mempunyai salah satu arti kiasan: bersangkut paut; 
ada hubungannya.

* Invalid - Invalid

Example uses: Invalid stream can be translated to siaran invalid, Invalid URL
can be translated to URL invalid. This direct translating won't be a problem.

Contoh penggunaan: Invalid stream dapat diartikan ke siaran invalid. Invalid
URL dapat diartikan ke URL invalid. Penerjemahan langsung tidak akan menjadi
masalah.

* Customization - Pengaturan

Customization in Zulip basically refers to the settings. Settings in Indonesia
is commonly translated to pengaturan. Therefore the use for pengaturan is
justified.

Cutomization pada Zulip secara singkat mengacu pada settings, Settings dalam
bahasa Indonesia biasa diterjemahkan ke pengaturan. Jadi penggunaan kata
pengaturan ini sah sah saja.

* I want - Saya ingin/mau

The word "aku" is **usually** used for a more traditional way of the language
style, while the word saya is used for a more formal way of saying "I" in
Indonesian.

The word ingin/mau can be used interchangably depending on the context in
Zulip. Examples: "I (ingin) to search about...", "Are you (mau) to exit from
Zulip?". Sometimes both word can be used. Choose one that in your opinion 
suits the best.

Kata "aku" **biasanya** dipakai untuk gaya bahasa yang lebih tradisional,
sedangkan kata saya digunakan untuk penggunaan bahasa Indonesia yang
lebih formal.

Kata ingin/mau dapat diganti sesuai konteks yang ada pada Zulip. Contoh: Saya
ingin mencari tentang: ..., Apakah Anda mau keluar dari Zulip?.  Terkadang dua
kata tersebut juga dapat digunakan. Pilih salah satu yang menurut Anda paling
sesuai.

* User - Pengguna

* Person/People - Orang/Orang(-orang)

Example: There are a lot of people in this stream.
Translated: Terdapat banyak orang pada siaran ini.

Example 2: There is only one person in this topic.
Translated: Hanya terdapat satu orang pada topik ini.

There isn't really something to signify plural nouns in Indonesian with one
word. Usually the word is just repeated with a (-), but that can have a
different meaning when used incorrectly.

Tidak ada sesuatu yang menandakan kejamakan pada kata benda dengan satu kata
pada bahasa Indonesia. Biasanya kata ini diulang dengan tanda (-), tapi hal 
ini bisa saja mengubah arti dari kata awal jika digunakan dengan tidak benar.

# Others (Lain-lain)

* He/She -> Dia
Untuk mengartikan seseorang dalam bahasa Inggris ke bahasa Indonesia atau
sebaliknya, sebagai contoh:
(To translate someone from English to Indonesian or reverse, as example:)

> He likes eating food

Gunakan kata dia, tanpa mengindikasikan maskulin/feminin.
(Use the word dia, without indicating masculinity/femininity.)

> Dia suka memakan makanan

* Is/am/are verb

Untuk menggantikan to be, perhatikan panduan berikut:
(To replace a to be, look at these examples:)

> The paper is 10 meters long  
> Kertas tersebut mempunyai panjang 10 meter

> This paper is 10 meters long  
> Kertas ini mempunyai panjang 10 meter

> The paper is thin  
> Kertas tersebut tipis

> This paper in thin  
> Kertas ini tipis

> The paper feels thin  
> Kertas ini terasa tipis

> They are looking for something  
> Mereks sedang mencari sesuatu

> They are tired  
> Mereka lelah

> They feel tired  
> Mereka merasa lelah

Untuk penerapan pada Zulip, perhatikan contoh berikut:
(For the applications in Zulip, look at these examples:)

> The stream is closed  
> Siaran tersebut ditutup

> This stream is closed  
> Siaran ini ditutup

> That stream is closed  
> Siaran itu ditutup

> Bots are designed to enhance user's experience  
> Robot-robot didesain untuk meningkatkan kenyamanan pengguna
