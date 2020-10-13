# SK플래닛 Wi-Fi 기반 위치인식
실행환경
-----
Windows 10, Anaconda3(admin)<br>
Anaconda3 가상환경 세팅 파일 -> environment.yaml

Anaconda 3 설치
-----
https://www.anaconda.com/products/individual

---

가상환경 불러오기
-----
Anaconda Prompt에서 프로젝트 폴더로 이동 후
```
conda env create -f environment.yaml
conda env list
```
리스트에서 skplanet-wps 가상환경이 만들어졌는지 확인
```
conda activate skplanet-wps
```
가상환경 활성화

---

스크립트 실행
---
```
python ~.py
make ~
```
파이썬 파일(.py) - python 명령어 사용<br>
```
jupyter notebook
```
노트북 파일(.ipynb) - 명령어 실행 후 주피터 노트북 상에서<br>
혹은 vscode의 python extension 설치 후 실행 가능<br>
(파이썬 kernel을 skplanet-wps으로 설정해야 함)<br>



