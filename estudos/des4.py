
k = input("Infome um alguma coisa.\n")
print(type("O valor é do tipo: "))

print(k.isnumeric(), "É númerico - Difere isdigit aceit n° em outra lingua.\n")
print(k.isalpha(), "É alfabético.\n")
print(k.isalnum(), "É alfanúmerico.\n")
print(k.isascii(), "Todos os caracteres São strings.\n")
print(k.islower(), "É uma string em caixa baixa.\n ")
print(k.isupper(), "É uma string em caixa alta.\n")
print(k.isspace(), "É espaço.\n")
print(k.isprintable(), "Todos os caracteres podem ser mostrados na tela.\n")
print(k.istitle(), "A primeira letra é maiúscula e o restante minúscula.\n")
print(k.isdigit(), "São apenas digitos númericos.\n")
