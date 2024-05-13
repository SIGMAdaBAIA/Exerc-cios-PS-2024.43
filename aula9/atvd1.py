alunos = ["Maynara","Luiz Carlos","Luiz Gustavo","Arthur","Anderson","Gabriel","Luana","Higor","Pedro","Luiz F.","Felipe"]

alunos.append("Adrian")
a = 0
for i in alunos:
    if i[0]=="A":
        a+=1
print("Há",a,"nomes que começam com a letra A")