def get_custom_metadata(info, audio):

    prompt = info["relpath"].replace(",", " ").replace("_", " ")
    return {"prompt": prompt}