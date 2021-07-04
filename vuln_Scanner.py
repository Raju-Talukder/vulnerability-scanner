import Port_Scanner

targetIp = input('[+] Enter Target To scan: ')
portNum = int(input('[+] Enter amount of port you want to scan: '))
vulnFile = input('[+] Enter file with vulnerable software: ')
print('\n')

target = Port_Scanner.PortScan(targetIp, portNum)
target.scan()

with open(vulnFile,'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: " '+ banner + ' " ON PORT: ' + str(target.openPort[count]))
        count += 1
