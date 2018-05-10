
from pytube import YouTube
error = 0
errorname = []
for name in open('D:/youtube.txt','r'):

    yt = YouTube(name)
# ダウンロードできる形式を表示
    for video in yt.get_videos():
      print(video)
    print('-' * 20)
    # ファイル名を表示
    print(yt.filename)

    print('-' * 20)
    # ダウンロードしたい形式を選択
    try:
        video = yt.get('mp4', '720p')
    # ダウンロードするファイル名を指定
    # yt.set_filename('download_pytube')
    # ダウンロード実行
        video.download('D:')
    except:
        print("not 720p")
        try:
            video = yt.get('mp4', '360p')
            video.download('D:')
        except:
            print('not 360p \n SKIP')
            error += 1
            errorname.append(yt.filename)
            continue



print("error {}".format(error))
for misname in errorname:
    print(misname)