# -*- coding: utf-8 -*-


if __name__ == "__main__":
    dict = {"nom":"DUPONT","prenom":"Robert"}
    str = "le nom : {0[nom]} le prenom : {0[prenom]}".format(dict)

    str2 = "le nom : {nom} le prenom : {prenom}".format(nom="DUPONT",prenom="Robert")
    str3 = "le nom : {nom} le prenom : {prenom}".format(**dict)
    print(str2)
    print(str3)

