# -*- coding: utf-8 -*-
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file',help='indiquez le fichier de configuration')
    parser.add_argument('--opt',help='indiquez le fichier de configuration',required=True)

    args = parser.parse_args()
    print(args.config_file)

