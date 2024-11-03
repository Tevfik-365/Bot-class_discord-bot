import discord
import random
import traceback
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.event
async def on_command_error(ctx, error):
    # Hata mesajını özelleştirebilir veya detaylandırabilirsiniz
    error_message = f"Oops! Bir şeyler ters gitti! 😅 \nHata: {error}"
    
    # Hata mesajını gönder
    await ctx.send(error_message)
    
    # Hata mesajını dosyaya kaydet
    with open('hata_mesajlari.txt', 'a', encoding='utf-8') as f:
        f.write(f"{ctx.command} komutu için hata: {traceback.format_exc()}\n")
@bot.command()
async def merhaba_asker(ctx):
    await ctx.send(f'*Sağol!* Ben {bot.user}, bir Discord KOMANDO botuyum!')
@bot.command()
async def kendini_tanıt(ctx):
    intro = (
        "Ben bir KOMANDO BOTUM, "
        "Senin Emirini dinlemek ve sunmak için buradayım! \n"
    )
    await ctx.send(intro)
@bot.command()
async def birazgülolum(ctx):
    with open(r'm2l1\png-transparent-smile-emoji-face-mouth-perspiration-anxious-face-smiley-emoticon.png', 'rb') as f:
        gulucuk = discord.File(f)
    await ctx.send(file=gulucuk)
@bot.command()
async def Tekmil_ver_asker(ctx):
    await ctx.send(f"Samsun/Tekkeköy SAĞOLUN! {ctx.author.name}")
@bot.command()
async def bayrak_göster_asker(ctx):
    with open(r'm2l1\Unh1OwPF_400x400.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
@bot.command()
async def izmirmarş(ctx):
    with open(r'm2l1\Haluk Levent - İzmir Marşı.mp3', 'rb') as f:
        sarki = discord.File(f)
    await ctx.send(file=sarki)
@bot.command()
async def çanakkalemarş(ctx):
    with open(r'm2l1\Çanakkale içinde aynalı çarşı, ana ben gidiyorum düşmana karşı .....mp3', 'rb') as f:
        çanakkale = discord.File(f)
    await ctx.send(file=çanakkale)
@bot.command()
async def durum_ne_asker(ctx):
    await ctx.send(f"KOMANDO Şu anda {len(bot.guilds)} sunucuda çalışıyor ve {len(bot.users)} kullanıcıya hizmet veriyor KOMUTANIM!")
@bot.command()
async def tarih(ctx):
    bilgiler = [
        "Atatürk, 1881 yılında Selanik'te doğmuştur.",
        "Türkiye Cumhuriyeti, 29 Ekim 1923'te kurulmuştur.",
        "Kurtuluş Savaşı, 1919-1922 yılları arasında gerçekleşmiştir."
    ]
    await ctx.send(random.choice(bilgiler))
@bot.command()
async def deyim(ctx):
    deyimler = [
        "Göz var nizam var: Bir şeyin estetik ve düzen açısından göze hoş göründüğünü belirtir.",
        "Ağaç yaşken eğilir: İnsanların eğitimi genç yaşta yapılmalıdır.",
        "Damlaya damlaya göl olur: Küçük birikimler zamanla büyük sonuçlar doğurur."
    ]
    await ctx.send(random.choice(deyimler))
@bot.command()
async def spor(ctx):
    sporlar = [
        "Galatasaray, Süper Lig'de en fazla şampiyon olan takımlardan biridir.",
        "Fenerbahçe'nin futbol takımı, Türkiye Kupası'nı birçok kez kazandı.",
        "Beşiktaş, 2016-2017 sezonunda Süper Lig'de şampiyon olmuştur."
    ]
    await ctx.send(random.choice(sporlar))
@bot.command()
async def yapay_zeka(ctx):
    yapay_zekalar = [
        "Gelişmiş Yapay Zeka: Yapay zeka, makine öğrenimi ve derin öğrenme teknikleri kullanarak insan benzeri düşünme ve karar verme yeteneklerine sahip olabilir.",
        "İnsansı Robotlar: İnsan davranışlarını taklit edebilen ve çeşitli görevleri yerine getirebilen robotlar, ev işlerinden hizmet sektörüne kadar geniş bir uygulama alanına sahiptir.",
        "Yapay Zeka Tıp: Hastalıkların erken teşhisi ve kişiselleştirilmiş tedavi planları oluşturmak için yapay zeka kullanımı artmaktadır."
    ]
    await ctx.send(random.choice(yapay_zekalar))
@bot.command()
async def istiklalmarş(ctx):
    with open(r'm2l1\İstiklal Marşı.mp3', 'rb') as f:
        mars = discord.File(f)
    await ctx.send(file=mars)
@bot.command()
async def atam(ctx):
    with open(r'm2l1\Ataturk.jpg', 'rb') as f:
        resim = discord.File(f)
    await ctx.send(file=resim)
@bot.command()
async def türkiyegif(ctx):
    gif_urls = [
        "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmQ2Y2JiZHhuNTJsMnlpcWs3emRmeWRncjdueWI0eTA0a3k5OWF3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6czwhfugNpJH7SaXti/giphy.gif",
        "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdml6cGludm04NHd1bXhxeWUyNzQ5b3hyY3MxaGM0cDk2YnA0cDd2dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hoqyLGyEVBf0tOY8SB/giphy.gif"
    ]
    for url in gif_urls:
        await ctx.send(url)
@bot.command()
async def kahramanlar(ctx):
    kahramanlar = [
        "Mustafa Kemal Atatürk: Türkiye Cumhuriyeti'nin kurucusu.",
        "Kurtuluş Savaşı'nda savaşan tüm kahramanlarımız.",
        "Fatih Sultan Mehmet: İstanbul'u fethederek Bizans İmparatorluğu'na son veren padişah."
    ]
    await ctx.send(random.choice(kahramanlar))
@bot.command()
async def renk(ctx):
    renkler = ["Kırmızı", "Mavi", "Yeşil", "Sarı", "Mor"]
    renk = random.choice(renkler)
    await ctx.send(f'Bugünün rengi: {renk}! Bu renk senin için ne ifade ediyor?')
@bot.command()
async def günün_bilgisi(ctx):
    bilgiler = [
        "Dünyada her yıl yaklaşık 8 milyon ton plastik okyanuslara karışıyor.",
        "Bir insan ömrü boyunca ortalama 25.000 ila 30.000 kez nefes alır.",
        "Kediler, insanlardan daha fazla kas hücresine sahiptir.",
        "Futbol oyuncularının çoğu, bir maç sırasında ortalama 11 km koşar.",
        "Yalnızca tavşanlar ve papağanlar, kafalarını çevirmeden arkalarını görebilir.",
        "Titanik, suya girdiğinde, 15.000 ton suyu anında çekmiştir.",
        "Ortalama bir insan yılda 1460'tan fazla rüya görür.",
        "İnsan vücudundaki kemiklerin 4'te 1'i ayaklardadır.",
        "Dünyanın en derin noktası Mariana Çukuru'dur, 11.034 metre derinliğindedir.",
        "Nebraska'da gerçek flamingolardan daha fazla plastik flamingo bulunmaktadır.",
        "Bir insanın kalbi, yaşamı boyunca yaklaşık 3 milyar kez atar.",
        "Dünyada her beş yetişkinden biri, uzaylıların yaşadığına inanıyor.",
        "Bir insan ortalama 7 dakikada uykuya dalar.",
        "Mavi rengi görebilen tek kuş türü baykuştur.",
        "Kış aylarında, penguenler 100 km'ye kadar yüzebilirler.",
        "Dünyada her gün yaklaşık 2.5 milyar kahve fincanı tüketilmektedir."
    ]
    
    await ctx.send(random.choice(bilgiler))
@bot.command()
async def söz(ctx):
    sözler = [
        "Başarı, çoğu zaman azim ve çalışkanlığın sonucudur.",
        "Her şey yolunda gitmese bile, devam etmek önemlidir.",
        "Hayallerinizin peşinden gidin, onlar sizi yönlendirecektir."
    ]
    await ctx.send(random.choice(sözler))
@bot.command()
async def nasılsın(ctx):
    cevaplar = [
        "Harikayım, teşekkür ederim! 😄",
        "Biraz yorgunum, ama iyiyim! 😊",
        "Muhteşemim! Sen nasılsın? 😎"
    ]
    await ctx.send(random.choice(cevaplar))
@bot.command()
async def yazıtura(ctx):
    sonuc = random.choice(['Yazı', 'Tura'])
    await ctx.send(f'Sonuç: {sonuc}!')
@bot.command()
async def seninresmin(ctx):
    await ctx.send(bot.user.avatar.url)
@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Evet, Tevfiğin botu çok havalı.')
@bot.command()
async def Bilgiliymişsin_Asker(ctx):
    await ctx.send("SAĞOLUN KOMUTANIM")

bot.run("TOKEN")
