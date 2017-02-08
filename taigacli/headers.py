def point():
    return ["ID", "Name", "Value"]

def project():
    return ["Project ID", "Slug", "Name"]

def userstory():
    return ["ID", "Subject", "Assigned", "Closed", "Time"] + ["Project"]
