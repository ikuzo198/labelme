# Docker ver.

## quick start

```bash
git clone git@github.com:ikuzo198/labelme.git
cd labelme
sudo sh docker/build-docker.sh
sudo sh docker/run-docker.sh
```

```bash
(In container)
labelme --labels datasets/label_list/
ex: labelme --labels datasets/label_list/YCB.txt
```