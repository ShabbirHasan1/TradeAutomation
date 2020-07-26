from kiteconnect import KiteTicker, KiteConnect
from selenium import webdriver
import time
import os


class KiteCore:

    api_key = "m1qcnaqrds4jp0k3"
    api_secret = "wmdcsqgd33l9912n1ce72h04ymtbcx8j"
    request_token = "z3UeHco0cln1OhFNz0UZmgMBjSaG0oE2"
    access_token = "DYuy9uIKWWV5MGR1SCbaYSuxup3ZT2sm"
    kite=any
    webSocket=any
    sender=any
    InstrumentToken=any
 

    def __init__(self):
        KiteCore.kite = KiteConnect(api_key=KiteCore.api_key)
        if not KiteCore.request_token:
            self.__getRequestToken() 
            print("Request token =" + KiteCore.request_token)
                                   
        if not KiteCore.access_token:
            try:
                self.__getAccessToken()
                print("Access Token =" + KiteCore.access_token)
            except:
                print("access token generation failed")
                exit()

                        
        KiteCore.webSocket=KiteTicker(KiteCore.api_key,KiteCore.access_token)
  
      

    def __getRequestToken(self):        
        service = webdriver.chrome.service.Service('..\\Core\\Utils\\chromedriver.exe')#enter your chrome driver path
        service.start()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') # disable this line to  lauch chrome
        options = options.to_capabilities()
        driver = webdriver.Remote(service.service_url, options)
        driver.get(KiteCore.kite.login_url())
        TimerforAuthorization=8
        TimerforRequestToken=3
        driver.implicitly_wait(TimerforAuthorization)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input').send_keys("")#Enter your Client ID)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input').send_keys("")#Enter your password
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input').send_keys("")#Enter your 2FA
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/button').click()

        except:
            print("Timeout while accessing the initial authorization page. Timer set =" , TimerforAuthorization)
            exit()

        time.sleep(TimerforRequestToken)

        try:
            KiteCore.request_token=driver.current_url.split('request_token=')[1].split('&action')[0]

        except:
            print("Timeout while extracting Request token. Timer set=" , TimerforRequestToken)
            exit()

        driver.quit()



    def __getAccessToken(self):
        data = KiteCore.kite.generate_session(KiteCore.request_token,KiteCore.api_secret)
        KiteCore.access_token = data["access_token"]
            
        

    def on_ticks(self,ws, ticks):
        print("Ticks entered")
        self.sender.on_ticks(ticks)
        print("returning from on ticks: kite core")



    def getQuote(self,instrumentToken, sender):
        try:
            self.sender = sender
            self.InstrumentToken=instrumentToken
            KiteCore.webSocket.on_ticks =self.on_ticks
            KiteCore.webSocket.on_connect = self.on_connect
            KiteCore.webSocket.connect(threaded=True)
            print("websocket subscribed")

        except:
            print("Subscription failed")


        
    def getInstrumentToken(self,exchange):
        try:
            instrument= KiteCore.kite.instruments(exchange=exchange)
            return instrument
        except:
            print("Unidentified exchange")



        
    def getTokenFromName(self,stockName,exchange):
         Tokens=self.getInstrumentToken(exchange)
         for i in Tokens:
             if(i['tradingsymbol']==stockName):
                 return i['instrument_token']

         print("unidentified security/instument name")

    

         
    def FilterInstrument(self,exchange):
        try:
            instrument= KiteCore.kite.instruments(exchange=exchange)
            instrumentlist=[]
            for i in instrument:
                instrumentlist.append(i['tradingsymbol'])
            return instrumentlist
        except:
            print("error in filtering instruments")



    def on_connect(self,ws,response):
        ws.subscribe(self.InstrumentToken)
        ws.set_mode(ws.MODE_FULL, self.InstrumentToken)
        print("Successfully connected to WebSocket")




         
        


         
        
            







        
        
  
        
        

