#coding: utf-8
import json
import sys
import collections

class json_to_compressed_type_format:
    def __init__(self, json_str, simple_dict = False):
        self.json_str = json_str
        self.simple_dict = simple_dict

        self.to_compressed_type_format()

    def to_compressed_type_format(self):
        json_data = json.loads(self.json_str)
        def walk(brunch):
            if type(brunch) == int:
                return "int"
            if type(brunch) == long:
                return "long"
            elif type(brunch) == float:
                return "float"
            elif type(brunch) == bool:
                return "bool"
            elif type(brunch) == type(None):
                return "null"
            elif type(brunch) == unicode:
                return "str"
            elif type(brunch) == list:
                return tuple(frozenset([walk(node) for node in brunch]))
            elif type(brunch) == dict:
                if self.simple_dict:
                    return frozenset([(walk(key), walk(brunch[key])) for key in brunch])
                else:
                    return frozenset([(key, walk(brunch[key])) for key in brunch])
            else:
                print >>sys.stderr, type(brunch), brunch
                raise

        self.compressed_json = walk(json_data)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        def walk(brunch):
            if type(brunch) == str:
                return brunch
            elif type(brunch) == tuple:
                return "[%s]" % ", ".join([walk(item) for item in brunch])
            elif type(brunch) == frozenset:
                return "{%s}" % ", ".join(["%s:%s" %(k, walk(v)) for k,v in brunch])
            elif type(brunch) == type(None):
                return "null"
            else:
                print >>sys.stderr, "to_str_error", type(brunch), brunch
                raise

        return walk(self.compressed_json)


if __name__ == "__main__":
    print "--object number"
    print json_to_compressed_type_format("1")
    print json_to_compressed_type_format("1.1")
    print json_to_compressed_type_format("100000000000")

    print "--object str"
    print json_to_compressed_type_format('"hoge"')

    print "--object list"
    print json_to_compressed_type_format('["hoge", 1, 1.1]')

    print "--object dict normal"
    print json_to_compressed_type_format('{"age":9, "gender":"Female", "name":"sakura"}')

    print "--object dict simple"
    print json_to_compressed_type_format('{"age":9, "gender":"Female", "name":"sakura"}', True)

    print "--nested object"
    print json_to_compressed_type_format('''[
            {"age":9, "gender":"Female", "name":"sakura"},
            {"age":10, "gender":"Male", "name":"xaolong"}
    ]''')

    print "--twitter json sample"
    try:
        twitter_json = open("./sample.json").read()
    except:
        print "cant open sample file"
        exit()

    print "--normal mode--"
    print json_to_compressed_type_format(twitter_json)
    print "--simple mode--"
    print json_to_compressed_type_format(twitter_json, True)


