import sys

class CLIUNKO:
    """
    ===========
    CLIUNKO: 使い方
    画面上になんか色々表示するだけ
    python unkoApp.py command
    ===========
    """
    def __init__(self, argv):
        self.argv = argv
        self.key = {
            'help' : self.help,
            'useage': self.usage,
        }
        self.logo = '''
        
            ), 
           (.:;)
          (.,:;;)
        This is Unko
        '''[1:-1]
        self.version = '0.0.0'

    def parse(self):
        if not self.argv:
            self.usage()
        else:
            func = self.key.get(self.argv[0])
            if func is not None:
                if '-h' in self.argv:
                    print("-- ヘルプ --")
                    print(func.__doc__)
                else:
                    try:
                        func()
                    except:
                        print(func.__doc__)
            else:
                if '-v' in self.argv[0]:
                    print('CLIUNKO : '+self.version)
                    print(self.logo)
                else:
                    # 未定義のコマンド
                    print("コマンド: {} は定義されていません".format(self.argv[0]))
                print(self.__doc__)

    ### Command
    def help(self):
        """
        特に何もしません
        """
        print(self.__doc__)

    def usage(self):
        """
        特に何もしません
        """
        print(self.__doc__)


if __name__ == '__main__':
    cli = CLIUNKO(sys.argv[1:]).parse()
