#!/usr/bin/python3.8

import requests
import hashlib
import optparse

class Main(object):
    def __init__(self):
        self.option = Options()
        self.hash = Hash()
        self.start()

    def start(self):
        file_path = self.option.opt_parser()
        hash_sum = self.hash.hashing(file_path)

        print(hash_sum)


class Options(object):
    def opt_parser(self):
        parser = optparse.OptionParser()
        parser.add_option("-f", "--file",
                          dest="file_path",
                          help="Add file path for chack")

        return self.check_input(parser)

    def check_input(self, parser):
        options = parser.parse_args()[0]

        if not options.file_path:
            mes = "[-] Please specify an interface, use -- help for more info."
            parser.error(mes)

        return options.file_path


class Hash(object):
    def __init__(self):
        self.m = hashlib.md5()

    def hashing(self, file_path):
        with open(file_path) as f:
            self.m.update(f.read().encode("utf-8"))
            return self.m.hexdigest()


class Call(object):
    def __init__(self):
        pass

    def requests(self, url):
        pass


if __name__ == "__main__":
    main = Main()