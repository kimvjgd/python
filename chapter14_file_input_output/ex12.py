from ex11_pickle_json import load, save, load_json, save_json

def main():
    # datas = [123,45,67,89,]
    datas = []
    for i in range(50):
        datas.append({
            'name':f'kim{i}',
            'age':f'{20+i}'
        })
    
    
    # 2022/ 01/ 11 15:00~ 강의 참조
    
    #pickle
    save('data1.dat', datas)        # dat - binary data 의 확장자
    
    content = load('data1.dat')
    print(content)
    
    
    # json
    save_json('data_json.json', datas)        # dat - binary data 의 확장자
    
    content = load_json('data_json.json')
    print(content)
    
    
    
    

main()