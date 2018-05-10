import time, os, random, pygame.mixer

start_time = 60.0
playtime = 20
playpath = 'C:/Users/sin/Desktop/test_sabi_music/'


def main():
    t1 = time.time()
    list = os.listdir(playpath)
    random.shuffle(list)

    for name in list:
        if (name.find('mp3') != -1):
            start_time = int(name[0:2])
            # mixerモジュールの初期化
            pygame.mixer.init()
            # 音楽ファイルの読み込み
            pygame.mixer.music.load(playpath + name)
            # 音量設定
            pygame.mixer.music.set_volume(0.1)
            # 音楽再生、および再生回数の設定(-1はループ再生)
            pygame.mixer.music.play(start=start_time)
            print(name[2:])
            time.sleep(playtime)
            # 再生の終了
            pygame.mixer.music.fadeout(1000)

    print("PlayEnd")
    print("total play time " + str(int(time.time() - t1)) + "秒")


if __name__ == '__main__':
    main()
