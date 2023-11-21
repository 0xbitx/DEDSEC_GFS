
<p align="center">
<img src="https://www.office1.com/hubfs/Office1%20Blog%20-%20Graphics%20and%20Images/Phishing%20Blog%201.png#keepProtocol", width="500", height="500">
</p>
<h1 align="center"> DEDSEC_GFS</h1>
<h4 align="center">DEDSEC_GFS is a Linux-based Google Form Spammer capable of sending ultra-realistic account information (firstname, lastname, age, address, birthday, phone_number, email and password).</h4>

## DESCRIPTION

DEDSEC_GFS is a Linux-based tool designed for Google Form spamming. This powerful tool is equipped to send ultra-realistic account information, including accessible variables such as firstname, lastname, age, address, birthday, phone_number, email and password. Its capabilities make it a potent option for simulating authentic user submissions on Google Forms."


<h3 align="center"> USABLE VARIABLE</h3>
<div align="center">
   
| variable | Description                |
| :-------- | ------------------------- |
| 1. firstname  |  filipino and english name. |
| 2. lastname  |   filipino and english lastname.|
| 3. age  | calculated age from birthday. |
| 4. address  | philippine cities. |
| 5. birthday | random birthday. |
| 6. phone_number  | philippine phone_number (smart, globe). |
| 7. email | generated from firstname and lastname. |
| 8. password  | generated from firstnane and lastname. |
| 9. random_id | random id |
   
</div>

<h3 align="center"> SPAMMER IMAGE</h3>
<p align="center">
<img src="https://i.imgur.com/5sPcA6e.png", width="900", height="900">
</p>

<h3 align="center"> ACTUAL FORM PAGE</h3>
<p align="center">
<img src="https://i.imgur.com/4yyODIh.png", width="500", height="500">
</p>

### You can replace the code below for your google form url, header and body
```python
            url = "https://docs.google.com/forms/d/e/1FAIpQLSdDXxjytZnmjwOEeMK8PjSJG-shr0UKNPg5nm7dknFi4wGDDg/formResponse"

            headers = {
                "Cookie": "S=spreadsheet_forms=wfdh4NG44Qt2hwbdd8gKy1HHOF2JPQg-T4IlJA9hMEA; COMPASS=spreadsheet_forms=CjIACWuJVzg5xsF0brWfqA0JdroOU1plgvuvL4bvFI6-Q3YX-v7V8o7ZusjHzUb6dfu8-hDQjumqBho0AAlriVezLLHdW7G10dfxpbZXAbZpnIqBnw0OH7Xk-mDbbWo89mJsB0MYxxLv3wS8jPGRoQ==; NID=511=N4043kekB5EkZRRpKKnGx3VpeA2i1-V47i8_3QABGrmdIDIp7Z9MebmM_PcAktcn4S7cjHHbNiuueB683ETlWTb0CAdVFGfARsi-Bvob0n0Ksa6MPCXNhJwEGauWpdXi3hEwHyXqhuPsdDk0KdMGeBC7AE3fNhgmNWe0aNMfFjg",
                "Host": "docs.google.com",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Content-Type': 'application/x-www-form-urlencoded',
                "Origin": "https://docs.google.com",
                "Referer": "https://docs.google.com/forms/d/e/1FAIpQLSdDXxjytZnmjwOEeMK8PjSJG-shr0UKNPg5nm7dknFi4wGDDg/viewform?fbzx=-3065528922530206851",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "X-Client-Data": "CKblygE=",
                'Upgrade-Insecure-Requests':'1'
            }

            body = {
                'entry.1630406277': email,
                'entry.254235199': password,
                'entry.17821565': firstname + ' ' + lastname,
                'entry.699087705': address,
                'entry.509920065': phone_number,
                'fvv': '1',
                'partialResponse': '[null,null,"-3065528922530206851"]',
                'pageHistory': '0',
                'fbzx': '-3065528922530206851'
            }
```
## INSTALLATION 
    * git clone https://github.com/0xbitx/DEDSEC_GFS.git
    * cd DEDSEC_GFS
    * sudo pip3 install pystyle pycryptodome tabulate
    * sudo python3 dedsec_gfs.py

### TESTED ON FOLLOWING
* Kali Linux 
* Parrot OS 
* Ubuntu
  
<h1 align="center"> DISCLAIMER </h1>

<h4 align="center">I'm not responsible for anything you do with this program, so please only use it for good and educational purposes. </h4>
