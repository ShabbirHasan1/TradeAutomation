from kiteconnect import KiteTicker, KiteConnect
from selenium import webdriver
import time
import os

class KiteCore:

    api_key = "m1qcnaqrds4jp0k3"
    api_secret = "wmdcsqgd33l9912n1ce72h04ymtbcx8j"
    request_token = "F8DHOvBb04LcTJ3kxYVQJz5mGpYNIHSp"
    access_token = "7eoFrhlLF9ZzhmzCM58A0TCl7NYjzQ3d"
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
        service = webdriver.chrome.service.Service('C:\\Users\\320067000\\OneDrive - Philips\\Desktop\\market\\Automation\\DBPlugIn\\KiteCore\\chromedriver.exe')
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
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input').send_keys("VY9919")
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input').send_keys("Sake#1997")
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input').send_keys("560004")
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




         
        


         
        
            







        
        
  
        
        

