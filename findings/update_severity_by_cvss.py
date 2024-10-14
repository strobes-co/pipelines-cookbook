def run_pipeline(input):
    if input.cvss and input.cvss.score:
        if input.cvss.score >= 9.0:
            return {"severity": 5}  # Critical
        elif input.cvss.score >= 7.0:
            return {"severity": 4}  # High
        elif input.cvss.score >= 4.0:
            return {"severity": 3}  # Medium
        elif input.cvss.score >= 0.1:
            return {"severity": 2}  # Low
        else:
            return {"severity": 1}  # Info
    return {}
