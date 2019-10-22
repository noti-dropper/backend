# Find-Noun-Python
자연어처리 기능을 수행합니다

## API

 - `POST` **/api/analyze-sentence**
   - **object** *(body)*: 
   ```javascript
   {
       "sentence": "입력할 문장"
   }
   ```
   - **response**
   ```javascript
   {
       "result": ["결과값 리스트(배열)"]
   }
   ```


## Dependancy
 - Python `(>=3)`
 - JDK `(>=8)`
 - pip install
   - flask
   - flask_restful
   - konlpy
  
## 서버 구동

```bash
$ python -m pip install {의존성 관련 라이브러리 설치}
$ python server.py
```
