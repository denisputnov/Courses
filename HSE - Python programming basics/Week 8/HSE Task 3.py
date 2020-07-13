print(
    min(
        sorted(
            set(
                map(
                    int,
                    input().split()
                )
            )
        ), key=lambda x: x % 2 == 0
    )
)
