
def display(results):
    for result in results:
            for job_info in result:
                for key, value in job_info.items():
                    print(key, " -> ", value)
                print()