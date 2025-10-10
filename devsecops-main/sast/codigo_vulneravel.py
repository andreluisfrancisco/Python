import os

def funcao_nao_segura():
    os.system("dir C:\\tmp\\{}".format(input_usuario))

input_usuario = input("Digite um diretório: ")
funcao_nao_segura()