from datetime import datetime

from pybo.models import Question
from pybo import create_app, db

def insert_test_data(n=300):
    """테스트용 질문 데이터 n개 생성"""
    app = create_app()
    with app.app_context():  # flask 컨텍스트 필요
        for i in range(n):
            q = Question(
                subject=f'테스트 데이터입니다.: [{i:03d}]',
                content='내용없음',
                create_date= datetime.now()
            )
            db.session.add(q)
        db.session.commit()
        print(f'{n}개의 테스트 데이터가 생성되었습니다.')

if __name__ == '__main__':
    insert_test_data()
