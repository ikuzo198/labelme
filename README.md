# Docker ver.

## quick start

```bash
xhost +
git clone git@github.com:ikuzo198/labelme.git
cd labelme
sudo sh docker/build-docker.sh
(USBカメラを接続したことがない場合は接続が必要)
sudo sh docker/run-docker.sh
```

```bash
(In container)
labelme --labels datasets/label_list/
ex: labelme --labels datasets/label_list/YCB.txt
```

## else

- datasets/label_list/YCB.txt
    - データセットのラベルと合わせる必要がある