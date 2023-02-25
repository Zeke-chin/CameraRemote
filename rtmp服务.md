# rtmp服务端搭建

[docker nginx rtmp](https://github.com/leaderyangzi/rtmp)

```shell
docker pull jun3/rtmp
docker run --name rtmp -p 1935:1935 -p 8035:80 -d -it jun3/rtmp
```
服务器推流状态后台 https://IP:8035/stat

# rtmp 推流

MacOS facetime摄像头 推流示例

```shell
ffmpeg -video_size 1280x720 -framerate 30 -f avfoundation -pixel_format uyvy422 -i "0:0" -ar 44100 -f flv rtmp://xxxxxxxx:1935/stream/test
```

ffmpeg命令自查或[参考](https://www.jianshu.com/p/049d03705a81)

ffmpeg 打包（自动重启，保存日志）

[方式一](https://wwc.lanzoum.com/i5z8k0kr5kra)：把命令后写成linux shell文件 用server管理

[方式二](http://amoffat.github.io/sh/)：用python cmd包 执行cmd命令



# ramp直播视频切帧

