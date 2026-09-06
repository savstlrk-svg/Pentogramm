
from colorama import Fore
import logging
import socket
import asyncio


name_sai = (
    f"{Fore.RED}\n\n\n"
    "• Maigret -- https://github.com/soxoj/maigret\n"
    "• Sherlock Project -- https://github.com/mitmedialab/sherlock-project\n"
    "• RecOSINT Tool -- https://recosint.com\n"
    "• WhatsMyName -- https://whatsmyname.io\n"
    "• Social Links OSINT Framework -- https://osintframework.com\n"
    "• Google Dorks Operator -- https://google.com\n"
)



google_dorks_operators = (
    f"{Fore.RED}\n\n\n"
    "• \"\" (Кавычки) -- Поиск точной фразы\n"
    "• site: -- Поиск только по конкретному сайту или домену\n"
    "• filetype: (или ext:) -- Поиск файлов определенного формата (pdf, docx, xls)\n"
    "• intitle: -- Поиск ключевого слова строго в заголовке страницы\n"
    "• inurl: -- Поиск ключевого слова внутри URL-адреса страницы\n"
    "• intext: -- Поиск ключевого слова строго в тексте страницы\n"
    "• - (Минус) -- Исключение слова или сайта из результатов выдачи\n"
    "• OR (или |) -- Логическое 'ИЛИ' для поиска одного из нескольких вариантов\n"
    "• * (Звёздочка) -- Подстановка любого неизвестного слова (placeholder)\n"
)



username_search_tools = (
    f"{Fore.RED}\n\n\n"
    "• Maigret -- https://github.com/soxoj/maigret\n"
    "• Blackbird -- https://github.com/p1ngul1n0/blackbird\n"
    "• GitFive -- https://github.com/mxrch/GitFive\n"
)




iot_search_engines = (
    f"{Fore.RED}\n\n\n"
    "• Shodan -- https://shodan.io\n"
    "• Netlas -- https://netlas.io\n"
    "• Censys -- https://censys.io\n"
    "• ZoomEye -- https://zoomeye.org\n"
    "• FOFA -- https://fofa.info\n"
    "• Criminal IP -- https://criminalip.io\n"
    "• GreyNoise -- https://greynoise.io\n"
    "• LeakIX -- https://leakix.net\n"
)

osint_data  = (
    f"{Fore.RED}\n\n\n"
    "• PhoneInfoga -- https://github.com/sundowndev/phoneinfoga\n"
    "• PhoneInfoga-Cloud -- https://github.com/AnshumanAtrey/phoneinfoga-phone-osint\n"
    "• PhoneIntel -- https://github.com/phoneintel/phoneintel\n"
    "• PhoneApi -- https://github.com/akrivendev/PhoneApi\n"
    "• DIGI-NETRA -- https://github.com/pwnxotus/DIGI-NETRA\n"
    "• Findigo -- https://github.com/The-Osint-Toolbox/Telephone-OSINT\n"
    "• PhantomTrace -- https://github.com/vabhishek6/PhantomTrace#examples\n"
    "• RedTiger-Tools -- https://github.com/loxy0devlp/RedTiger-Tools\n"
)

osint_data_s =     ("• Epieos -- https://epieos.com\n"
    "• Truecaller-Web -- https://truecaller.com\n"
    "• NumLookup -- https://numlookup.com\n"
    "• PhoneValidator -- https://phonevalidator.com\n"
    "• ThatsThem -- https://thatsthem.com\n"
    "• TruePeopleSearch -- https://truepeoplesearch.com\n"
    "• Whitepages -- https://whitepages.com\n"
    "• USPhonebook -- https://usphonebook.com\n"
    "• Sync.ME -- https://sync.me\n"
    "• ScamSearch -- https://scamsearch.io\n"
    "• HaveIBeenPwned -- https://haveibeenpwned.com\n"
)



osint_data_p_g = (   f"{Fore.RED}\n\n\n"
    "• Holehe -- https://github.com/megadose/holehe\n"
    "• Mosint -- https://github.com/alpkeskin/mosint\n"
    "• Ghunt -- https://github.com/mxrch/GHunt\n"
    "• MailAccess -- https://github.com/KatrielMoses/MailAccess\n"
    "• User-Scanner -- https://github.com/kaifcodec/user-scanner\n"
    "• MailSleuth -- https://github.com/44za12/mailsleuth\n"
    "• Mailogle -- https://github.com/dincertekin/mailogle\n"
    "• Poastal -- https://github.com/jakecreps/poastal\n"
    "• ProtOSINT -- https://github.com/pixelbubble/ProtOSINT\n"
    "• GitSome -- https://github.com/chm0dx/gitSome\n"
    "• Git-Emails -- https://github.com/zcrosman/git-emails\n"
    "• Linkook -- https://github.com/JackJuly/linkook\n"
    "• Infoga -- https://github.com/robertswin/Infoga\n"
    "• EmailHarvester -- https://github.com/maldevel/EmailHarvester\n"
    "• CrossLinked -- https://github.com/m8sec/CrossLinked\n"
    "• H8mail -- https://github.com/khast3x/h8mail\n"
    "• LeakLooker -- https://github.com/woj-ciech/LeakLooker\n"
)
osint_data_p_s =(
    f"{Fore.RED}\n[+] КАТАЛОГ ПОЛНОСТЬЮ БЕСПЛАТНЫХ ВЕБ-САЙТОВ (EMAIL OSINT):\n\n"
    "• Epieos -- https://epieos.com\n"
    "• HaveIBeenPwned -- https://haveibeenpwned.com\n"
    "• Phonebook -- https://phonebook.cz\n"
    "• MXToolbox -- https://mxtoolbox.com\n"
    "• EmailFormat -- https://emailformat.com\n"
    "• Skymem -- https://skymem.info\n"
    "• Email-Checker -- https://email-checker.net\n"
    "• Hunter-Free -- https://hunter.io\n"
    "• Snov-Free -- https://snov.io\n"
)


print(f"{Fore.RED}""""                                                        
                   ██                                    ██                   
                    ███                                ███                    
                     █████                          █████                     
                     ███████                      ███████                     
                      ██   ████                ████   ██                      
                       ██    ████            ████    ██                       
                       ███      ████      ████       ██                       
                        ██        ████  ████        ██                        
                        ███         ██████         ███                        
                         ██       ██████████       ██                         
                         ███    ████      ████    ███                         
                          ████████          ████████                          
                          █████                █████                          
                        ██████                  ██████                        
                      ████  ██                  ██  ████                      
                   ████     ███                ███     ████                   
                █████        ███              ███        █████                
              ████            ██              ██            ████              
           █████              ███            ███              █████           
         ████████████████████████████████████████████████████████████         
                                ██          ██                                
                                ███        ███                                
                                 ██        ██                                 
                                 ███      ███                                 
                                  ██      ██                                  
                                  ███    ███                                  
                                   ███  ███                                   
                                    ██  ██                                    
                                    ██████                                    
                                     ████                                     
                                     ████                                     
                                      ██  """"")
                                                 #название/\  и  \/
print(f"""{Fore.RED}
ooooooooo.   oooooooooooo ooooo      ooo ooooooooooooo   .oooooo.     .oooooo.    ooooooooo.         .o.       ooo        ooooo ooo        ooooo
`888   `Y88. `888'     `8 `888b.     `8' 8'   888   `8  d8P'  `Y8b   d8P'  `Y8b   `888   `Y88.      .888.      `88.       .888' `88.       .888'
 888   .d88'  888          8 `88b.    8       888      888      888 888            888   .d88'     .8"888.      888b     d'888   888b     d'888 
 888ooo88P'   888oooo8     8   `88b.  8       888      888      888 888            888ooo88P'     .8' `888.     8 Y88. .P  888   8 Y88. .P  888 
 888          888    "     8     `88b.8       888      888      888 888     ooooo  888`88b.      .88ooo8888.    8  `888'   888   8  `888'   888 
 888          888       o  8       `888       888      `88b    d88' `88.    .88'   888  `88b.   .8'     `888.   8    Y     888   8    Y     888 
o888o        o888ooooood8 o8o        `8      o888o      `Y8bood8P'   `Y8bood8P'   o888o  o888o o88o     o8888o o8o        o888o o8o        o888o
""")
print(f"{Fore.RED}==========  1 SKAN ПORTOV, 2 KАТАLОG IНSТРYМЕNТОV==========")

try:
    Us_1 = int(input(f"{Fore.RED}Vаш Vыбоr:   "))
except ValueError:
    print(f"{Fore.RED}[-]Напишите ваш выбор цифрами!")
    Us_1 = None

if Us_1 == 2:
    print(f"{Fore.RED}Кakiе iнsтrумeнtы vам нuжны?")
    print(f"{Fore.RED} 1-пробиiv по tеlефонy    2-проbiv по почtе     3-пrобiv по ФИО   4-поisк mеstноsti по fото  5-gaйд nа Google DORK 6-поisковiк по уstrойсtvаm 7-пробив по нику")

    try:
        Us_2 = int(input(f"{Fore.RED}Vаш vыбоr:   "))
    except ValueError:
        print(f"{Fore.RED}[-]Напишите ваш выбор цифрами!")
        Us_2 = None

    if Us_2 == 1:
        print(f"{Fore.RED}Вам что?       1-github 2-сайты")
        try:
            Us_3 = int(input("Ваш выбор:   "))
        except ValueError:
            print(f"{Fore.RED}[-]Напишите ваш выбор цифрами!")
            Us_3 = None
        if Us_3 == 1:
            print(osint_data)
        if Us_3 == 2:
            print(osint_data_s)

    if Us_2 == 2:
        print(f"{Fore.RED}Вам как 1-github  2-сайты")
        try:
            Us_4 = int(input(f"{Fore.RED}Ваш выбор:"))
        except ValueError:
            print(f"{Fore.RED}[-]Напишите ваш выбор цифрами!")
            Us_4 = None
        if Us_4 == 1:
            print(osint_data_p_g)
        if Us_4 == 2:
            print(osint_data_p_s)

    if Us_2 == 3:
        print(name_sai)

    if Us_2 == 4:
        print(f"{Fore.RED}\n\n\n"
              f"Cloud\n"
              f"Google\n"
              f"Gemeni\n"
              f"Yandex MAP\n"
              f"Google MAP\n")

    if Us_2 == 5:
        print(f"{Fore.RED} Смотри когда нам надо найти человека с помощю Google-Dork и чтобы это сделать нам надо правильно со специальными знаками составить вопрос в поисковую строку ниже привидены знаки и премер")
        print(google_dorks_operators)

    if Us_2 == 6:
        print(iot_search_engines)

    if Us_2 == 7:
        print(username_search_tools)

if Us_1 == 1:
    Us_5 = input(f"{Fore.RED}Введите URL:   ")
    async def skan(loop, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(False)
        try:
            await asyncio.wait_for(loop.sock_connect(s, (host, port)), timeout=1)
            print(f"{Fore.GREEN}[+] порт {port} открыт")
        except:
            print(f"{Fore.RED}[-] порт {port} закрыт ")
        finally:
            s.close()


    async def main():
        host = Us_5
        ports = [1, 3, 4, 6, 7, 9, 13, 17, 19, 20, 21, 22, 23, 24, 25,
                 26, 30, 32, 33, 37, 42, 43, 49, 53, 70, 79, 80, 81, 82, 83,
                 84, 85, 88, 89, 90, 99, 100, 106, 109, 110, 111, 113, 119, 125, 135,
                 139, 143, 144, 146, 161, 163, 179, 199, 211, 212, 222, 254, 255, 256, 259,
                 264, 280, 301, 306, 311, 340, 366, 389, 406, 407, 416, 417, 425, 427, 443,
                 444, 445, 458, 464, 465, 481, 497, 500, 512, 513, 514, 515, 524, 541, 543,
                 544, 545, 548, 554, 555, 563, 587, 593, 616, 617, 625, 631, 636, 646, 648,
                 666, 667, 668, 683, 687, 691, 700, 705, 711, 714, 720, 722, 726, 749, 765,
                 777, 783, 787, 800, 801, 808, 843, 873, 880, 888, 898, 900, 901, 902, 903,
                 911, 912, 981, 987, 990, 992, 993, 995, 999, 1000, 1001, 1002, 1007, 1009, 1010,
                 1011, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034,
                 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049,
                 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064,
                 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079,
                 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1093, 1094, 1096,
                 1097, 1098, 1099, 1100, 1104, 1106, 1107, 1108, 1110, 1111, 1112, 1114, 1117, 1119, 1122,
                 1124, 1131, 1138, 1148, 1151, 1152, 1169, 1175, 1183, 1186, 1199, 1201, 1218, 1234, 1247,
                 1248, 1271, 1272, 1296, 1310, 1311, 1334, 1352, 1417, 1433, 1434, 1443, 1455, 1461, 1494,
                 1500, 1501, 1503, 1521, 1524, 1533, 1580, 1600, 1666, 1687, 1700, 1717, 1718, 1720, 1723,
                 1755, 1761, 1782, 1783, 1801, 1840, 1862, 1863, 1864, 1900, 1935, 1947, 1984, 1998, 1999,
                 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2013, 2020, 2021, 2022,
                 2030, 2033, 2034, 2035, 2038, 2040, 2041, 2042, 2043, 2045, 2046, 2047, 2048, 2049, 2065,
                 2068, 2100, 2103, 2105, 2106, 2107, 2111, 2119, 2121, 2126, 2135, 2144, 2160, 2161, 2179,
                 2190, 2191, 2222, 2251, 2260, 2301, 2323, 2381, 2383, 2393, 2394, 2399, 2401, 2492, 2500,
                 2522, 2525, 2601, 2602, 2604, 2605, 2607, 2608, 2638, 2701, 2702, 2717, 2718, 2725, 2809,
                 2811, 2869, 2875, 2909, 2967, 2998, 3000, 3001, 3003, 3005, 3006, 3011, 3017, 3030, 3031,
                 3052, 3071, 3077, 3128, 3168, 3211, 3221, 3260, 3261, 3268, 3269, 3283, 3300, 3301, 3306,
                 3322, 3323, 3324, 3325, 3333, 3351, 3367, 3369, 3370, 3371, 3372, 3389, 3390, 3404, 3476,
                 3493, 3517, 3527, 3546, 3551, 3580, 3659, 3689, 3690, 3703, 3737, 3766, 3784, 3800, 3801,
                 3809, 3814, 3826, 3827, 3828, 3851, 3869, 3871, 3878, 3880, 3889, 3905, 3914, 3918, 3920,
                 3945, 3971, 3986, 3995, 3998, 4000, 4001, 4002, 4003, 4004, 4005, 4006, 4045, 4111, 4125,
                 4126, 4129, 4224, 4242, 4279, 4321, 4343, 4443, 4444, 4445, 4446, 4449, 4550, 4567, 4662,
                 4848, 4899, 4900, 4998, 5000, 5001, 5002, 5003, 5004, 5009, 5030, 5033, 5050, 5051, 5054,
                 5060, 5061, 5080, 5087, 5100, 5101, 5102, 5120, 5190, 5200, 5214, 5221, 5222, 5225, 5226,
                 5269, 5280, 5298, 5357, 5405, 5414, 5431, 5432, 5440, 5500, 5510, 5544, 5550, 5555, 5560,
                 5566, 5631, 5633, 5666, 5678, 5679, 5718, 5730, 5800, 5801, 5802, 5810, 5811, 5815, 5822,
                 5825, 5850, 5859, 5862, 5877, 5900, 5901, 5902, 5903, 5904, 5906, 5907, 5910, 5911, 5915,
                 5922, 5925, 5950, 5952, 5959, 5960, 5961, 5962, 5963, 5985, 5986, 5987, 5988, 5989, 5998,
                 5999, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 6009, 6025, 6059, 6100, 6101, 6106,
                 6112, 6123, 6129, 6156, 6346, 6389, 6502, 6510, 6543, 6547, 6565, 6566, 6567, 6580, 6646,
                 6666, 6667, 6668, 6669, 6689, 6692, 6699, 6779, 6788, 6789, 6792, 6839, 6881, 6901, 6969,
                 7000, 7001, 7002, 7004, 7007, 7019, 7025, 7070, 7100, 7103, 7106, 7200, 7201, 7402, 7435,
                 7443, 7496, 7512, 7625, 7627, 7676, 7741, 7777, 7778, 7800, 7911, 7920, 7921, 7937, 7938,
                 7999, 8000, 8001, 8002, 8007, 8008, 8009, 8010, 8011, 8021, 8022, 8031, 8042, 8045, 8080,
                 8081, 8082, 8083, 8084, 8085, 8086, 8087, 8088, 8089, 8090, 8093, 8099, 8100, 8180, 8181,
                 8192, 8193, 8194, 8200, 8222, 8254, 8290, 8291, 8292, 8300, 8333, 8383, 8400, 8402, 8443,
                 8500, 8600, 8649, 8651, 8652, 8654, 8701, 8800, 8873, 8888, 8899, 8994, 9000, 9001, 9002,
                 9003, 9009, 9010, 9011, 9040, 9050, 9071, 9080, 9081, 9090, 9091, 9099, 9100, 9101, 9102,
                 9103, 9110, 9111, 9200, 9207, 9220, 9290, 9415, 9418, 9485, 9500, 9502, 9503, 9535, 9575,
                 9593, 9594, 9595, 9618, 9666, 9876, 9877, 9878, 9898, 9900, 9917, 9929, 9943, 9944, 9968,
                 9998, 9999, 10000, 10001, 10002, 10003, 10004, 10009, 10010, 10012, 10024, 10025, 10082, 10180, 10215,
                 10243, 10566, 10616, 10617, 10621, 10626, 10628, 10629, 10778, 11110, 11111, 11967, 12000, 12174,
                 12265,
                 12345, 13456, 13722, 13782, 13783, 14000, 14238, 14441, 14442, 15000, 15002, 15003, 15004, 15660,
                 15742,
                 16000, 16001, 16012, 16016, 16018, 16080, 16113, 16992, 16993, 17877, 17988, 18040, 18101, 18988,
                 19101,
                 19283, 19315, 19350, 19780, 19801, 19842, 20000, 20005, 20031, 20221, 20222, 20828, 21571, 22939,
                 23502,
                 24444, 24800, 25734, 25735, 26214, 27000, 27352, 27353, 27355, 27356, 27715, 28201, 28211, 29672,
                 29831,
                 30000, 30005, 30704, 30718, 30951, 31038, 31337, 31727, 32768, 32769, 32770, 32771, 32772, 32773,
                 32774,
                 32775, 32776, 32777, 32778, 32779, 32780, 32781, 32782, 32783, 32784, 32785, 32791, 32792, 32803,
                 32816,
                 32822, 32835, 33354, 33453, 33554, 33899, 34571, 34572, 34573, 35500, 35513, 37839, 38185, 38188,
                 38292,
                 39136, 39376, 39659, 40000, 40193, 40811, 40911, 41064, 41511, 41523, 42510, 44176, 44442, 44443,
                 44501,
                 44709, 45100, 46200, 46996, 47544, 48080, 49152, 49153, 49154, 49155, 49156, 49157, 49158, 49159,
                 49160,
                 49161, 49163, 49164, 49165, 49167, 49168, 49171, 49175, 49176, 49186, 49195, 49236, 49400, 49401,
                 49999,
                 50000, 50001, 50002, 50003, 50006, 50050, 50300, 50389, 50500, 50636, 50800, 51103, 51191, 51413,
                 51493,
                 52660, 52673, 52710, 52735, 52822, 52847, 52848, 52849, 52850, 52851, 52853, 52869, 53211, 53313,
                 53314,
                 53535, 54045, 54328, 55020, 55055, 55056, 55555, 55576, 55600, 56737, 56738, 57294, 57665, 57797,
                 58001,
                 58002, 58080, 58630, 58632, 58838, 59110, 59200, 59201, 59202, 60020, 60123, 60146, 60443, 60642,
                 61532,
                 61613, 61900, 62078, 63331, 64623, 64680, 65000, 65129, 65310, 65389,
                 ]
        loop = asyncio.get_running_loop()
        await asyncio.gather(*[skan(loop, host, port) for port in ports])


    asyncio.run(main())