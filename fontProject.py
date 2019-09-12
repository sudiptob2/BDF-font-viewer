import sys
def ReadFile(path):
    f = open(path)   
    AllLines = f.readlines()
    f.close()
    return AllLines

def SearchEncoding(encoding,AllLines):
    index = 0
    flag = -1
    n = len(AllLines)
    while(index<n):
        testLine = AllLines[index]
        if testLine.strip() == encoding:
            flag = 1
            break
        index+=1   
    if flag<0:
        return flag
    return index

def BuildBitMap(index,AllLines):
    start = index+5
    bitmap = list()
    while AllLines[start].strip()!= "ENDCHAR":
        bitmap.append(AllLines[start].strip())
        start+=1
    return bitmap

def hex2bin(str):
   bin = ['0000','0001','0010','0011',
         '0100','0101','0110','0111',
         '1000','1001','1010','1011',
         '1100','1101','1110','1111']
   aa = ''
   for i in range(len(str)):
      aa += bin[int(str[i],base=16)]
   return aa

def displayFont(bitmap):
    n = len(bitmap)
    res = ''
    for i in range(0,7):
        b_data = '00000000'
        if(i<n):
            data = bitmap[i]
            b_data = hex2bin(data)
        for j in range(0,8):
            if(b_data[j]=='1'):
                res+='*'
            else:
                res+='-'
        res+='\n'
    print(res)

def GenerateEncoding(eNumber):
    # This function generates the encoding number in decimal if needed
    # else return the decimal itself
    if eNumber[0]=='0' and eNumber[1]=='X' and len(eNumber)>2:
        eNumber= str(int(eNumber[2:], 16))
    return eNumber
    
    
## Main Body of the programme
    
path = 'ib8x8u.bdf' #Default file
if(len(sys.argv)>1):
    path = sys.argv[1]

#displayFont(bitmap)

while(1):
    AllLines = ReadFile(path)
    eNumber = input("エンコード番号を入力してください ").upper()
    if(eNumber=="Q"):
        break
    eNumber = GenerateEncoding(eNumber)
    encoding = "ENCODING "+eNumber
    index = SearchEncoding(encoding, AllLines)
    if(index>=0):
        message = "エンコード: "+eNumber+" ("+hex(int(eNumber))+")"
        bitmap = BuildBitMap(index,AllLines)
        print(message)
        print("ビットマップ：")
        displayFont(bitmap)
    else:
        print("該当のデータがありません")
        
    

    

            
        
            




