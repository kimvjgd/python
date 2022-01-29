users = [
    {
        'name':'홍길동',
        'age':'20',
        'address':'서울',
    }, # 회원 정보
    {
        'name':'고길동',
        'age':'21',
        'address':'부산',
    },
    {
        'name':'황길동',
        'age':'23',
        'address':'평양',
    },
]

def main():
    for user in users:
        print(f"{user['name']}\t{user['age']}\t{user['address']}")

main()