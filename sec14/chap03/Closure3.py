def make_secure_access(data):
    def secure_access(key):
        if key == 'abcd1234':
            return data
        else:
            return "⚠️ 비밀번호 오류"
    return secure_access


access_data = make_secure_access("🎁 기밀정보")


try_1 = access_data("1234abcd")
try_2 = access_data("abcd1234")

print(try_1)
print(try_2)

pass