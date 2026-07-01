from health_analyzer import HealthAnalyzer

health = HealthAnalyzer()

results = health.analyze(5)

print()
print("Host Health Summary")
print("------------------------------")

for host, stats in results.items():

    print(host)

    print("Successful :", stats["successful"])

    print("Failed     :", stats["failed"])

    print("Unreachable:", stats["unreachable"])

    print("Changed    :", stats["changed"])

    print("------------------------------")

health.close()
