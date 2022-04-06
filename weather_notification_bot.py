import requests
from bs4 import BeautifulSoup
import pandas as pd
#import time as t
#import re

def job1():
  
  city = ["Bangkok","Chonburi","Rayong","Chiangmai","Khonkaen","Nakhorn ratchasima",
        "Pathumthani","Nakhonpathom","Nonthaburi","Samutprakarn","Samutsakorn","Phuket","Songkla","Lopburi","Nakhon si thammarat"]
  # creating url and requests instance

  city_ = list()
  temp_ = list()
  time_ = list()
  weather = list()

  for i in range(0,len(city)):
    url = "https://www.google.com/search?hl=en&q="+"weather"+city[i]
    #url = "https://www.google.com/search?q="+city[i]+"weather&rlz=1C1GCEA_enTH983TH983&sxsrf=APq-WBvmegDCCDXETOgfvAyE6bg8CgZjCQ%3A1648801966794&ei=rrhGYu6FMN6fseMPnJW_kAc&oq=bangkok&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIMCC4QyAMQsAMQQxgCMg8ILhDUAhDIAxCwAxBDGAIyDAguEMgDELADEEMYAjIPCC4Q1AIQyAMQsAMQQxgCSgQIQRgASgQIRhgBUABYAGCdB2gBcAF4AIABAIgBAJIBAJgBAMgBEMABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz"
    html = requests.get(url).content
    
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    
    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    
    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]


    city_.append(city[i])
    temp_.append(temp)
    time_.append(time)
    weather.append(sky)

  df1 = pd.DataFrame(zip(city_,temp_,time_,weather),columns=['city','temperature','time','weather'])
  #df1 = df1[df1['weather'].str.contains('rain|thunderstroms|mist|cloudy')]
  df1

    #ข้อความ
  def lineNotify(message):
      payload = {'message':message,}
      return _lineNotify(payload)

  #สติกเกอร์
  def notifySticker(stickerID,stickerPackageID):
      payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
      return _lineNotify(payload)


  #ส่งแจ้งเตือน
  def _lineNotify(payload,file=None):
      import requests
      url = 'https://notify-api.line.me/api/notify'
      token = 'WjmbznOsx1WeKbZgSD4pnZ1zNT3T2YhilArggGdEB6v'
      headers = {'Authorization':'Bearer '+token}
      return requests.post(url, headers=headers , data = payload, files=file)



  #ส่งแจ้งเตือน
  def __lineNotify(a,b,d,
                   a1,b1,d1,
                   a2,b2,d2,
                   a3,b3,d3,
                   a4,b4,d4,
                   a5,b5,d5,
                   a6,b6,d6,
                   a7,b7,d7,
                   a8,b8,d8,
                   a9,b9,d9,
                   a10,b10,d10,
                   a11,b11,d11,
                   a12,b12,d12,
                   a13,b13,d13,
                   a14,b14,d14,
                   file=None):
      import requests
      url = 'https://notify-api.line.me/api/notify'
      token = 'WjmbznOsx1WeKbZgSD4pnZ1zNT3T2YhilArggGdEB6v'
      headers = {'Authorization':'Bearer '+token}
      return requests.post(url, headers=headers , data={'message':['\n========================',
                                                                   '\n',a,b,d,
                                                                   '\n========================',
                                                                   '\n',a1,b1,d1,
                                                                   '\n========================',
                                                                   '\n',a2,b2,d2,
                                                                   '\n========================',
                                                                   '\n',a3,b3,d3,
                                                                   '\n========================',
                                                                   '\n',a4,b4,d4,
                                                                   '\n========================',
                                                                   '\n',a5,b5,d5,
                                                                   '\n========================',
                                                                   '\n',a6,b6,d6,
                                                                   '\n========================',
                                                                   '\n',a7,b7,d7,
                                                                   '\n========================',
                                                                   '\n',a8,b8,d8,
                                                                   '\n========================',
                                                                   '\n',a9,b9,d9,
                                                                   '\n========================',
                                                                   '\n',a10,b10,d10,
                                                                   '\n========================',
                                                                   '\n',a11,b11,d11,
                                                                    '\n========================',
                                                                   '\n',a12,b12,d12,
                                                                      '\n========================',
                                                                   '\n',a13,b13,d13,
                                                                      '\n========================',
                                                                   '\n',a14,b14,d14]},files=file)


  


  def weather_notify(x):
      City = x.city[0]
      #a = {'message':City}
      a = City
      Temperature = x.temperature[0]
      #b = {'message':Temperature}
      b = Temperature
      Time = x.time[0]
      #c = {'message':Time}
      c = Time
      Weather = x.weather[0]
      #d = {'message':Weather}
      d = Weather

      City1 = x.city[1]
      #a = {'message':City}
      a1 = City1
      Temperature1 = x.temperature[1]
      #b = {'message':Temperature}
      b1 = Temperature1
      Time1 = x.time[1]
      #c = {'message':Time}
      c1 = Time1
      Weather1 = x.weather[1]
      #d = {'message':Weather}
      d1 = Weather1


      City2 = x.city[2]
      #a = {'message':City}
      a2 = City2
      Temperature2 = x.temperature[2]
      #b = {'message':Temperature}
      b2 = Temperature2
      Time2 = x.time[2]
      #c = {'message':Time}
      c2 = Time2
      Weather2 = x.weather[2]
      #d = {'message':Weather}
      d2 = Weather2


      City3 = x.city[3]
      #a = {'message':City}
      a3 = City3
      Temperature3 = x.temperature[3]
      #b = {'message':Temperature}
      b3 = Temperature3
      Time3 = x.time[3]
      #c = {'message':Time}
      c3 = Time3
      Weather3 = x.weather[3]
      #d = {'message':Weather}
      d3 = Weather3

      City4 = x.city[4]
      #a = {'message':City}
      a4 = City4
      Temperature4 = x.temperature[4]
      #b = {'message':Temperature}
      b4 = Temperature4
      Time4 = x.time[4]
      #c = {'message':Time}
      c4 = Time4
      Weather4 = x.weather[4]
      #d = {'message':Weather}
      d4 = Weather4


      City5 = x.city[5]
      #a = {'message':City}
      a5 = City5
      Temperature5 = x.temperature[5]
      #b = {'message':Temperature}
      b5 = Temperature5
      Time5 = x.time[5]
      #c = {'message':Time}
      c5 = Time5
      Weather5 = x.weather[5]
      #d = {'message':Weather}
      d5 = Weather5



      City6 = x.city[6]
      #a = {'message':City}
      a6 = City6
      Temperature6 = x.temperature[6]
      #b = {'message':Temperature}
      b6 = Temperature6
      Time6 = x.time[6]
      #c = {'message':Time}
      c6 = Time6
      Weather6 = x.weather[6]
      #d = {'message':Weather}
      d6 = Weather6


      City7 = x.city[7]
      #a = {'message':City}
      a7 = City7
      Temperature7 = x.temperature[7]
      #b = {'message':Temperature}
      b7 = Temperature7
      Time7 = x.time[7]
      #c = {'message':Time}
      c7 = Time7
      Weather7 = x.weather[7]
      #d = {'message':Weather}
      d7 = Weather7


      City8 = x.city[8]
      #a = {'message':City}
      a8 = City8
      Temperature8 = x.temperature[8]
      #b = {'message':Temperature}
      b8 = Temperature8
      Time8 = x.time[8]
      #c = {'message':Time}
      c8 = Time8
      Weather8 = x.weather[8]
      #d = {'message':Weather}
      d8 = Weather8


      City9 = x.city[9]
      #a = {'message':City}
      a9 = City9
      Temperature9 = x.temperature[9]
      #b = {'message':Temperature}
      b9 = Temperature9
      Time9 = x.time[9]
      #c = {'message':Time}
      c9 = Time9
      Weather9 = x.weather[9]
      #d = {'message':Weather}
      d9 = Weather9


      City10 = x.city[10]
      #a = {'message':City}
      a10 = City10
      Temperature10 = x.temperature[10]
      #b = {'message':Temperature}
      b10 = Temperature10
      Time10 = x.time[10]
      #c = {'message':Time}
      c10 = Time10
      Weather10 = x.weather[10]
      #d = {'message':Weather}
      d10 = Weather10


      City11 = x.city[11]
      #a = {'message':City}
      a11 = City11
      Temperature11 = x.temperature[11]
      #b = {'message':Temperature}
      b11 = Temperature11
      Time11 = x.time[11]
      #c = {'message':Time}
      c11 = Time11
      Weather11 = x.weather[11]
      #d = {'message':Weather}
      d11 = Weather11

      City12 = x.city[12]
      #a = {'message':City}
      a12 = City12
      Temperature12 = x.temperature[12]
      #b = {'message':Temperature}
      b12 = Temperature12
      Time12 = x.time[12]
      #c = {'message':Time}
      c12 = Time12
      Weather12 = x.weather[12]
      #d = {'message':Weather}
      d12 = Weather12


      City13 = x.city[13]
      #a = {'message':City}
      a13 = City13
      Temperature13 = x.temperature[13]
      #b = {'message':Temperature}
      b13 = Temperature13
      Time13 = x.time[13]
      #c = {'message':Time}
      c13 = Time13
      Weather13 = x.weather[13]
      #d = {'message':Weather}
      d13 = Weather13


      City14 = x.city[14]
      #a = {'message':City}
      a14 = City14
      Temperature14 = x.temperature[14]
      #b = {'message':Temperature}
      b14 = Temperature14
      Time14 = x.time[14]
      #c = {'message':Time}
      c14 = Time14
      Weather14 = x.weather[14]
      #d = {'message':Weather}
      d14 = Weather14


      return __lineNotify(a,b,d,
                        a1,b1,d1,
                        a2,b2,d2,
                        a3,b3,d3,
                        a4,b4,d4,
                        a5,b5,d5,
                        a6,b6,d6,
                        a7,b7,d7,
                        a8,b8,d8,
                        a9,b9,d9,
                        a10,b10,d10,
                        a11,b11,d11,
                        a12,b12,d12,
                        a13,b13,d13,
                        a14,b14,d14)




  lineNotify('Hi, thanks god I brought u an umrealla')

  weather_notify(df1)
  notifySticker(9,1)
  #weather_notify2(df1)
  #weather_notify3(df1)
  #weather_notify4(df1)
  #weather_notify5(df1)
  #weather_notify6(df1)
  #weather_notify7(df1)
  #weather_notify8(df1)
  
  return(df1)
  # printing all data
  #print("City is", city[i])
  #print("Temperature is", temp)
  #print("Time: ", time)
  #print("Sky Description: ", sky)
  #print(other_data)
 
# enter city name
city = ["Bangkok","Chonburi","Rayong","Chiangmai","Khonkaen","Nakhorn ratchasima",
        "Pathumthani","Nakhonpathom","Nonthaburi","Samutprakarn","Samutsakorn","Phuket","Songkla","Lopburi","Nakhon si thammarat"]
 
# creating url and requests instance
#url = "https://www.google.com/search?q="+"weather"+city

city_ = list()
temp_ = list()
time_ = list()
weather = list()

for i in range(0,len(city)):
  url = "https://www.google.com/search?hl=en&q="+"weather"+city[i]
  #url = "https://www.google.com/search?q="+city[i]+"weather&rlz=1C1GCEA_enTH983TH983&sxsrf=APq-WBvmegDCCDXETOgfvAyE6bg8CgZjCQ%3A1648801966794&ei=rrhGYu6FMN6fseMPnJW_kAc&oq=bangkok&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIMCC4QyAMQsAMQQxgCMg8ILhDUAhDIAxCwAxBDGAIyDAguEMgDELADEEMYAjIPCC4Q1AIQyAMQsAMQQxgCSgQIQRgASgQIRhgBUABYAGCdB2gBcAF4AIABAIgBAJIBAJgBAMgBEMABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz"
  html = requests.get(url).content
  
  # getting raw data
  soup = BeautifulSoup(html, 'html.parser')
  temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
  str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

  # formatting data
  data = str.split('\n')
  time = data[0]
  sky = data[1]
  
  # getting all div tag
  listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
  strd = listdiv[5].text
  
  # getting other required data
  pos = strd.find('Wind')
  other_data = strd[pos:]


  city_.append(city[i])
  temp_.append(temp)
  time_.append(time)
  weather.append(sky)

df1 = pd.DataFrame(zip(city_,temp_,time_,weather),columns=['city','temperature','time','weather'])
#df1 = df1[df1['weather'].str.contains('rain|thunderstroms|mist|cloudy')]
df1

  








a = weather
#b = [x.lower() for x in a]
#r = re.compile(".*rain|.*thunder|.*mist|.*showers")
#newlist = list(filter(r.match, b)) # Read Note below
 
if len(a) > 0:
  job1()
else:
    'stop'
