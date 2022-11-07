# from data.EnCrypt import Decrypt

# print(Decrypt("^2achbdgfe^3dgcahfeb^7bdfehagci&6bfagedch&5hcfdgba$4ibfeca&0dibefca^6ecigbaf","hi"))

fun_name = ["isalnum","isalpha","isascii","isdecimal","isdigit","isidentifier","islower","isnumeric","isprintable"
            ,"isspace"]

code  = ""

for i in fun_name:
    a=f"""def {i}(self,security_key=False): 
            String = Decrypt(self.String,self.Key).{i}()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)"""
    b = f"""print(a.{i}(security_key="hi"))"""
    
    code = code+b+"\n"
    
print(code)