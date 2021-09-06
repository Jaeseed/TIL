### 1. Form

##### form

- 유효성 도구들 중 하나이다.
- 공격 및 우연한 데이터 손상에 대한 중요한 방어수단이다.
- form 기능을 단순화, 자동화 할 수 있다.



##### form 선언하기

- Model 선언과 유사하다.
- from django import forms 필요. 
- 앱 하위에 forms.py 파일 생성 



##### form 사용하기

- views에서 Model과 마찬가지로 모듈 import 해야함 ex) from .forms import ArticleForm
- 렌더링 옵션: as_p(), as_ul(), as_table()로 감싸서 label과 input 태그의 역할을 할 수 있다.



##### widgets

- 웹 페이지의 input 요소 렌더링
- 반드시 form fields에 할당 됨





### 2. ModelForm



##### ModelForm

- 이미 모델에서 필드(ex) title, content)를 정의했기 때문에 form에서 재정의하는 중복된 행위 방지
- ModelForm Class: Model을 통해 Form Class를 만들 수 있는 helper, view에서 사용 가능





##### ModelForm 선언하기

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = __all__
        # exclude = ('title'.)  # title이라는 field를 제거 가능
        
## 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
```

- 모델 정보 ex) model = Article , 필드 입력 범위 ex) fields = '던더all던더'  좌측 두 정보가 필수 입력 요소이다.



##### Meta class

- ModelForm 사용 시 필요한 모델에 대한 정보를 작성하고 구성한다.





##### views.py에서 기존의 create가 어떻게 변하는지 예시

```python
def create(request):
    form = Article(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles.detail', article.pk)
    return redirect('articles:new')
## 유효성 검증 및 검증 실패 시 다시 new로 보냄
```



create까지 복습 완료