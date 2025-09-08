import pytest

@pytest.mark.usefixtures("setup")
class passclass :
    pass # 아무런 작업을 하지 않는다. (passclass는 setup 픽스쳐에 대한 정보를 가지고 있다.
         # 부모 클래스로서 자식 클래스에 상속해줌으로서 자동적으로 이 자식 클래스도 setup 픽스쳐에 대한 정보를 가지게 됨
         # 하나 하나 픽스쳐를 메소드, 클래스 머리위에 달아주는 것 보다, 이런식으로 여기에 선언 후 passclass를 자식클래스에 할당 해주면 코드가 깔끔해짐
