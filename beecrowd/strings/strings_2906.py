class Email():
    def __init__(self, casos):
        self.lista_emails = [input() for i in range(casos)]

    
    def encontra_arroba(self, email):
        return email.find('@')
    
    def encontra_sinal_de_mais(self, email):
        return email.find('+')
    
    def higieniza(self, email):
        indice_arroba = self.encontra_arroba(email)
        indice_sinal_mais = self.encontra_sinal_de_mais(email)
        inicio = email[:indice_arroba]
        final = email[indice_arroba:]        
        
        if indice_sinal_mais > 0:
            inicio = inicio[:indice_sinal_mais]
    
        inicio = inicio.replace('.', '')
        
        return inicio + final

    def unicos(self):
        self.emails_unicos = set(list(map(self.higieniza, self.lista_emails)))
        return len(self.emails_unicos)
    
obj = Email(int(input()))
print(obj.unicos())