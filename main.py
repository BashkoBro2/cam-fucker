import os
import colorama
from colorama import Fore
import requests
import re

countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
            "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
            "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
            "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
            "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
            "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
            "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
            "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
            "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
            "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
            "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
            "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
            "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
            "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
            "SY", "TZ", "UG", "UZ", "VC","BJ", ]

banner = f'''{Fore.LIGHTBLUE_EX}
 ██████╗ █████╗ ███╗   ███╗ ██████╗    ███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗████╗ ████║██╔════╝    ██╔════╝██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║██╔████╔██║██║         █████╗  ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██║██║╚██╔╝██║██║         ██╔══╝  ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╗    ██║     ╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝    ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{Fore.RESET}                            {Fore.GREEN}IG : @na2sim_mgll{Fore.RESET}                                                  
'''

pays_banner = f'''
1) United States                31) Mexico                61) Moldova
2) Japan                        32) Finland               62) Nicaragua
3) Italy                        33) China                 63) Malta
4) Korea                        34) Chile                 64) Trinidad And Tobago
5) France                       35) South Africa          65) Soudi Arabia
6) Germany                      36) Slovakia              66) Croatia
7) Taiwan                       37) Hungary               67) Cyprus
8) Russian Federation           38) Ireland               68) Pakistan
9) United Kingdom               39) Egypt                 69) United Arab Emirates
0) Netherlands                  40) Thailand              70) Kazakhstan
1) Czech Republic               41) Ukraine               71) Kuwait
2) Turkey                       42) Serbia                72) Venezuela
3) Austria                      43) Hong Kong             73) Georgia
4) Switzerland                  44) Greece                74) Montenegro
5) Spain                        45) Portugal              75) El Salvador
6) Canada                       46) Latvia                76) Luxembourg
7) Sweden                       47) Singapore             77) Curacao
8) Israel                       48) Iceland               78) Puerto Rico
9) Iran                         49) Malaysia              79) Costa Rica
20) Poland                      50) Colombia              80) Belarus
21) India                       51) Tunisia               81) Albania
22) Norway                      52) Estonia               82) Liechtenstein
23) Romania                     53) Dominican Republic    83) Bosnia And Herzegovia
24) Viet Nam                    54) Sloveania             84) Paraguay
25) Belgium                     55) Ecuador               85) Philippines
26) Brazil                      56) Lithuania             86) Faroe Islands
27) Bulgaria                    57) Palestinian           87) Guatemala
28) Indonesia                   58) New Zealand           88) Nepal
29) Denmark                     59) Bangladeh             89) Peru
30) Argentina                   60) Panama                90) Uruguay
91) Extra                       92) Andorra               93) Antigua And Barbuda
94) Armenia                     95) Angola                96) Australia
97) Aruba                       98) Azerbaijan            99) Barbados
00) Bonaire                     01) Bahamas               02) Botswana
03) Congo                       04) Ivory Coast           05) Algeria
06) Fiji                        07) Gabon                 08) Guernsey
09) Greenland                   10) Guadeloupe            11) Guam
12) Guyana                      13) Honduras              14) Jersey
15) Jamaica                     16) Jordan                17) Kenya
18) Cambodia                    19) Saint Kitts           20) Cayman Islands
21) Laos                        22) Lebanon               23) Sri Lanka
24) Morocco                     25) Madagascar            26) Macedonia
27) Mongolia                    28) Macao                 29) Martinique
30) Mauritius                   31) Namibia               32) New Caledonia
33) Nigeria                     34) Qatar                 35) Reunion
36) Sudan                       37) Senegal               38) Suriname
39) Sao Tome And Principe       40) Syria                 41) Tanzania
42) Uganda                      43) Uzbekistan           44) Saint Vincent And The Grenadines
45) Benin
'''

def main():
    os.system('cls')
    print(banner)
    print(Fore.LIGHTBLUE_EX + pays_banner + Fore.RESET)
    try:
        print()
        countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                    "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                    "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                    "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                    "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                    "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                    "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                    "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                    "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                    "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
                    "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                    "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                    "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                    "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                    "SY", "TZ", "UG", "UZ", "VC","BJ", ]
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

        num = int(input(Fore.LIGHTBLUE_EX + "Select > " + Fore.RESET))
        if num not in range(1, 145+1):
            raise IndexError

        country = countries[num-1]
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        for page in range(int(last_page)):
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
            for ip in find_ip:
                req_cam = requests.get(ip)
                if req_cam.status_code == 200:
                    print(Fore.LIGHTGREEN_EX + ip + " No password needed ! " + Fore.LIGHTGREEN_EX)
                else:
                    print(Fore.RED + ip + " Password needed ! ")
                
    except:
        pass
    finally:
        print("\033[1;37m")
        exit()

main()