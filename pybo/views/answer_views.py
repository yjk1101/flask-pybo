from datetime import datetime

from flask import Blueprint, redirect, request, url_for, render_template

from pybo.forms import AnswerForm
from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods = ['POST'])
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        # content = request.form['content']  # 폼태그에 입력된 값 받을 때
        content = form.content.data  # 폼모듈로 입력된 값 받을 때
        answer = Answer(question=question, content=content, create_date=datetime.now())
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('question.detail', question_id = question_id))

    return render_template('question/question_detail.html', question=question, form=form)

