import pickle
import os


class game:
    def __init__(self, BT, img, name, message):
        self.BT = BT
        self.img = img
        self.name = name
        self.message = message

    def print_message(self):
        print(self.BT)
        print(self.img)
        print(self.name)
        print(self.message)


path = 'e:/热门'


def serialization(game):
    if not os.path.exists(path):
        os.mkdir(path)
    f = open(path + '/' + game.name + '.pkl', 'rb')
    return pickle.load(f)


def deserialization():
    files = os.listdir(path)
    games = []
    for file in files:
        f = open(path+'/'+file,'rb')
        try: #异常处理,防止获取空的内容导致程序终止
            Game = pickle.load(f)
            games.append(Game)
        except BaseException as e:
            print(e)
        finally:
            f.close()
    for game in games:
        game.print_message()
    print("获得的了序列化对象有"+str(len(games)))

if __name__ == '__main__':
    with open("E:/热门/Trials Rising.pkl",'rb') as f:
        game = pickle.load(f)
        game.print_message()

    # deserialization()
    # f = open('e:/尝试/' + game1.name, 'rb')
    # game2 = pickle.load(f)
    # game2.print_message()
