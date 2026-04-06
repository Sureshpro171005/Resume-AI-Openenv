def calculate_similarity(resume, job):
    resume_words = set(resume.lower().split())
    job_words = set(job.lower().split())

    if len(job_words) == 0:
        return 0.0

    score = len(resume_words & job_words) / len(job_words)
    return score