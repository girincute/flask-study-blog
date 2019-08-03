# flask-study-blog
### vscode - setting.json 설정
- pylint 관련 설정
  - `"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"],` 추가
### db 커맨드라인
``` shell
from app import db
db.create_all() 

from app import User, Post 
user_1 = User(username='test1', email='test1@test.com', password='password')
db.session_add(user_1)

db.session.commit()

user = User.query.get(1)
post_1 = Post(title='title 1', content='First Post', user_id=user.id)  
post_2 = Post(title='title 2', content='Second Post', user_id=user.id)  
db.session.add(post_1) 
db.session.add(post_2)  

db.session.commit() 
```
