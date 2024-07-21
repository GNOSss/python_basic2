def validate_args(*validators):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # args 는 multiply(10,5) 즉 인자 10과5이며 len(args)는 2
            # validators 는 데코레이터 검증 함수 lambda들이다 즉 검증함수가 2개이며 len(validators) 는 2
            if len(args) != len(validators):
                print("⚠️ 인자 수와 검증자 수 불일치")
                return
            # zip(agrs,validators)는 args[n]번째와 validators[n]번째를 튜플로 묶어주는 것
            # zip으로 묶인 인자와 검증함수를 for문으로 분리하여 꺼내 순회시킴
            for arg, validator in zip(args, validators):
                # arg(인자)가 validator(함수 , 여기선 lambda) 인자로 들어가서 실행되는데
                # if not 즉 False면 print("인자 조건 불충족")
                if not validator(arg):
                    print("⚠️ 인자 조건 불충족")
                    return

            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_args(lambda x: isinstance(x, int), lambda y: y > 0)
def multiply(x, y):
    print(x * y)


multiply(10, 5)

# multiply(10)
# multiply(10, 5, 7)
#
# multiply(10.1, 5)
# multiply(10, -5)