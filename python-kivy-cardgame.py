
from kivy.lang              import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window       import Window
from kivy.uix.widget        import Widget
from kivy.uix.boxlayout     import BoxLayout
from kivy.app               import App
from kivy.uix.label         import Label
from kivy.uix.button        import Button
from kivy.uix.image         import Image
import os
import time
import random



Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        orientation: "vertical"
        padding: 150
        spacing: 80
        Label:
            text: "MERHABA CARD OYUNUNA HOŞ GELDİNİZ"
            bold: True
        Label:
            text: "OLASILIKSAL CARD OYUNU"
            bold: True
        Button:
            text: "Oyuna başlamak için tıklayınız"
            on_press:
                root.manager.transition.direction = 'down'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
<ScreenTwo>:
    BoxLayout:
        orientation: "vertical"
        #ust sekme
        ActionBar:
            ActionView:
                ActionPrevious:
                    title: "ANA EKRANA DON"
                    on_press:
                        root.oyunrestart()
                        root.manager.transition.direction = 'down'
                        root.manager.current = 'screen_one'                   
        BoxLayout:    
        BoxLayout:
            spacing: 10
            Label:
            Label:
            Button:
                id: at1
                size_hint: .6,1.8 
                on_press: root.kartat1() 
                background_normal: ""
            Button:
                id: at2
                size_hint: .6,1.8
                on_press: root.kartat2() 
                background_normal: ""  
            Button:
                id: at3
                size_hint: .6,1.8
                on_press: root.kartat3() 
                background_normal: ""   
            Button:
                id: at4
                size_hint: .6,1.8
                on_press: root.kartat4() 
                background_normal: ""   
            Button:
                id: at5
                size_hint: .6,1.8
                on_press: root.kartat5() 
                background_normal: ""   
            Label:
            Label:
        BoxLayout:       
        BoxLayout:
            spacing: 10
            Label: 
            Label:
            Label:
            ########## sırayla sec1 sec2 sec3 buttonları################
            Button:
                id: sec1
                size_hint: .7,1.8  
                background_normal: ""   
            Button:
                id: sec2
                size_hint: .7,1.8  
                background_normal: ""   
            Button:
                id: sec3
                size_hint: .7,1.8  
                background_normal: ""   
            Label:
            #anlık skor yerine pop uc mesajı eklencek
            Label:
            Label:
        BoxLayout:
        BoxLayout:
            padding: 22
            Label:
            Button:
                id: kartver
                size_hint: 0.75,3
                text: "KartverButonu"
                on_press: root.kartver24()
            Label:
                id: kalankartlabel
                text: "24"
            Label:
                text: "Toplam Puan"
            Label:
                id:   puanlama
                text: "0"
            Label:
            Label:
            Label:
            Button:
                id: kartsil
                size_hint: 0.75,3
                text: "kartsil"
                on_press: root.sec1sec2sec3kartsil()
            Label:
        BoxLayout:
            Label:        
            Label:
                size_hint: .95,.82
                text: "Dokunarak Kart at "
            Label:
            Label:
            #Label:
            Button:
                id: yenioyun
                text: "Yenı oyun"
                on_press: root.oyunrestart()
            Label:
            Label:
            Label:
            Label:
        BoxLayout:
            Button:
                size_hint: .4, .5
                text: "Oyun Hakkında bilgi"
""")


class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):

    path = 'C:/Users/asus/Desktop/KıvyProgrammıng/cardgame/cardresimleri/'
    resimdosyalari  = [ 'k1.jpg', 'k2.jpg', 'k3.jpg', 'k4.jpg', 
                            'k5.jpg', 'k6.jpg', 'k7.jpg', 'k8.jpg',
                            's1.jpg', 's2.jpg', 's3.jpg', 's4.jpg', 
                            's5.jpg', 's6.jpg', 's7.jpg', 's8.jpg',
                            'y1.jpg', 'y2.jpg', 'y3.jpg', 'y4.jpg', 
                            'y5.jpg', 'y6.jpg', 'y7.jpg', 'y8.jpg']

    def kartver24(self):
        if (self.ids.kalankartlabel.text == str(24)):
            path = 'C:/Users/asus/Desktop/KıvyProgrammıng/cardgame/cardresimleri/'
            resimdosyalari  = [ 'k1.jpg', 'k2.jpg', 'k3.jpg', 'k4.jpg', 
                            'k5.jpg', 'k6.jpg', 'k7.jpg', 'k8.jpg',
                            's1.jpg', 's2.jpg', 's3.jpg', 's4.jpg', 
                            's5.jpg', 's6.jpg', 's7.jpg', 's8.jpg',
                            'y1.jpg', 'y2.jpg', 'y3.jpg', 'y4.jpg', 
                            'y5.jpg', 'y6.jpg', 'y7.jpg', 'y8.jpg']

            temp = random.sample(self.resimdosyalari, k=5 )
            print(temp)

            for i in range(5):
                self.resimdosyalari.remove(temp[i])

                print("kaldırılan dosyalar",temp[i])
                self.ids.kalankartlabel.text = str(int(self.ids.kalankartlabel.text) -1 )
            print("Kaldırılan resım dosyası",temp[i])
            print("Resim dosyası listesi",self.resimdosyalari)

            #rastgele 5 kart secımının butonlara  atanması
            sifirlanacaklar = ["at1","at2","at3","at4","at5" ]
            for i in range(len(sifirlanacaklar)):
                getattr(self.ids, sifirlanacaklar[i]).background_normal = self.path + temp[i]
        
        else:
            #bu kartlardan birı bos degılse pop ac mesajı  yapılcak
            self.ilkbessonrasisecilmiskartkontrol() 
    

    def ilk5sonrasıkartsec(self):
        if self.ids.kalankartlabel.text != str(0):
            self.temp5 = random.choice(self.resimdosyalari)
            self.resimdosyalari.remove(self.temp5)
            
            print("Kaldırılan resım dosyası",self.temp5)
            print("Resim dizesi",self.resimdosyalari)
            self.ids.kalankartlabel.text = str(int(self.ids.kalankartlabel.text) - 1 )
        else:
            print("oyun sonuna geldık kart secemezsin") 
    
    def ilkbessonrasikartat(self):
    
        if (self.ids.at1.background_normal  == ""):
           self.ilk5sonrasıkartsec()
           self.ids.at1.background_normal  = self.path + self.temp5
    
        elif self.ids.at2.background_normal  == "":
            self.ilk5sonrasıkartsec()
            self.ids.at2.background_normal  = self.path + self.temp5
    
        elif self.ids.at3.background_normal  == "":
            self.ilk5sonrasıkartsec()
            self.ids.at3.background_normal  = self.path + self.temp5
    
        elif self.ids.at4.background_normal  == "":
            self.ilk5sonrasıkartsec()
            self.ids.at4.background_normal  = self.path + self.temp5
    
        elif self.ids.at5.background_normal  == "":
            self.ilk5sonrasıkartsec()
            self.ids.at5.background_normal  = self.path + self.temp5
        else:
           print("kartsecilemez")
            #gıdakı 3u kontrol edıp ardından diger 5i kontrol et
    
    def ilkbessonrasisecilmiskartkontrol(self):
        #print("ilkbessonrasisecilmiskartkontrol fonskyonuna geldik")
    
        a = self.ids.at1.background_normal[-5:-4]
        b = self.ids.at2.background_normal[-5:-4]
        c = self.ids.at3.background_normal[-5:-4]
        d = self.ids.at4.background_normal[-5:-4]
        e = self.ids.at5.background_normal[-5:-4]
        f = self.ids.sec1.background_normal[-5:-4]
        g = self.ids.sec2.background_normal[-5:-4]
        h = self.ids.sec3.background_normal[-5:-4]
        int = a,b,c,d,e,f,g,h
        #arka plan
        print(a,b,c,d,e,f,g,h)
    
        toplamg = a+b+c+d+e+f+g+h
        print("toplamg",len(toplamg))


        #en fazla 5 kart secmek ıcın kosullar
        if (self.ids.sec1.background_normal == ""):
            if (self.ids.kalankartlabel.text != str(0) and len(toplamg) < 5):
                self.ilkbessonrasikartat()
                print("en fazla 5 kart 1.kosul")
    
        elif(self.ids.sec1.background_normal == ""):
            if (len(toplamg) < 5):
                print("en fazla 5 kart 2.kosul")
            else:
                self.ilkbessonrasikartat()
    
        elif(self.ids.sec3.background_normal == ""):
            if (len(toplamg) < 5):
                print("en fazla 5 kart 3.kosul")
                self.ilkbessonrasikartat()
    
        elif(self.ids.sec1.background_normal != "" and 
            self.ids.sec2.background_normal != "" and
            self.ids.sec3.background_normal != ""):
                if (len(toplamg) <= 2 ):
                    print("butun sec kartlarının dolu oldgu kosul")
                    self.ilkbessonrasikartat()
        else:
            print("Secılmıs 3 kart dolu ve toplam 5 kartınız var")
    
    #kartsile bastıgında sec1 sec2 sec3 sıfırla
    def sec1sec2sec3kartsil(self):
            self.ids.sec1.background_normal = ""
            self.ids.sec2.background_normal = ""
            self.ids.sec3.background_normal = ""
            print("Kart atmak için KARTLAR SİLİNDİ")

    def puanlama(self):
    
        ff = self.ids.sec1.background_normal[-6:-4]
        gg = self.ids.sec2.background_normal[-6:-4]
        hh = self.ids.sec3.background_normal[-6:-4]
        #print(ff,gg,hh)

        #sadece rakamlar ıcın
        fff = self.ids.sec1.background_normal[-5:-4]
        ggg = self.ids.sec2.background_normal[-5:-4]
        hhh = self.ids.sec3.background_normal[-5:-4]
        #print(fff,ggg,hhh)
    
        #Puan hesaplama farklı renkler ıcın, sadece sayı kısımları alındı
        # sarı8 kırmızı8 yeşil 8 == 90 puan
        if (int(fff == ggg == hhh  == str(8)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 90) 
            self.sec1sec2sec3kartsil()
        elif (int(fff == ggg == hhh == str(7)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 80) 
            self.sec1sec2sec3kartsil()
        elif (int(fff == ggg == hhh  == str(6)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 70) 
            self.sec1sec2sec3kartsil()
        elif (int(fff == ggg == hhh  == str(5)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 60) 
            self.sec1sec2sec3kartsil()
        elif (int(fff == ggg == hhh  == str(4)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 50) 
            self.sec1sec2sec3kartsil()
        elif (int(fff == ggg == hhh  == str(3)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 40) 
            self.sec1sec2sec3kartsil()
        elif (int(fff == ggg == hhh  == str(2)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 30) 
            self.sec1sec2sec3kartsil()
        elif (int(fff == ggg == hhh  == str(1)))  :
            self.ids.puanlama.text = str(int(self.ids.puanlama.text) + 20) 
            self.sec1sec2sec3kartsil()
    
    #Button1 den 5 e  secılmıs buton gelen kartları sırayla almak ıcın
    def kartat1(self):
        
        if self.ids.sec1.background_normal == "":
            self.ids.sec1.background_normal = self.ids.at1.background_normal
            self.ids.at1.background_normal = ""
    
        elif self.ids.sec2.background_normal == "":
            self.ids.sec2.background_normal = self.ids.at1.background_normal
            self.ids.at1.background_normal = ""
               
        elif self.ids.sec3.background_normal == "":
           self.ids.sec3.background_normal = self.ids.at1.background_normal
           self.ids.at1.background_normal = ""
        self.puanlama()

    #5 secılmıs buton gelen kartları sırayla almak ıcın
    def kartat2(self):
        
        if self.ids.sec1.background_normal == "":
            self.ids.sec1.background_normal = self.ids.at2.background_normal
            self.ids.at2.background_normal = ""
    
        elif self.ids.sec2.background_normal =="":
            self.ids.sec2.background_normal = self.ids.at2.background_normal
            self.ids.at2.background_normal = ""
    
        elif self.ids.sec3.background_normal == "":
            self.ids.sec3.background_normal = self.ids.at2.background_normal
            self.ids.at2.background_normal = ""
        self.puanlama()

    #5 secılmıs buton gelen kartları sırayla almak ıcın        
    def kartat3(self):
        
        if self.ids.sec1.background_normal == "":
            self.ids.sec1.background_normal = self.ids.at3.background_normal
            self.ids.at3.background_normal = ""
    
        elif self.ids.sec2.background_normal == "":
            self.ids.sec2.background_normal = self.ids.at3.background_normal
            self.ids.at3.background_normal = ""
    
        elif self.ids.sec3.background_normal == "":
            self.ids.sec3.background_normal = self.ids.at3.background_normal
            self.ids.at3.background_normal = ""
        self.puanlama()
    

    #5 secılmıs buton gelen kartları sırayla almak ıcın        
    def kartat4(self):
        
        if self.ids.sec1.background_normal == "":
            self.ids.sec1.background_normal = self.ids.at4.background_normal
            self.ids.at4.background_normal = ""
    
        elif self.ids.sec2.background_normal == "":
            self.ids.sec2.background_normal = self.ids.at4.background_normal
            self.ids.at4.background_normal = ""
    
        elif self.ids.sec3.background_normal == "":
            self.ids.sec3.background_normal = self.ids.at4.background_normal
            self.ids.at4.background_normal = ""
        self.puanlama()

    #5 secılmıs buton gelen kartları sırayla almak ıcın        
    def kartat5(self):
        
        if self.ids.sec1.background_normal == "":
            self.ids.sec1.background_normal = self.ids.at5.background_normal
            self.ids.at5.background_normal = ""
    
        elif self.ids.sec2.background_normal == "":
            self.ids.sec2.background_normal = self.ids.at5.background_normal
            self.ids.at5.background_normal = ""
    
        elif self.ids.sec3.background_normal == "": 
            self.ids.sec3.background_normal = self.ids.at5.background_normal
            self.ids.at5.background_normal = ""
        self.puanlama()

    def oyunrestart(self):
        self.ids.kalankartlabel.text = str(24)
        self.ids.puanlama.text = str(0)
        sifirlanacaklar = ["at1","at2","at3","at4","at5","sec1","sec2","sec3"]
        for i in sifirlanacaklar:
            getattr(self.ids, i).background_normal = ""
        print("yenı oyun için kartlar silindi")

screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))

class KivyTut2App(App):

    def build(self):

        return screen_manager

sample_app = KivyTut2App()
sample_app.run()










#aynırenk 678 100 puan
#aynı renk 567 90 puan
#aynı renk 456 80puan
#aynı renk 345 70 puan
#aynı renk 123 50puan
#farklı 678 60puan
#farklı 567 50
#farklı 456 40
#farklı 345 30 puan
#       234 20
#       123 10

#yapılcak
#farklı renk 888 90
#farklı renk 777 80
#farklı renk 666 70
#farklı renk 555 60
#farklı renk 444 50
#farklı renk 333 40
#farklı renk 222 30
#farklı renk 111 20


