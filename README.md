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
```
파이썬 파일(.py) - python 명령어 사용<br>
```
jupyter notebook
```
노트북 파일(.ipynb) - 명령어 실행 후 브라우저의 주피터 노트북 상에서 수정하거나<br>
혹은 vscode의 python extension 설치하면 코드 상에서 수정 가능<br>
(파이썬 kernel을 skplanet-wps으로 설정해야 함)<br>

---

실행 순서
---
1. collector.py로 wifi 데이터 수집
2. 모델 학습에 사용하고자 하는 데이터를 ml_data/signal_data에 넣기
3. make_ml_data.ipynb 실행 (모델 학습용 데이터 생성)
4. randomforest.ipynb와 svm.ipynb로 모델 학습 (ml_data 폴더 안에 저장됨)
5. detection.py로 실시간 인식 수행


