from Crypto.Cipher import AES
from tkinter import *

class Application(Frame):
    def Decrypt(self):
        key = self.KeyEntry.get()
        while len(key)%16 != 0:
            key = key + 'x'
        IV = 16 * '\x00'
        mode = AES.MODE_CBC
        encryptor = AES.new(key, mode, IV=IV)

        ciphertext = self.InputText.get("1.0",END)
        while len(ciphertext)%16 != 0:
            ciphertext = ciphertext + 'x'
        '''
        sampleText = 'a'*4+'b'*4+'c'*4+'d'*4
        ciphertext = encryptor.encrypt(sampleText)
        decryptor = AES.new(key, mode, IV=IV)
        plain = decryptor.decrypt(ciphertext)
        '''
        decryptor = AES.new(key, mode, IV=IV)
        plain = decryptor.decrypt(ciphertext)
        self.OutputText.delete(0.0,END)
        self.OutputText.insert(0.0,ciphertext)

    def Encrypt(self):
        key = self.KeyEntry.get()
        while len(key)%16 != 0:
            key = key + 'x'
        IV = 16 * '\x00'
        mode = AES.MODE_CBC
        encryptor = AES.new(key, mode, IV=IV)
        text = self.InputText.get("1.0",END)
        while len(text)%16 != 0:
            text = text + 'x'
        ciphertext = encryptor.encrypt(text)
        self.OutputText.delete(0.0,END)
        self.OutputText.insert(0.0,ciphertext)

    def createWidgets(self):
        ''' Key Entry '''
        self.KeyEntry = Entry(self)
        self.KeyEntry.pack(padx=5, pady=5)
        ''' Input TextBox '''
        self.InputText = Text(root,height = 5,width = 50)
        self.InputText.pack(padx=5, pady=5)
        ''' Output TextBox '''
        self.OutputText = Text(root,height = 5,width = 50)
        self.OutputText.pack(padx=5, pady=5)
        ''' Encryption Button '''
        self.EncryptButton = Button(self)
        self.EncryptButton["text"] = "Encrypt",
        self.EncryptButton["command"] = self.Encrypt
        self.EncryptButton.pack({"side": "left"})
        ''' Decryption Button '''
        self.DecryptButton = Button(self)
        self.DecryptButton["text"] = "Decrypt",
        self.DecryptButton["command"] = self.Decrypt
        self.DecryptButton.pack({"side": "left"})
        ''' QUIT '''
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.wm_title("AES")
app = Application(master=root)
app.mainloop()
root.destroy()
