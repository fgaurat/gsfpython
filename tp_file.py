# -*- coding: utf-8 -*-


if __name__ == "__main__":

    with open("le_fichier.txt",'a') as f:
        f.write("toto\n")
        f.write("tata\n")
        f.write("titi\n")
    
    
    with open("le_fichier.txt") as f:   
        la_list = []
        for line in f:
            la_list.append(line)
        print(la_list)

        