# 한글설정 명령어
## -y부분은 설치할 때 yes로 한다는 의미, 무조건 설치됨
```
sudo apt-get install fonts-unfonts-core -y
sudo apt-get install ibus ibus-hangul -y
sudo reboot # 변경사항 적용을 위한 재부팅
```

------------------------------------------------------
AO -> Analog Output
Serial.begin(9600); -> 9600의 속도로 시작
Serial 통신으로 자신의 데이터 전달
미들웨어 - python으로 작업, Serial과 연결
DB, GUI를 미들웨어에 설치 그리고 DB에서 GUI를 가져옴
이때, DB는 influxDB이다.

------------------------------------------------------
PIR 센서 -> 0과 1의 출력값만 출력
Serial로 하다가 바로 python으로 실해하면 오류남

------------------------------------------------------
# influx(influx1) 설치
# 데이터베이스 생성 명령어
```
create database 'pir'
```

# 파이썬 라이브러리 설치
```
sudo pip3 install influxdb
```

# 파이썬 파일 실행 명령어 -> python [파일명]
```
python pir_influxdb.py
```
