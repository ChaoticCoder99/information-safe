_tuple = ('q','w','i','o','p','a', 's','d','f','g','h', 'j', 'X','C','V','B','N',
          'k','l','z','x','c','v', 'b','n','m','Q','W', 'E', 'R','T','Y','U',
          'O','P','A','S','e','r', 't','y','u','D','F', 'G', 'H','J','K','L',
          '6','7','8','~',"'",'!', '@','1','2','9','0', '.', '/',';','[',']',
          '-','=','#','$','%','^', '&','*','(',')','{', '}', ' ','3','4','5',
          ':','<','>','?','"','`','\\','|','+','_',',',"\n","\t",'M','Z','I',
          )

def encrypt(text):
    output = []
    dictionary = {_tuple[i]:i for i in range(len(_tuple))}
    for i in text:
        output.append(dictionary[i])
    return bytearray(output)

def decrypt(text):
    output = ''
    text = tuple(text)
    dictionary = {i:_tuple[i] for i in range(len(_tuple))}
    for i in text:
        output += dictionary[i]
    return output