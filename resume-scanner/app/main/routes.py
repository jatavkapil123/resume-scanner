from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.main.forms import ResumeUploadForm, JobDescriptionForm
from app.models import Resume, JobDescription
from app.utils.parsing import parse_resume
from app.utils.matching import match_resumes_to_jobs

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    resumes = Resume.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', resumes=resumes)

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = ResumeUploadForm()
    if form.validate_on_submit():
        resume_file = form.resume.data
        resume_text = resume_file.read().decode('utf-8')
        parsed_data = parse_resume(resume_text)
        resume = Resume(user_id=current_user.id, **parsed_data, raw_text=resume_text)
        db.session.add(resume)
        db.session.commit()
        flash('Resume uploaded and parsed successfully!')
        return redirect(url_for('main.dashboard'))
    return render_template('upload.html', form=form)

@bp.route('/job_description', methods=['GET', 'POST'])
@login_required
def job_description():
    form = JobDescriptionForm()
    if form.validate_on_submit():
        job_description = JobDescription(title=form.title.data, description=form.description.data)
        db.session.add(job_description)
        db.session.commit()
        flash('Job description added successfully!')
        return redirect(url_for('main.dashboard'))
    return render_template('job_description.html', form=form)

