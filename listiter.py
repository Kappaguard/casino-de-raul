import itertools


l=[100,500,200,45,23]
print(list(enumerate(l)))
en=enumerate(l)
#for i,e in en:
#    print(i+1,e)
#for i,e in en:
#    print(i+1,e)

r=range(1,11)
i= iter(r)

print(1,next(i))
z=next(i)
print(2,z,next(i))
print(3,i.__next__())
print(4,[x for x in i])
print(5,[x for x in r],[x for x in r])

k=int(-1)
if k<0:
    try:
        print("Ашипка!")
        raise Exception()
    except Exception as e:
        print('1-0, exception', e)
    finally:
        print('Завершение')

i=iter(r)
while True:
    try:
        print(next(i))
    except StopIteration:
        print("Done!")
        break
for i,f in zip(itertools.count(1),itertools.islice(r,5)):
    print(i,f)