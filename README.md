# GMFT 테이블 추출 데모

[GMFT](https://github.com/conjuncts/gmft) 라이브러리를 사용하여 PDF 문서에서 테이블을 추출하고 Markdown 으로 출력  
(GPU 없이 **Windows + CPU** 환경만으로 동작)

## 0) conda 가상환경 예시
```bash
# conda 프롬프트에서 실행 (Python 3.11 권장)
conda create -n gmft python=3.11 -y
conda activate gmft
# pip 로 gmft 전용 의존성 설치
pip install -r requirements_gmft.txt
```

## 1) 가상 환경 생성 및 의존성 설치 (Windows CMD 기준)
```cmd
:: 프로젝트 루트에서 실행
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

> 첫 실행 시 Microsoft Table-Transformer 모델(약 270 MB)이 자동으로 다운로드되어 캐시에 저장됩니다.

## 2) 스크립트 실행

Example:
```cmd
    python gmft_extract.py --pdf documents/"The Technology Bubble_ 25 Years On.pdf" --out results/bubble.md
```
```cmd    
    python gmft_extract.py --pdf documents/"Attention Is All You Need.pdf" --out results/attention.md
```

## 출력 예시
```
### Table 1
| Year | Revenue ($M) | Employees |
|------|--------------|-----------|
| 2022 | 123.4        | 250       |
| 2023 | 150.2        | 320       |
| 2024 | 185.7        | 410       |
```

## 참고
- `extract_tables.py` 는 CPU 전용으로 동작
- 더 복잡한 PDF 에 대해서도 동일한 방식으로 적용 가능
- GMFT 객체는 `to_pandas()`, `to_csv()`, `to_json()` 등 다양한 형식으로 내보내기를 지원
