import sentry_sdk

sentry_sdk.init(
    dsn="https://52c5fc5181ec754a8cbb018e8d5e0087@us.sentry.io/4506680887345152",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

if __name__ == "__main__":
    for i in range(1, 99):
        if i == 30:
            division_by_zero = 1 / 0
            print(division_by_zero)
        else:
            print("ok")
