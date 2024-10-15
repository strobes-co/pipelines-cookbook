def run_pipeline(input):
    title = input.title
    description = ""
    if input.prefetched_cve:
        for cve in input.prefetched_cve:
            title = cve.cve_id + " - "+title
            description = cve.description
            break
    else:
        description = input.description
    return {"title": title, "desription": description}
