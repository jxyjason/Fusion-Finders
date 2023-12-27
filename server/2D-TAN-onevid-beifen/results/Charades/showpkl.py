import pickle
path='TAN_vgg_rgb_test.pkl'   #path='/root/……/aus_openface.pkl'   pkl文件所在路径
	   
f=open(path,'rb')
data=pickle.load(f)

print(len(data))
print(data)

